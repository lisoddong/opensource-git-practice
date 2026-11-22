import pytest
from bank import Account
from service import AccountRepository, AccountService


def test_service_withdrawal_updates_repository_state():
    repo = AccountRepository()
    repo.save(Account("A", 1000))
    service = AccountService(repo)
    service.withdraw("A", 400)
    assert repo.find_by_id("A").balance == 600
    assert service.balance_of("A") == 600


def test_rejected_withdrawal_does_not_modify_stored_account():
    repo = AccountRepository()
    repo.save(Account("A", 1000))
    service = AccountService(repo)
    with pytest.raises(ValueError):
        service.withdraw("A", 1001)
    assert repo.find_by_id("A").balance == 1000


def test_unknown_account_rejects():
    service = AccountService(AccountRepository())
    with pytest.raises(ValueError):
        service.withdraw("missing", 100)
