from models import ShoppingCart


class TestShoppingCart:
    def test_add_new_item(self, default_item: dict):
        cart = ShoppingCart()
        cart.add_item(default_item["item"], default_item["price"], default_item["quantity"])
        assert cart.items == [default_item]

    def test_add_existing_item(self, cart_with_default_item: ShoppingCart):
        cart_with_default_item.add_item("apple", 12, 3)
        assert cart_with_default_item.items == [{"item": "apple", "price": 12, "quantity": 5}]