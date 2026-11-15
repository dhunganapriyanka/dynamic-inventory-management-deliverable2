# Dynamic Inventory Management System — Deliverable 2

A Python proof of concept based on Deliverable 1. A dictionary stores products by unique ID, and a list records successful inventory changes.

## Requirements
Python 3.10+ (standard library only).

## Run the demonstration
```bash
python demo.py
```

## Run the tests
```bash
python -m unittest -v
```

## Files
- `inventory.py`: InventoryManager class and validation
- `demo.py`: demonstration of add, search, update, delete
- `test_inventory.py`: automated tests including edge cases

## Current limitations
Data exists only while the program runs. There is no database, multi-user support, or graphical interface. Money is represented using floats for demonstration only; a production application should use decimal or integer cents.
