"""Unit tests for normal inventory operations and edge cases."""
import unittest
from inventory import InventoryManager


class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.manager = InventoryManager()
        self.manager.add_product(101, "Laptop", 10, 899.99, "Electronics")

    def test_add_product(self):
        self.assertEqual(self.manager.search_product(101)["quantity"], 10)

    def test_duplicate_product(self):
        with self.assertRaises(ValueError):
            self.manager.add_product(101, "Mouse", 3, 19.99, "Accessories")

    def test_search_missing(self):
        self.assertIsNone(self.manager.search_product(999))

    def test_update_quantity(self):
        self.manager.update_quantity(101, 7)
        self.assertEqual(self.manager.search_product(101)["quantity"], 7)

    def test_zero_quantity_allowed(self):
        self.manager.update_quantity(101, 0)
        self.assertEqual(self.manager.search_product(101)["quantity"], 0)

    def test_negative_quantity_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.update_quantity(101, -1)

    def test_blank_name_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_product(102, " ", 2, 3.5, "Other")

    def test_negative_price_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_product(102, "Mouse", 2, -3.5, "Other")

    def test_delete_product(self):
        self.manager.delete_product(101)
        self.assertIsNone(self.manager.search_product(101))

    def test_delete_missing_product(self):
        with self.assertRaises(KeyError):
            self.manager.delete_product(999)

    def test_transaction_history(self):
        self.manager.update_quantity(101, 7)
        self.assertEqual(self.manager.transaction_history[-1], ("update", 101, 7))

    def test_search_returns_copy(self):
        returned = self.manager.search_product(101)
        returned["quantity"] = 999
        self.assertEqual(self.manager.search_product(101)["quantity"], 10)

    def test_invalid_id_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.search_product(0)

    def test_invalid_price_infinity_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_product(102, "Mouse", 1, float("inf"), "Accessories")


if __name__ == "__main__":
    unittest.main()
