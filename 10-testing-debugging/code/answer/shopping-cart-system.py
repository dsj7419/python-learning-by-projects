
import unittest

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append({"item": item, "quantity": quantity})

    def remove_item(self, item_name):
        for item in self.items:
            if item["item"].name == item_name:
                self.items.remove(item)
                return
        raise ValueError("Item not found")

    def total_price(self):
        return sum([item["item"].price * item["quantity"] for item in self.items])

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.item1 = Item("Apple", 0.5)
        self.item2 = Item("Banana", 0.3)

    def test_add_item(self):
        self.cart.add_item(self.item1, 3)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["item"].name, "Apple")
        self.assertEqual(self.cart.items[0]["quantity"], 3)

    def test_remove_item(self):
        self.cart.add_item(self.item1, 3)
        self.cart.add_item(self.item2, 2)
        self.cart.remove_item("Apple")
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["item"].name, "Banana")

    def test_total_price(self):
        self.cart.add_item(self.item1, 3)  # 1.5
        self.cart.add_item(self.item2, 2)  # 0.6
        self.assertEqual(self.cart.total_price(), 2.1)

if __name__ == "__main__":
    unittest.main()
