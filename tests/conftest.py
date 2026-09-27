"""Fixture-lar ve report ayarlari."""
import html

import pytest

from clients.cards_client import CardsClient
from clients.stats_client import StatsClient
from utils import http_recorder


@pytest.fixture(scope="session")
def cards_client():
    return CardsClient()


@pytest.fixture(scope="session")
def stats_client():
    return StatsClient()


@pytest.fixture(autouse=True)
def _clear_http_log():
    """Her test oz sorgularini temiz siyahi ile baslayir."""
    http_recorder.reset()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Test bitende sorgu/cavablari report-a elave edir.

    Terminalda: yalniz fail olan testin altinda gorunur.
    HTML report-da: her testin yaninda gorunur.
    """
    outcome = yield
    report = outcome.get_result()
    if report.when != "call":
        return

    report.endpoints = http_recorder.endpoints()
    text = http_recorder.as_text()
    if text:
        report.sections.append(("HTTP sorgu ve cavab", text))


# ---------- HTML report-a "Endpoint" sutunu ----------

def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Endpoint</th>")


def pytest_html_results_table_row(report, cells):
    cells.insert(2, f"<td>{html.escape(getattr(report, 'endpoints', ''))}</td>")


def pytest_html_report_title(report):
    report.title = "Card API Test Report"
