"""Card status endpoint-leri. Testler URL yazmir, bu metodlari cagirir."""
import requests

from clients.base_client import BaseClient


class CardsClient(BaseClient):
    def change_status(self, body) -> requests.Response:
        """POST /api/cards/status"""
        return self.post("/api/cards/status", json=body)

    def change_status_batch(self, items: list) -> requests.Response:
        """POST /api/cards/status/batch"""
        return self.post("/api/cards/status/batch", json=items)

    def list_cards(self) -> requests.Response:
        """GET /api/cards"""
        return self.get("/api/cards")
