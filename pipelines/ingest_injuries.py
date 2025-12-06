"""Mock ingestion of injury news feeds."""

from __future__ import annotations

from utils.logger import get_logger

LOGGER = get_logger(__name__)


def run() -> None:
    LOGGER.info("Checking injury updates ... (mocked)")
