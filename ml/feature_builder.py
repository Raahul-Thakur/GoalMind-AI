"""Feature engineering helpers for the mock models."""

from __future__ import annotations

from typing import Dict, List

from utils.constants import MOCK_PLAYERS


def build_player_features(players: List[Dict[str, object]] | None = None) -> List[Dict[str, object]]:
    """Add a few derived stats to player dictionaries."""

    players = players or MOCK_PLAYERS
    enriched = []
    for player in players:
        form_score = player.get("expected_points", 0) * (1 + player.get("ownership", 0) / 100)
        difficulty_modifier = max(1, 5 - player.get("fixture_difficulty", 3)) / 5
        enriched.append({**player, "form": form_score, "adjusted_xpts": form_score * difficulty_modifier})
    return enriched
