from __future__ import annotations
import argparse
import sys
from pathlib import Path
from . import __version__ as VERSION
from . import todo, timer, clean


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    p = argparse.ArgumentParser(prog="toolbox", description="Everyday CLI utilities")
    p.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    sp = p.add_subparsers(dest="cmd", required=True)

    # todo
    pt = sp.add_parser("todo", help="Manage todos")
    st = pt.add_subparsers(dest="action", required=True)
    pa = st.add_parser("add", help="Add a todo")
    pa.add_argument("text")
    st.add_parser("list", help="List open todos")
    pd = st.add_parser("done", help="Mark done")
    pd.add_argument("id", type=int)

    # timer
    pti = sp.add_parser("timer", help="Simple timer")
    sti = pti.add_subparsers(dest="action", required=True)
    sti.add_parser("start")
    sti.add_parser("status")
    sti.add_parser("stop")

    # clean
    pc = sp.add_parser("clean", help="Cleanup utilities")
    sc = pc.add_subparsers(dest="action", required=True)
    pr = sc.add_parser("rename", help="Rename files by pattern")
    pr.add_argument("--pattern", required=True)
    pr.add_argument("--to", required=True)
    pr.add_argument("--apply", action="store_true", help="Actually perform renames")

    args = p.parse_args(argv)

    if args.cmd == "todo":
        if args.action == "add":
            item = todo.add(args.text)
            print(f"[{item['id']}] {item['text']}")
            return 0
        if args.action == "list":
            for t in todo.list_open():
                print(f"[{t['id']}] {t['text']}")
            return 0
        # done
        result = todo.mark_done(args.id)
        if result:
            print("OK")
            return 0
        print("Not found")
        return 1

    if args.cmd == "timer":
        if args.action == "start":
            started = timer.start()
            print("Timer already running" if started is None else "Started")
            return 0
        if args.action == "status":
            s = timer.status()
            print("Not running" if s is None else f"Elapsed: {int(s)}s")
            return 0
        # stop
        e = timer.stop()
        print("Not running" if e is None else f"Stopped at {int(e)}s")
        return 0

    if args.cmd == "clean" and args.action == "rename":
        pairs = clean.plan_rename(args.pattern, args.to, Path.cwd())
        for src, dst in pairs:
            print(f"{src.name} -> {dst.name}")
        if args.apply:
            n = clean.apply_rename(pairs)
            print(f"Renamed {n} file(s)")
        else:
            print("Dry run. Use --apply to perform.")
        return 0

    # should not reach here
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
