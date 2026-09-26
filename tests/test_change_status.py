"""POST /api/cards/status  (hazir numune)"""
import pytest

from data.card_factory import VALID_STATUSES, make_card_request
from models.card import ProcessingResult


@pytest.mark.smoke
def test_change_status_returns_200(cards_client):
    response = cards_client.change_status(make_card_request())

    assert response.status_code == 200


@pytest.mark.parametrize("status", VALID_STATUSES)
def test_change_status_response_matches_request(cards_client, status):
    body = make_card_request(status=status)

    response = cards_client.change_status(body)

    assert response.status_code == 200
    result = ProcessingResult.model_validate(response.json())
    assert result.id == body["id"]
    assert result.cardNumber == body["cardNumber"]


def test_change_status_error_message_only_on_failure(cards_client):
    # Xarici servis bezen ugursuz olur, ona gore her iki halı yoxlayiriq
    response = cards_client.change_status(make_card_request())
    result = ProcessingResult.model_validate(response.json())

    if result.success:
        assert result.errorMessage is None
    else:
        assert result.errorMessage


def test_change_status_timings_are_consistent(cards_client):
    response = cards_client.change_status(make_card_request())
    result = ProcessingResult.model_validate(response.json())

    stages = [result.externalCallMs, result.dbWriteMs, result.kafkaPublishMs]
    assert all(ms >= 0 for ms in stages)
    assert result.totalMs >= sum(stages) - 5  # yuvarlaqlasdirma ucun kicik tolerans


@pytest.mark.negative
def test_change_status_invalid_json_returns_400(cards_client):
    response = cards_client.session.post(
        f"{cards_client.base_url}/api/cards/status", data="bad json"
    )

    assert response.status_code == 400


@pytest.mark.negative
@pytest.mark.xfail(reason="BUG: bos body 400 yox, 500 qaytarir")
def test_change_status_empty_body_returns_400(cards_client):
    response = cards_client.change_status({})

    assert response.status_code == 400


@pytest.mark.negative
@pytest.mark.xfail(reason="BUG: movcud olmayan status qebul olunur")
def test_change_status_unknown_status_is_rejected(cards_client):
    response = cards_client.change_status(make_card_request(status="XYZ"))

    assert response.status_code == 400
