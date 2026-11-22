import pytest

from orderlab.csv_report import revenue_from_csv


def test_csv_revenue(tmp_path):
    path = tmp_path / "orders.csv"
    path.write_text("price,quantity\n10000,2\n5000,3\n", encoding="utf-8")
    assert revenue_from_csv(path) == 35_000


def test_fixture_revenue(sample_csv):
    assert revenue_from_csv(sample_csv) == 35_000


@pytest.mark.parametrize("content", ["", "price,quantity\n"])
def test_csv_empty(tmp_path, content):
    path = tmp_path / "empty.csv"
    path.write_text(content, encoding="utf-8")
    assert revenue_from_csv(path) == 0


def test_csv_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        revenue_from_csv(tmp_path / "missing.csv")


@pytest.mark.parametrize("row", ["invalid,2", "1000,invalid", ",2"])
def test_csv_invalid_number(tmp_path, row):
    path = tmp_path / "invalid.csv"
    path.write_text(f"price,quantity\n{row}\n", encoding="utf-8")
    with pytest.raises(ValueError):
        revenue_from_csv(path)


def test_csv_missing_column(tmp_path):
    path = tmp_path / "missing-column.csv"
    path.write_text("price\n1000\n", encoding="utf-8")
    with pytest.raises(KeyError, match="quantity"):
        revenue_from_csv(path)
