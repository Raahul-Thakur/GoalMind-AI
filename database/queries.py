"""Query helpers sitting on top of the local mock datastore."""

from __future__ import annotations

from typing import Dict, List

from database.connect import load_json
from utils.constants import CURRENT_GAMEWEEK, MOCK_FIXTURES, MOCK_PLAYERS, MOCK_TEAM
from utils.logger import get_logger

LOGGER = get_logger(__name__)


def get_players() -> List[Dict[str, object]]:
    """Return player pool; falls back to ``MOCK_PLAYERS`` if no data file exists."""

    return load_json("players.json", MOCK_PLAYERS)


def get_team() -> Dict[str, object]:
    """Return the manager team snapshot."""

    return load_json("team.json", [MOCK_TEAM])[0]


def get_fixtures() -> List[Dict[str, object]]:
    """Return upcoming fixtures."""

    return load_json("fixtures.json", MOCK_FIXTURES)


def top_expected_points(limit: int = 5) -> List[Dict[str, object]]:
    """Return top players by expected points for the current gameweek."""

    players = get_players()
    sorted_players = sorted(players, key=lambda p: p.get("expected_points", 0), reverse=True)
    return sorted_players[:limit]


def gameweek_context() -> str:
    """Return a short string describing the current gameweek state."""

    fixtures = get_fixtures()
    fixture_summary = ", ".join(f"{fx['team']} vs {fx['opponent']}" for fx in fixtures)
    return f"GW{CURRENT_GAMEWEEK} ({len(fixtures)} fixtures): {fixture_summary}"
