from __future__ import annotations
import time
from .storage import load_state, save_state


def start() -> float | None:
    s = load_state()
    if s["timer"]["start"] is not None:
        return None
    s["timer"]["start"] = time.time()
    save_state(s)
    return s["timer"]["start"]


def status() -> float | None:
    s = load_state()
    ts = s["timer"]["start"]
    return None if ts is None else (time.time() - ts)


def stop() -> float | None:
    s = load_state()
    ts = s["timer"]["start"]
    if ts is None:
        return None
    elapsed = time.time() - ts
    s["timer"]["start"] = None
    save_state(s)
    return elapsed
