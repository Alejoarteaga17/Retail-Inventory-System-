#!/usr/bin/env bash
# Exercises every endpoint of the inventory API against a running server.
#
#   uvicorn main:app --app-dir src --reload      # terminal 1
#   ./scripts/smoke.sh                           # terminal 2
#
# Override the target with:  BASE_URL=http://host:port ./scripts/smoke.sh
set -euo pipefail

BASE_URL="${BASE_URL:-http://127.0.0.1:8000}"
API="$BASE_URL/api/v1"
JSON=(-H 'Content-Type: application/json')
STAFF=(-H 'X-User-Name: ana.staff'    -H 'X-User-Role: STORE_STAFF')
MANAGER=(-H 'X-User-Name: luis.manager' -H 'X-User-Role: STORE_MANAGER')

step() { printf '\n\033[1;36m== %s\033[0m\n' "$1"; }
call() { curl -sS -w '  [HTTP %{http_code}]\n' "$@"; }

step "Health"
call "$BASE_URL/health"

step "List active items"
call "$API/items"

step "Filter: Decor category only"
call "$API/items?category=Decor"

step "Filter: low stock only"
call "$API/items?low_stock=true"

step "Create an item"
call -X POST "$API/items" "${JSON[@]}" -d '{
  "sku": "KIT-KNF-040",
  "name": "Chef Knife",
  "category": "Kitchen",
  "quantity": 5,
  "reorder_threshold": 10
}'

step "Duplicate SKU is rejected (expect 409)"
call -X POST "$API/items" "${JSON[@]}" -d '{
  "sku": "KIT-KNF-040", "name": "Duplicate", "category": "Kitchen",
  "quantity": 1, "reorder_threshold": 1
}'

step "Stock-in of 10 units on item 3, as Store Staff"
call -X POST "$API/items/3/movements" "${JSON[@]}" "${STAFF[@]}" \
  -d '{"type": "STOCK_IN", "quantity": 10, "note": "Supplier delivery"}'

step "Stock-out of 4 units on item 3"
call -X POST "$API/items/3/movements" "${JSON[@]}" "${STAFF[@]}" \
  -d '{"type": "STOCK_OUT", "quantity": 4, "note": "Sold in store"}'

step "Stock cannot go negative (expect 409)"
call -X POST "$API/items/3/movements" "${JSON[@]}" "${STAFF[@]}" \
  -d '{"type": "STOCK_OUT", "quantity": 9999}'

step "Store Staff may not adjust stock (expect 403)"
call -X POST "$API/items/3/movements" "${JSON[@]}" "${STAFF[@]}" \
  -d '{"type": "ADJUSTMENT", "quantity": 12}'

step "Store Manager may adjust stock (expect 201)"
call -X POST "$API/items/3/movements" "${JSON[@]}" "${MANAGER[@]}" \
  -d '{"type": "ADJUSTMENT", "quantity": 12, "note": "Physical count"}'

step "Movement on an unknown item (expect 404)"
call -X POST "$API/items/9999/movements" "${JSON[@]}" "${STAFF[@]}" \
  -d '{"type": "STOCK_IN", "quantity": 1}'

step "Movement on a deactivated item (expect 409)"
call -X POST "$API/items/8/movements" "${JSON[@]}" "${STAFF[@]}" \
  -d '{"type": "STOCK_IN", "quantity": 1}'

step "Movement history for item 3"
call "$API/items/3/movements"

step "Full movement history"
call "$API/movements"

step "Low-stock alerts"
call "$API/insights/low-stock"

step "Dashboard"
call "$API/insights/dashboard"

step "Deactivate item 9 (soft delete)"
call -X DELETE "$API/items/9"

printf '\n\033[1;32mDone.\033[0m Interactive docs: %s/docs\n' "$BASE_URL"
