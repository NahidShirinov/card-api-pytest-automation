"""GET /api/cards  (hazir numune)"""
import pytest

from data.card_factory import make_card_request
from models.card import CardStatusRecord


@pytest.mark.smoke
def test_list_cards_returns_200(cards_client):
    response = cards_client.list_cards()

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_list_cards_items_match_schema(cards_client):
    records = cards_client.list_cards().json()

    for item in records[:50]:
        CardStatusRecord.model_validate(item)


def test_processed_card_appears_in_list(cards_client):
    body = make_card_request(status="BLOCKED")
    cards_client.change_status(body)

    records = cards_client.list_cards().json()
    ours = [r for r in records if r["id"] == body["id"]]

    assert len(ours) == 1
    assert ours[0]["requestedStatus"] == "BLOCKED"
    assert ours[0]["result"] in ("SUCCESS", "FAILURE")
