class Account:
    def __init__(self, account_id: str, opening_balance: int):
        if not account_id:
            raise ValueError("id required")
        if opening_balance < 0:
            raise ValueError("negative opening balance")
        self.account_id = account_id
        self.balance = opening_balance

    def withdraw(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
