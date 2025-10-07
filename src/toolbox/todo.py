from __future__ import annotations
from datetime import datetime, UTC
from .storage import load_state, save_state


def add(text: str) -> dict:
    s = load_state()
    next_id = max([t["id"] for t in s["todos"]] or [0]) + 1
    item = {
        "id": next_id,
        "text": text,
        "done": False,
        "created_at": datetime.now(UTC).isoformat(),
    }
    s["todos"].append(item)
    save_state(s)
    return item


def list_open() -> list[dict]:
    return [t for t in load_state()["todos"] if not t["done"]]


def mark_done(item_id: int) -> dict | None:
    s = load_state()
    for t in s["todos"]:
        if t["id"] == item_id:
            t["done"] = True
            save_state(s)
            return t
    return None
