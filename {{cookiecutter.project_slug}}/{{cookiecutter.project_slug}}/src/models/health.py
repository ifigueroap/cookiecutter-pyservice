from enum import Enum

from pydantic import BaseModel


class StatusEnum(str, Enum):
    """Health status enumeration."""

    passed = "pass"
    failed = "fail"
    warned = "warn"


class Health(BaseModel):
    """Health model structure.

    A health summary based on the recommendation at:
    https://tools.ietf.org/html/draft-inadarei-api-health-check-05
    """

    status: StatusEnum
    version: str
    releaseId: str
