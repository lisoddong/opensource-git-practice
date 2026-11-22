import csv
from pathlib import Path


def revenue_from_csv(path: str | Path) -> int:
    with open(path, encoding="utf-8", newline="") as csv_file:
        rows = csv.DictReader(csv_file)
        return sum(int(row["price"]) * int(row["quantity"]) for row in rows)
