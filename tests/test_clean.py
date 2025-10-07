from pathlib import Path
from toolbox.clean import plan_rename


def test_plan_rename(tmp_path: Path):
    (tmp_path / "a b.txt").write_text("x")
    (tmp_path / "c.txt").write_text("y")
    pairs = plan_rename(" ", "_", tmp_path)
    names = [(s.name, d.name) for s, d in pairs]
    assert ("a b.txt", "a_b.txt") in names
