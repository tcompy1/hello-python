from toolbox import timer


def test_timer_start_stop(tmp_path, monkeypatch):
    monkeypatch.setattr("toolbox.storage.STATE_PATH", tmp_path / "state.json")
    assert timer.status() is None
    assert timer.start() is not None
    assert timer.status() >= 0
    e = timer.stop()
    assert e is not None and timer.status() is None
