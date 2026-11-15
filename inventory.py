"""Dictionary-based inventory proof of concept for Deliverable 2."""
from copy import deepcopy
from math import isfinite


class InventoryManager:
    """Manage products by ID and record successful changes in a list."""

    def __init__(self):
        self.inventory = {}
        self.transaction_history = []

    @staticmethod
    def _validate_id(product_id):
        if type(product_id) is not int or product_id <= 0:
            raise ValueError("Product ID must be a positive integer.")

    @staticmethod
    def _validate_quantity(quantity):
        if type(quantity) is not int or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

    def add_product(self, product_id, name, quantity, price, category):
        self._validate_id(product_id)
        if product_id in self.inventory:
            raise ValueError("Product already exists.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name cannot be blank.")
        if not isinstance(category, str) or not category.strip():
            raise ValueError("Category cannot be blank.")
        if type(price) not in (int, float) or not isfinite(price) or price < 0:
            raise ValueError("Price must be a non-negative finite number.")
        self._validate_quantity(quantity)
        self.inventory[product_id] = {
            "name": name.strip(),
            "quantity": quantity,
            "price": round(float(price), 2),
            "category": category.strip(),
        }
        self.transaction_history.append(("add", product_id, quantity))
        return "Product added successfully."

    def search_product(self, product_id):
        self._validate_id(product_id)
        product = self.inventory.get(product_id)
        return deepcopy(product) if product is not None else None

    def update_quantity(self, product_id, new_quantity):
        self._validate_id(product_id)
        self._validate_quantity(new_quantity)
        if product_id not in self.inventory:
            raise KeyError("Product not found.")
        self.inventory[product_id]["quantity"] = new_quantity
        self.transaction_history.append(("update", product_id, new_quantity))
        return "Quantity updated successfully."

    def delete_product(self, product_id):
        self._validate_id(product_id)
        if product_id not in self.inventory:
            raise KeyError("Product not found.")
        del self.inventory[product_id]
        self.transaction_history.append(("delete", product_id, None))
        return "Product deleted successfully."

    def list_products(self):
        """Traverse the dictionary and return a safe snapshot."""
        return deepcopy(self.inventory)
