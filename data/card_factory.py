"""Test ucun request body-leri yaradir.

Her cagirisda unikal id ve test kart nomresi (4111...) verir ki,
testler bir-birinin melumatina qarismasin.
"""
import random
import uuid

VALID_STATUSES = ["ACTIVE", "BLOCKED", "EXPIRED"]


def test_card_number() -> str:
    return "41111111" + "".join(random.choices("0123456789", k=8))


def make_card_request(status: str = "ACTIVE", **overrides) -> dict:
    body = {
        "id": f"autotest-{uuid.uuid4().hex[:8]}",
        "cardNumber": test_card_number(),
        "requestedStatus": status,
    }
    body.update(overrides)
    return body
