"""Project-wide constants and small mock datasets used by the MVP."""

from __future__ import annotations

from datetime import date
from typing import Dict, List

# Basic static info that the rest of the modules can reuse
CURRENT_GAMEWEEK = 5
SEASON = "2024/25"

MOCK_PLAYERS: List[Dict[str, object]] = [
    {
        "id": 1,
        "name": "Erling Haaland",
        "team": "MCI",
        "position": "FWD",
        "expected_points": 7.4,
        "ownership": 81.2,
        "price": 14.0,
        "fixture_difficulty": 2,
    },
    {
        "id": 2,
        "name": "Bukayo Saka",
        "team": "ARS",
        "position": "MID",
        "expected_points": 6.1,
        "ownership": 56.7,
        "price": 9.0,
        "fixture_difficulty": 2,
    },
    {
        "id": 3,
        "name": "Son Heung-min",
        "team": "TOT",
        "position": "MID",
        "expected_points": 6.5,
        "ownership": 40.2,
        "price": 10.0,
        "fixture_difficulty": 3,
    },
    {
        "id": 4,
        "name": "Mohamed Salah",
        "team": "LIV",
        "position": "MID",
        "expected_points": 6.9,
        "ownership": 45.1,
        "price": 13.0,
        "fixture_difficulty": 2,
    },
    {
        "id": 5,
        "name": "Josko Gvardiol",
        "team": "MCI",
        "position": "DEF",
        "expected_points": 4.3,
        "ownership": 8.4,
        "price": 5.2,
        "fixture_difficulty": 2,
    },
]

MOCK_FIXTURES = [
    {"team": "MCI", "opponent": "FUL", "difficulty": 2, "kickoff": date(2024, 9, 14)},
    {"team": "ARS", "opponent": "BHA", "difficulty": 3, "kickoff": date(2024, 9, 14)},
    {"team": "TOT", "opponent": "NEW", "difficulty": 3, "kickoff": date(2024, 9, 15)},
    {"team": "LIV", "opponent": "CHE", "difficulty": 4, "kickoff": date(2024, 9, 15)},
]

MOCK_TEAM = {
    "budget": 1.5,
    "free_transfers": 1,
    "players": [player for player in MOCK_PLAYERS if player["id"] in {1, 2, 3, 5}],
}
