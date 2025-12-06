"""Lightweight local datastore helpers used by the MVP."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from utils.logger import get_logger

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
LOGGER = get_logger(__name__)


def load_json(filename: str, default: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Return JSON content from ``data/filename`` or ``default`` if missing."""

    path = DATA_DIR / filename
    if not path.exists():
        LOGGER.warning("Data file %s not found, using defaults", filename)
        return default
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)
