"""Entrypoint for a nightly maintenance run."""

from __future__ import annotations

from pipelines import ingest_fbref, ingest_fpl_official, ingest_injuries, ingest_understat
from pipelines.feature_pipeline import build_features
from utils.logger import get_logger

LOGGER = get_logger(__name__)


def run() -> None:
    """Run ingestion and feature preparation steps."""

    LOGGER.info("Starting nightly cron")
    ingest_fpl_official.run()
    ingest_understat.run()
    ingest_fbref.run()
    ingest_injuries.run()
    build_features()
    LOGGER.info("Nightly cron finished")


if __name__ == "__main__":
    run()
