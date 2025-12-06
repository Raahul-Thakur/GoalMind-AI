"""Combine ingestion outputs into model-ready features."""

from __future__ import annotations

from ml.feature_builder import build_player_features
from utils.logger import get_logger

LOGGER = get_logger(__name__)


def build_features() -> None:
    features = build_player_features()
    LOGGER.info("Built %d feature rows", len(features))
