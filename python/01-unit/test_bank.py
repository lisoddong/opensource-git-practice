import pytest
from bank import Account


def test_partial_withdrawal_changes_balance():
    a = Account("A", 1000)
    a.withdraw(400)
    assert a.balance == 600


def test_full_withdrawal_allows_zero_balance():
    a = Account("A", 1000)
    a.withdraw(1000)
    assert a.balance == 0


def test_insufficient_balance_rejects_and_preserves_balance():
    a = Account("A", 1000)
    with pytest.raises(ValueError):
        a.withdraw(1001)
    assert a.balance == 1000


@pytest.mark.parametrize("amount", [0, -1])
def test_nonpositive_amount_rejects(amount):
    a = Account("A", 1000)
    with pytest.raises(ValueError):
        a.withdraw(amount)
    assert a.balance == 1000
