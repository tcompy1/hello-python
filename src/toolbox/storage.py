from __future__ import annotations
from pathlib import Path
import json

STATE_PATH = Path.home() / ".toolbox" / "state.json"


def _ensure_dir() -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)


def load_state() -> dict:
    _ensure_dir()
    if not STATE_PATH.exists():
        return {"todos": [], "timer": {"start": None}}
    return json.loads(STATE_PATH.read_text())


def save_state(state: dict) -> None:
    _ensure_dir()
    STATE_PATH.write_text(json.dumps(state, indent=2))
