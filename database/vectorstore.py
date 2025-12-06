"""Tiny in-memory vector store for retrieval augmented generation mocks."""

from __future__ import annotations

import math
from typing import Dict, Iterable, List, Tuple

from utils.logger import get_logger

LOGGER = get_logger(__name__)

DOCUMENTS: List[Tuple[str, str]] = [
    ("captaincy", "Haaland leads expected goals; Saka has strong home form; Son on pens"),
    ("injuries", "No new injuries reported for core assets"),
    ("fixtures", "City face Fulham (2), Arsenal host Brighton (3)"),
]


def embed(text: str) -> List[float]:
    """Very small embedding using term frequency lengths (mock only)."""

    tokens = text.lower().split()
    unique = sorted(set(tokens))
    return [tokens.count(tok) for tok in unique]


def cosine(a: List[float], b: List[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    return dot / (norm_a * norm_b + 1e-9)


def search(query: str, limit: int = 3) -> List[Dict[str, str]]:
    """Return the best matching documents for a query."""

    query_vec = embed(query)
    scores = []
    for namespace, text in DOCUMENTS:
        score = cosine(query_vec, embed(text))
        scores.append({"namespace": namespace, "text": text, "score": score})
    sorted_scores = sorted(scores, key=lambda r: r["score"], reverse=True)
    LOGGER.info("Vector search for '%s' returned %d results", query, len(sorted_scores))
    return sorted_scores[:limit]
