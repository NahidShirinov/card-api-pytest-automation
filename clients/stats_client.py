from clients.base_client import BaseClient


class StatsClient(BaseClient):
    def get_stats(self):
        """GET /api/stats"""
        return self.get("/api/stats")
