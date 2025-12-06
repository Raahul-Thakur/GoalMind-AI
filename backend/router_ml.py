"""FastAPI router exposing ML-style endpoints."""

from __future__ import annotations

from fastapi import APIRouter

from ml import captaincy_booster, transfer_optimizer

router = APIRouter(prefix="/ml", tags=["ml"])


@router.get("/captaincy")
def captaincy_candidates(limit: int = 3):
    return captaincy_booster.score_candidates(limit=limit)


@router.get("/transfers")
def transfer_suggestions(limit: int = 5):
    return transfer_optimizer.suggest_transfers(limit=limit)
