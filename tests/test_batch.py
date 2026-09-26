"""POST /api/cards/status/batch  -- BUNU SEN YAZ

Numune kimi tests/test_change_status.py faylina bax.
Istifade edeceyin seyler:
  - cards_client.change_status_batch([...])   -> clients/cards_client.py
  - make_card_request()                       -> data/card_factory.py
  - ProcessingResult.model_validate(...)      -> models/card.py

Her testi bitirende pytest.skip(...) setrini sil.
"""
import pytest

from data.card_factory import make_card_request
from models.card import ProcessingResult


def test_batch_returns_200(cards_client):
    # TODO: 3 dene request yarat, batch ile gonder, status 200 oldugunu yoxla
    pytest.skip("TODO: sen yaz")


def test_batch_returns_one_result_per_item(cards_client):
    # TODO: 5 item gonder -> cavabda da 5 netice olmalidir
    pytest.skip("TODO: sen yaz")


def test_batch_keeps_request_order(cards_client):
    # TODO: Swagger deyir ki, neticeler "gonderildiyi ardicilliqla" qayidir.
    # Gonderdiyin id-lerin siyahisi ile cavabdaki id-lerin siyahisi eyni olmalidir.
    # Ipucu: [item["id"] for item in items]
    pytest.skip("TODO: sen yaz")


def test_batch_items_match_schema(cards_client):
    # TODO: cavabdaki her elementi ProcessingResult.model_validate ile yoxla
    pytest.skip("TODO: sen yaz")


@pytest.mark.negative
def test_batch_empty_list(cards_client):
    # TODO: bos siyahi [] gonder. Ne qaytarir? 200 ve [] gozleyirik.
    pytest.skip("TODO: sen yaz")
