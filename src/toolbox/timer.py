from __future__ import annotations
import time
from .storage import load_state, save_state
from datetime import datetime, UTC

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

    s["timer"].setdefault("log", [])
    s["timer"]["log"].append({
        "ended_at": datetime.now(UTC).isoformat(),
        "seconds": int(elapsed),
    })

    save_state(s)
    return elapsed

def get_log() -> list[dict]:
    """
    Return the lsit of recorded timer sessions.
    Each entry is a dict with keys:
      - 'ended_at' : ISO 8601 UTC timestamp string
      - 'seconds' : int duration in seconds
    """

    s = load_state()   # read current state from disk
    return s["timer"].get("log", []) # default to [] if missing
