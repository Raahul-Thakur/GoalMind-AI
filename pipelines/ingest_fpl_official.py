"""Mock ingestion of the official FPL API."""

from __future__ import annotations

from utils.logger import get_logger

LOGGER = get_logger(__name__)


def run() -> None:
    LOGGER.info("Fetching official FPL bootstrap-static ... (mocked)")
