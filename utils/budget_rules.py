"""Basic FPL-style budget and squad rule helpers."""

from __future__ import annotations

from typing import Dict, Iterable, List


POSITION_LIMITS = {"GK": 2, "DEF": 5, "MID": 5, "FWD": 3}
TEAM_LIMIT = 3


def validate_transfer(team: Dict[str, object], incoming: Dict[str, object], outgoing: Dict[str, object]) -> bool:
    """Return ``True`` if the move keeps the squad within constraints."""

    if incoming["price"] - outgoing["price"] > team.get("budget", 0):
        return False

    # Check club limit
    current_from_team = sum(1 for p in team["players"] if p["team"] == incoming["team"])
    if current_from_team >= TEAM_LIMIT and incoming["team"] != outgoing["team"]:
        return False

    # Check positional limit
    pos_count = sum(1 for p in team["players"] if p["position"] == incoming["position"])
    if pos_count >= POSITION_LIMITS.get(incoming["position"], 5):
        return False

    return True


def rank_transfers(team: Dict[str, object], candidates: Iterable[Dict[str, object]]) -> List[Dict[str, object]]:
    """Return ranked list of candidate transfers with simple gain heuristic."""

    suggestions: List[Dict[str, object]] = []
    weakest = min(team["players"], key=lambda p: p.get("expected_points", 0))
    for player in candidates:
        gain = player["expected_points"] - weakest.get("expected_points", 0)
        if validate_transfer(team, player, weakest):
            suggestions.append(
                {
                    "out_name": weakest["name"],
                    "in_name": player["name"],
                    "gain": gain,
                    "cost": max(0.0, player["price"] - weakest.get("price", 0)),
                }
            )
    return sorted(suggestions, key=lambda r: r["gain"], reverse=True)
