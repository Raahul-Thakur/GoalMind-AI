"""Suggest transfers using a lightweight heuristic."""

from __future__ import annotations

from typing import Dict, List

from database import queries
from utils.budget_rules import rank_transfers


def suggest_transfers(limit: int = 5) -> List[Dict[str, object]]:
    """Return the top transfer moves for the manager team."""

    team = queries.get_team()
    candidates = [p for p in queries.get_players() if p["id"] not in {player["id"] for player in team["players"]}]
    ranked = rank_transfers(team, candidates)
    return ranked[:limit]
