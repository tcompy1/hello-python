# Changelog

All notable changes are tracked here.  
Format inspired by [Keep a Changelog](https://keepachangelog.com/) and semantic versioning.

---

## [0.4.0] – 2025-10-09
### Added
- Colorized CLI output using [rich] for todos, timer logs, and clean messages.
- Interactive confirmation for `todo rm` (with `--yes/-y` flag to skip prompt).
- `timer log --limit N` option to show only the last N sessions.
- Initial `README.md` with usage examples and install instructions.
- Prepared package for release with version bump to `0.4.0`.

---

## [0.3.0] – Week 3
### Added
- New `toolbox` package structure under `src/`.
- Core modules: `todo`, `timer`, `clean`, `storage`.
- CLI wiring for todos (add/list/done), timer (start/status/stop/log), and clean (rename).
- Daily note script (`scripts/daily_note.py`) that creates `notes/YYYY-MM-DD.md`.
- Expanded pytest coverage across modules.

---

## [0.2.0] – Week 2
### Added
- Expanded pytest tests for greet function.
- Introduced `pre-commit` hooks (black, ruff, pytest).
- CI-ready project layout with `src/` and `tests/`.
- First use of Ruff + Black for lint and format enforcement.

---

## [0.1.0] – Week 1
### Added
- Initial project skeleton (`hello-python`).
- Basic `hello.main.greet()` function.
- First test (`test_greet.py`) with pytest.
- Virtual environment setup, Git initialized.

---

[rich]: https://github.com/Textualize/rich
