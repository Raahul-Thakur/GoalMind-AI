"""Utilities for presenting model outputs and stats."""

from __future__ import annotations

from typing import Dict, Iterable, List


def format_player_row(player: Dict[str, object]) -> str:
    """Return a short summary string for a player dictionary."""

    return (
        f"{player['name']} ({player['team']}, {player['position']}) - "
        f"xPts: {player['expected_points']:.1f}, EO: {player['ownership']:.1f}%"
    )


def format_transfer_suggestion(transfers: Iterable[Dict[str, object]]) -> List[str]:
    """Format transfer moves into bullet-friendly strings."""

    suggestions = []
    for move in transfers:
        suggestions.append(
            f"Sell {move['out_name']} for {move['in_name']} (ΔxPts: {move['gain']:+.1f}, cost {move['cost']:.1f}m)"
        )
    return suggestions
