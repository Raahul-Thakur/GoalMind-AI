"""Heuristic LLM stand-in used for the MVP UI."""

from __future__ import annotations

from typing import Dict, List

from database import queries
from llm.rag_retriever import retrieve_context
from utils.formatters import format_player_row


def synthesize_answer(question: str) -> Dict[str, object]:
    """Return an answer dictionary with rationale and stats."""

    context = retrieve_context(question)
    top_players = queries.top_expected_points(limit=3)
    captain_pick = top_players[0]
    rationale = (
        f"Based on expected points, {captain_pick['name']} is the safest captain. "
        f"Recent fixtures: {context[-1]['text']}."
    )
    stats = [format_player_row(player) for player in top_players]
    return {
        "answer": rationale,
        "captain": captain_pick,
        "support": context,
        "stats": stats,
    }
