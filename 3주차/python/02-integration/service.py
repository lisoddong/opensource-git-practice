from bank import Account


class AccountRepository:
    def __init__(self):
        self._accounts = {}

    def save(self, account: Account):
        self._accounts[account.account_id] = account

    def find_by_id(self, account_id: str) -> Account:
        if account_id not in self._accounts:
            raise ValueError(f"unknown account: {account_id}")
        return self._accounts[account_id]


class AccountService:
    def __init__(self, repository: AccountRepository):
        self.repository = repository

    def withdraw(self, account_id: str, amount: int):
        account = self.repository.find_by_id(account_id)
        account.withdraw(amount)
        self.repository.save(account)

    def balance_of(self, account_id: str) -> int:
        return self.repository.find_by_id(account_id).balance
