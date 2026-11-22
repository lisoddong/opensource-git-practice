import subprocess
import sys
from pathlib import Path

import pytest

from generate_report import build_report


def test_report_revenue(sample_csv, tmp_path):
    report = build_report(sample_csv, tmp_path / "site")
    html = report.read_text(encoding="utf-8")
    assert report.name == "index.html"
    assert "<h1>OrderLab Report</h1>" in html
    assert "Revenue: 35,000 KRW" in html
    assert '<meta charset="utf-8">' in html


def test_report_rebuild_updates_revenue(sample_csv, tmp_path):
    output = tmp_path / "site"
    build_report(sample_csv, output)
    sample_csv.write_text("price,quantity\n100,4\n", encoding="utf-8")
    report = build_report(sample_csv, output)
    assert "Revenue: 400 KRW" in report.read_text(encoding="utf-8")
    assert "35,000" not in report.read_text(encoding="utf-8")


def test_missing_csv_does_not_create_report(tmp_path):
    output = tmp_path / "site"
    with pytest.raises(FileNotFoundError):
        build_report(tmp_path / "missing.csv", output)
    assert not output.exists()


def test_import_does_not_create_site(tmp_path):
    root = Path(__file__).resolve().parents[1]
    subprocess.run(
        [
            sys.executable,
            "-c",
            "import sys; sys.path.insert(0, sys.argv[1]); import generate_report",
            str(root),
        ],
        cwd=tmp_path,
        check=True,
    )
    assert not (tmp_path / "site").exists()
