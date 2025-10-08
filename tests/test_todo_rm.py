# test/test_todo_rm.py
# Purpose: test that we can remove a todo by id safely.

from toolbox import todo
from toolbox.storage import STATE_PATH

def test_todo_remove_by_id(tmp_path, monkeypatch):
    # Use a temp state.json file so tests dont' interfere with real data
    monkeypatch.setattr("toolbox.storage.STATE_PATH", tmp_path / "state.json")

    # Add two todos
    a = todo.add("alpha")
    b = todo.add("beta")

    # Remove the first one
    assert todo.remove(1) is True

    # Only the second should remain
    remaining = todo.list_open()
    assert len(remaining) == 1
    assert remaining[0]["id"] == 2

    # Removing something nonexistent should return False
    assert todo.remove(999) is False
