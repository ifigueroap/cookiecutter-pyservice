"""
Health and Readiness Interface Specification.

Provides health and readiness diagnostics.
"""

from fastapi import APIRouter
from models.health import Health
from settings import settings

router = APIRouter()


@router.get("/health", response_model=Health, tags=["Health"])
def health():
    """Diagnose the application's health."""
    return {"status": "pass", "version": settings.version, "releaseId": settings.commit}
