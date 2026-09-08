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
