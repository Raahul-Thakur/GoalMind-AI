"""Helpers that create chart-friendly data structures for Streamlit."""

from __future__ import annotations

from typing import Dict, List

from database import queries


def team_overview() -> List[Dict[str, object]]:
    """Return table-ready overview of the manager team."""

    team = queries.get_team()
    rows = []
    for player in team["players"]:
        rows.append(
            {
                "Name": player["name"],
                "Team": player["team"],
                "Pos": player["position"],
                "xPts": player["expected_points"],
                "Ownership": player["ownership"],
            }
        )
    return rows


def compare_players(names: List[str]) -> List[Dict[str, object]]:
    """Return comparison rows for selected players."""

    player_map = {p["name"]: p for p in queries.get_players()}
    return [player_map[name] for name in names if name in player_map]


def fixture_difficulty() -> List[Dict[str, object]]:
    """Return fixture difficulty for each tracked team."""

    fixtures = queries.get_fixtures()
    return [
        {"Team": fx["team"], "Opponent": fx["opponent"], "FDR": fx["difficulty"], "Kickoff": fx["kickoff"].isoformat()}
        for fx in fixtures
    ]
