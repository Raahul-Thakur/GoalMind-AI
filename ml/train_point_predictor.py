"""Placeholder training loop for a point prediction model."""

from __future__ import annotations

import random
from typing import Dict, List

from ml.feature_builder import build_player_features
from utils.logger import get_logger

LOGGER = get_logger(__name__)


def train(features: List[Dict[str, object]] | None = None) -> Dict[str, float]:
    """Return a mapping of player id to a mock predicted score."""

    dataset = build_player_features(features)
    model = {row["id"]: round(row["adjusted_xpts"] + random.uniform(-0.5, 0.5), 2) for row in dataset}
    LOGGER.info("Trained lightweight predictor on %d players", len(dataset))
    return model
