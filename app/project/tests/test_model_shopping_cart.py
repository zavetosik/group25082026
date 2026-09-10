from models import ShoppingCart


class TestShoppingCart:
    def test_add_new_item(self):
        cart = ShoppingCart()
        cart.add_item("apple", 10, 2)
        assert cart.items == [{"item": "apple", "price": 10, "quantity": 2}]