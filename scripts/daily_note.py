#!/usr/bin/env python3
from datetime import date
from pathlib import Path


def create_daily_note():
    today = date.today().isoformat()
    notes_dir = Path(__file__).resolve().parent.parent / "notes"
    notes_dir.mkdir(exist_ok=True)
    note_file = notes_dir / f"{today}.md"

    if note_file.exists():
        print(f"Note for {today} already exists: {note_file}")
    else:
        note_file.write_text(f"# Notes for {today}\n\n- ")
        print(f"Created new note: {note_file}")


if __name__ == "__main__":
    create_daily_note()
