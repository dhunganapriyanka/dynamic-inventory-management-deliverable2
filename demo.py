"""Run a small demonstration of inventory operations."""
from inventory import InventoryManager


def main():
    manager = InventoryManager()
    print(manager.add_product(101, "Laptop", 10, 899.99, "Electronics"))
    print(manager.add_product(102, "Mouse", 25, 19.99, "Accessories"))
    print("Search product 101:", manager.search_product(101))
    print(manager.update_quantity(101, 7))
    print("Updated product 101:", manager.search_product(101))
    print(manager.delete_product(102))
    print("Search deleted product 102:", manager.search_product(102))
    print("Current inventory:", manager.list_products())
    print("Transaction history:", manager.transaction_history)
    try:
        manager.add_product(101, "Duplicate", 1, 5.00, "Other")
    except ValueError as error:
        print("Expected duplicate ID error:", error)


if __name__ == "__main__":
    main()
