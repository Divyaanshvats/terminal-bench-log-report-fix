import json
from pathlib import Path

REPORT = Path("/app/report.json")


def load_report():
    assert REPORT.exists(), "/app/report.json was not created"
    return json.loads(REPORT.read_text())


def test_output_exists():
    """Success criterion 1: Create /app/report.json."""
    assert REPORT.exists()


def test_total_requests():
    """Success criterion 2: total_requests is correct."""
    report = load_report()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Success criterion 3: unique_ips is correct."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Success criterion 4: top_path is correct."""
    report = load_report()
    assert report["top_path"] == "/index.html"