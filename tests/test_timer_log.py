# tests/test_timer_log.py
# Goal: stopping the timer should append a simple session record,
# and we should be able to read that log back.

from toolbox import timer
from toolbox.storage import STATE_PATH


def test_timer_stop_appends_log(tmp_path, monkeypatch):
    #Router state to a temp file so we don't touch ~/.toolbox/state.json
    monkeypatch.setattr("toolbox.storage.STATE_PATH", tmp_path / "state.json")

    #Initially , no timer is running
    assert timer.status() is None

    # Start a timer; we only assert it's running, not exact time
    assert timer.start() is not None

    # Stop the timer; this should finalize the session
    elapsed = timer.stop()
    assert elapsed is not None # sanity: something was measured

    # Read the session log (we'll implement timer.get_log soon)
    log = timer.get_log()
    # We expect exactly one entry
    assert len(log) == 1
    # Each entry should have a durtation and an end timestamp
    assert "seconds" in log[0]
    assert "ended_at" in log[0]
    # 'seconds' should be numeric (exact value will vary)
    assert isinstance(log[0]["seconds"], (int, float))
