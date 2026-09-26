"""Swagger-deki schema-larin Python versiyasi.

Cavabi model-e cevirende (model_validate) sahe eksikdirse ve ya tipi
sehvdirse, pydantic xeta atir ve test ozu-ozluyunde fail olur.
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ProcessingResult(BaseModel):
    id: str
    cardNumber: str
    success: bool
    externalCallMs: int
    dbWriteMs: int
    kafkaPublishMs: int
    totalMs: int
    errorMessage: Optional[str] = None


class CardStatusRecord(BaseModel):
    recordId: int
    id: str
    cardNumber: str
    requestedStatus: str
    result: str
    processedAt: datetime
