from toolbox import todo


def test_todo_add_and_done(tmp_path, monkeypatch):
    monkeypatch.setattr("toolbox.storage.STATE_PATH", tmp_path / "state.json")
    item = todo.add("task")
    assert item["id"] == 1 and item["text"] == "task"
    open_items = todo.list_open()
    assert len(open_items) == 1
    todo.mark_done(1)
    assert todo.list_open() == []
