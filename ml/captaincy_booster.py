"""Bayesian-like scoring for captaincy choices."""

from __future__ import annotations

from typing import Dict, List

from database import queries
from ml.feature_builder import build_player_features


def score_candidates(limit: int = 3) -> List[Dict[str, object]]:
    """Return top captaincy options with a blended score."""

    features = build_player_features(queries.get_players())
    scored = []
    for player in features:
        reliability = 1 - player.get("ownership", 0) / 200  # penalise extreme ownership swings
        bayes_score = round(player.get("adjusted_xpts", 0) * reliability, 2)
        scored.append({**player, "captain_score": bayes_score})
    return sorted(scored, key=lambda p: p["captain_score"], reverse=True)[:limit]
