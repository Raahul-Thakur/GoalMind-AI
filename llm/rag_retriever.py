"""RAG-style retrieval for football insights."""

from __future__ import annotations

from typing import Dict, List

from database import queries
from database.vectorstore import search
from utils.caching import timed_lru_cache


@timed_lru_cache(seconds=600)
def retrieve_context(question: str) -> List[Dict[str, str]]:
    """Return structured context snippets for a question."""

    fixtures = queries.get_fixtures()
    fixture_text = "; ".join(f"{fx['team']} vs {fx['opponent']} (FDR {fx['difficulty']})" for fx in fixtures)

    results = search(question)
    results.append({"namespace": "fixtures", "text": fixture_text, "score": 1.0})
    return results
