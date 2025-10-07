from __future__ import annotations
from pathlib import Path


def plan_rename(pattern: str, to: str, cwd: Path) -> list[tuple[Path, Path]]:
    pairs: list[tuple[Path, Path]] = []
    for p in cwd.iterdir():
        if p.is_file() and pattern in p.name:
            new = p.with_name(p.name.replace(pattern, to))
            if new.exists() and new != p:
                continue  # skip conflicting rename
            pairs.append((p, new))
    return pairs


def apply_rename(pairs: list[tuple[Path, Path]]) -> int:
    for src, dst in pairs:
        if src != dst:
            src.rename(dst)
    return len(pairs)
