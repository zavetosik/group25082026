import uuid

class BankAccount:
    def __init__(self, owner: str):
        self.owner = owner
        self.money = 0
        self.id = uuid.uuid7()  # UUID('01a06d8c-4402-71b2-a90e-5f764e656bdc')

    def withdraw_money(self, summa: int) -> None:
        self.money -= summa
        print(f"SMS: {self.id} withdraw_money {summa}. Current balance: {self.money}grn")

    def deposit_money(self, summa: int) -> None:
        self.money += summa
        print(f"SMS: {self.id} deposit_money {summa}. Current balance: {self.money}grn")


class ShoppingCart:
    def __init__(self):
        self.items = []

    def _find_item(self, name: str):
        for item in self.items:
            if item["item"] == name:
                return item
        return None

    def add_item(self, item: str, price: float | int, quantity: int):
        found = self._find_item(item)
        if found is None:
            self.items.append(
                {"item": item, "price": price, "quantity": quantity}
            )
        else:
            found["quantity"] += quantity
            found["price"] = price

    def remove_item(self, item: str):
        found = self._find_item(item)
        if found is not None:
            self.items.remove(found)

    def get_total(self) -> float| int:
        return sum(item["price"] * item["quantity"] for item in self.items)
