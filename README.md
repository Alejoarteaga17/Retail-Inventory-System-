# Retail Inventory Management System

FastAPI backend for **Cornerline Home Goods** inventory catalog management.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --app-dir src --reload --host 127.0.0.1 --port 8000
```

Default URL: http://127.0.0.1:8000  
Interactive docs: http://127.0.0.1:8000/docs

If port 8000 is already in use, pick another one:

```bash
uvicorn main:app --app-dir src --reload --host 127.0.0.1 --port 8080
```

## Inventory Item Endpoints

| Method | Path | Description |
| ------ | ---- | ----------- |
| GET | `/inventory/items` | List active catalog items with current quantities |
| GET | `/inventory/items?include_inactive=true` | Include deactivated items |
| GET | `/inventory/items/{item_id}` | View a single inventory item |
| POST | `/inventory/items` | Create a new inventory item |
| PATCH | `/inventory/items/{item_id}` | Update an inventory item |
| POST | `/inventory/items/{item_id}/deactivate` | Deactivate an inventory item |

### Create / update payload

Required fields on create:

- `name` (string, 1–200 characters)
- `current_quantity` (integer, ≥ 0)
- `reorder_threshold` (integer, ≥ 0)

Update accepts any subset of the same fields via `PATCH`.

### Example

```bash
curl -X POST http://127.0.0.1:8000/inventory/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Bookshelf - Walnut", "current_quantity": 10, "reorder_threshold": 4}'
```

## Project Structure

```
src/
├── main.py                      # FastAPI application entry point
├── dependencies.py              # Shared service instances
├── data/mock_data.py            # Seed catalog data
├── schemas/inventory_item.py    # Request/response models (validation)
├── repositories/                # Data access layer
├── services/                    # Business logic
└── routers/                     # HTTP route handlers
```
