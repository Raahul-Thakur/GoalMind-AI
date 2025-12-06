"""Mock ingestion of Understat shot data."""

from __future__ import annotations

from utils.logger import get_logger

LOGGER = get_logger(__name__)


def run() -> None:
    LOGGER.info("Pulling Understat xG feed ... (mocked)")
