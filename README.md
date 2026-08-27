# Retail Inventory Management System

Inventory API for **Cornerline Home Goods**, built with FastAPI. It covers the
MVP scope defined in [`docs/proposals/statement-of-work-01.md`](docs/proposals/statement-of-work-01.md):
item catalog, stock movements with a full audit trail, and low-stock insights.

Data is served from an in-memory mock store seeded from
[`src/data/inventory_seed.py`](src/data/inventory_seed.py), so **state resets on
every restart**. Swapping in a real database is a change to `data/repositories.py`
and nothing else.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --app-dir src --reload
```

Interactive docs: <http://127.0.0.1:8000/docs>

## Architecture

Layers depend inward only. The domain knows nothing about FastAPI, and the
routers know nothing about how data is stored.

```
src/
├── domain/          Pure business core — no framework imports
│   ├── entities.py      Item, StockMovement
│   ├── enums.py         MovementType, UserRole
│   ├── rules.py         Movement validation (negative stock, permissions)
│   └── errors.py        Business-rule violations
├── data/            Persistence
│   ├── inventory_seed.py    Mock catalog derived from docs/
│   └── repositories.py      In-memory repositories
├── services/        Use cases
│   ├── catalog_service.py   Create, update, view, deactivate items
│   ├── stock_service.py     Record movements, read history
│   └── insights_service.py  Low-stock alerts, dashboard
└── api/             HTTP boundary
    ├── schemas.py       Pydantic request/response contracts
    ├── dependencies.py  Composition root + current actor
    ├── errors.py        Domain error → HTTP status mapping
    └── routers/         items, movements, insights
```

## Endpoints

All inventory endpoints live under `/api/v1`.

| Method | Path | Description |
| ------ | ---- | ----------- |
| `GET` | `/health` | Liveness probe |
| `GET` | `/api/v1/items` | List items — filters: `category`, `low_stock`, `include_inactive`, `q` |
| `POST` | `/api/v1/items` | Create an item |
| `GET` | `/api/v1/items/{id}` | Get one item |
| `PATCH` | `/api/v1/items/{id}` | Update catalog attributes |
| `DELETE` | `/api/v1/items/{id}` | Deactivate (soft delete) |
| `POST` | `/api/v1/items/{id}/reactivate` | Reactivate |
| `POST` | `/api/v1/items/{id}/movements` | Record a stock movement |
| `GET` | `/api/v1/items/{id}/movements` | Movement history for one item |
| `GET` | `/api/v1/movements` | Full movement history |
| `GET` | `/api/v1/insights/low-stock` | Items at or below their reorder threshold |
| `GET` | `/api/v1/insights/dashboard` | Dashboard summary |

## Business rules

| Rule | Behaviour |
| ---- | --------- |
| Quantities never go negative | Stock-out beyond the quantity on hand → `409` |
| No movements on unknown items | → `404` |
| No movements on deactivated items | → `409` |
| Quantity changes only via movements | `PATCH /items/{id}` rejects a `quantity` field |
| Manual adjustments are restricted | Store Staff → `403`; Manager and Owner allowed |
| `ADJUSTMENT` sets, it does not add | A physical recount overrides the system value |
| Low stock is *reached*, not crossed | `quantity <= reorder_threshold` |
| SKUs are unique, case-insensitive | Duplicate → `409` |

Every movement is recorded with its type, quantity, resulting quantity,
timestamp, and the user and role responsible.

## Who is calling

Authentication is **not implemented in this iteration**. The caller is read from
two headers and trusted:

| Header | Default | Values |
| ------ | ------- | ------ |
| `X-User-Name` | `demo.user` | Any string |
| `X-User-Role` | `STORE_STAFF` | `STORE_STAFF`, `STORE_MANAGER`, `OWNER` |

The seam is deliberate: when real authentication lands, only
`api/dependencies.py::get_current_actor` changes — the services already receive
an actor and enforce permissions on it.

## Trying it out

### Swagger UI

<http://127.0.0.1:8000/docs> — click **Try it out** on any endpoint.

### Postman

Import [`docs/postman/retail-inventory.postman_collection.json`](docs/postman/retail-inventory.postman_collection.json).
It ships 22 requests grouped by capability, including the failure cases
(`403`, `404`, `409`). Set the `base_url` collection variable if you are not on
`http://127.0.0.1:8000`.

### One-shot curl script

With the server running:

```bash
./scripts/smoke.sh
```

It walks the whole API — happy paths and every rejection — and prints the status
code for each call.

### Individual curl calls

```bash
API=http://127.0.0.1:8000/api/v1

# Current inventory
curl -s "$API/items" | jq

# Only what needs reordering
curl -s "$API/insights/low-stock" | jq

# Dashboard
curl -s "$API/insights/dashboard" | jq

# Receive 10 units of item 3
curl -s -X POST "$API/items/3/movements" \
  -H 'Content-Type: application/json' \
  -H 'X-User-Name: ana.staff' -H 'X-User-Role: STORE_STAFF' \
  -d '{"type": "STOCK_IN", "quantity": 10, "note": "Supplier delivery"}' | jq

# Sell 4 units
curl -s -X POST "$API/items/3/movements" \
  -H 'Content-Type: application/json' \
  -d '{"type": "STOCK_OUT", "quantity": 4, "note": "Sold in store"}' | jq

# Stock cannot go negative → 409
curl -s -X POST "$API/items/3/movements" \
  -H 'Content-Type: application/json' \
  -d '{"type": "STOCK_OUT", "quantity": 9999}' | jq

# Staff cannot adjust → 403
curl -s -X POST "$API/items/3/movements" \
  -H 'Content-Type: application/json' -H 'X-User-Role: STORE_STAFF' \
  -d '{"type": "ADJUSTMENT", "quantity": 12}' | jq

# Manager can → 201
curl -s -X POST "$API/items/3/movements" \
  -H 'Content-Type: application/json' -H 'X-User-Role: STORE_MANAGER' \
  -d '{"type": "ADJUSTMENT", "quantity": 12, "note": "Physical count"}' | jq

# Audit trail for item 3
curl -s "$API/items/3/movements" | jq

# Create an item
curl -s -X POST "$API/items" \
  -H 'Content-Type: application/json' \
  -d '{"sku": "KIT-KNF-040", "name": "Chef Knife", "category": "Kitchen",
       "quantity": 5, "reorder_threshold": 10}' | jq
```

## Not in this iteration

Authentication, persistent storage, automated tests, supplier management,
purchase orders, and email/SMS notifications. The legacy `/` and `/reservations`
endpoints are leftovers from the starter template and are unrelated to the
inventory domain.
