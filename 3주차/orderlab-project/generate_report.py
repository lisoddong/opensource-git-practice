from pathlib import Path

from orderlab.csv_report import revenue_from_csv

ROOT = Path(__file__).resolve().parent


def build_report(
    csv_path: str | Path = ROOT / "data/sample_orders.csv",
    output_dir: str | Path = ROOT / "site",
) -> Path:
    revenue = revenue_from_csv(csv_path)
    site = Path(output_dir)
    site.mkdir(parents=True, exist_ok=True)
    report = site / "index.html"
    report.write_text(
        "<!doctype html>\n"
        '<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "<title>OrderLab Report</title>\n"
        "<style>body{font-family:system-ui,sans-serif;max-width:48rem;"
        "margin:5rem auto;padding:0 1.5rem;background:#f5f7fa;color:#162235}"
        "main{padding:2rem;background:white;border-radius:1rem}"
        "h1{margin-top:0}p{font-size:1.5rem}</style>\n"
        "</head>\n<body>\n<main>\n<h1>OrderLab Report</h1>\n"
        f"<p>Revenue: {revenue:,} KRW</p>\n"
        "</main>\n</body>\n</html>\n",
        encoding="utf-8",
    )
    return report


if __name__ == "__main__":
    print(build_report())
