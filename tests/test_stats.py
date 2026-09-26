"""GET /api/stats  -- BUNU SEN YAZ

Istifade edeceyin seyler:
  - stats_client.get_stats()        -> clients/stats_client.py
  - StatsResponse.model_validate()  -> models/stats.py
"""
import pytest

from models.stats import StatsResponse


@pytest.mark.smoke
def test_stats_returns_200(stats_client):
    # TODO
    pytest.skip("TODO: sen yaz")


def test_stats_matches_schema(stats_client):
    # TODO: cavabi StatsResponse-a cevir
    pytest.skip("TODO: sen yaz")


def test_stats_total_is_sum(stats_client):
    # TODO: total == outboxCount + failureCount olmalidir
    pytest.skip("TODO: sen yaz")


def test_stats_success_rate_in_range(stats_client):
    # TODO: successRatePercent 0 ile 100 arasinda olmalidir
    # Elave: outboxCount / total * 100 ile de tutusdur (pytest.approx istifade et)
    pytest.skip("TODO: sen yaz")


def test_stats_total_grows_after_processing(stats_client, cards_client):
    # TODO: evvelce total-i oxu, sonra 1 kart emal et, yeniden oxu -> artmalidir
    # Diqqet: Kafka consumer gecikmeyle yaza biler. time.sleep ve ya bir nece
    # defe yoxlamaq (retry) lazim ola biler.
    pytest.skip("TODO: sen yaz")
