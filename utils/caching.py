"""Lightweight caching helpers for repeated computations."""

from __future__ import annotations

import functools
import time
from typing import Any, Callable, Dict, Tuple


def timed_lru_cache(seconds: int = 300, maxsize: int = 128) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Cache a function result for ``seconds``.

    This is intentionally simple and does not rely on external services so that
    the MVP can be deployed quickly.
    """

    def wrapper(fn: Callable[..., Any]) -> Callable[..., Any]:
        cache: Dict[Tuple[Any, ...], Tuple[float, Any]] = {}

        @functools.wraps(fn)
        def inner(*args: Any, **kwargs: Any) -> Any:
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()
            if key in cache:
                timestamp, value = cache[key]
                if now - timestamp < seconds:
                    return value
            value = fn(*args, **kwargs)
            if len(cache) >= maxsize:
                cache.pop(next(iter(cache)))
            cache[key] = (now, value)
            return value

        return inner

    return wrapper
