import pytest

from orderlab.pricing import final_total, subtotal


def test_subtotal_normal():
    assert subtotal(10_000, 2) == 20_000


def test_subtotal_zero():
    assert subtotal(0, 3) == 0


def test_subtotal_negative():
    with pytest.raises(ValueError, match="negative input"):
        subtotal(-100, 2)


@pytest.mark.parametrize("price, quantity", [(100, -1), (-1, -1)])
def test_subtotal_negative_quantity(price, quantity):
    with pytest.raises(ValueError, match="negative input"):
        subtotal(price, quantity)


@pytest.mark.parametrize(
    "price, qty, discount, expected",
    [
        (10_000, 2, 0, 23_000),
        (49_999, 1, 0, 52_999),
        (50_000, 1, 0, 50_000),
        (50_001, 1, 0, 50_001),
        (10_000, 2, 10, 21_000),
        (100_000, 1, 50, 50_000),
        (50_000, 1, 1, 52_500),
        (10_000, 2, 100, 0),
        (0, 3, 0, 0),
        (10_000, 0, 0, 0),
        (101, 1, 10, 3_091),
    ],
)
def test_final_total(price, qty, discount, expected):
    assert final_total(price, qty, discount) == expected


@pytest.mark.parametrize("discount", [-1, 101])
def test_invalid_discount(discount):
    with pytest.raises(ValueError, match="invalid discount"):
        final_total(10_000, 2, discount)


@pytest.mark.parametrize("price, qty", [(-100, 2), (100, -2)])
def test_final_total_negative_input(price, qty):
    with pytest.raises(ValueError, match="negative input"):
        final_total(price, qty, 0)
