from pydantic import BaseModel


class StatsResponse(BaseModel):
    outboxCount: int
    failureCount: int
    total: int
    successRatePercent: float
