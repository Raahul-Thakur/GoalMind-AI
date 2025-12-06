"""FastAPI router for LLM-backed reasoning endpoints."""

from __future__ import annotations

from fastapi import APIRouter

from llm.llm_engine import synthesize_answer

router = APIRouter(prefix="/llm", tags=["llm"])


@router.get("/answer")
def answer(question: str = "Who to captain this week?"):
    return synthesize_answer(question)
