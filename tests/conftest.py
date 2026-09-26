"""Fixture-lar: testlere hazir client-ler verir."""
import pytest

from clients.cards_client import CardsClient
from clients.stats_client import StatsClient


@pytest.fixture(scope="session")
def cards_client():
    return CardsClient()


@pytest.fixture(scope="session")
def stats_client():
    return StatsClient()
