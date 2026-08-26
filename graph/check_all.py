#!/usr/bin/env python3
"""
check_all.py — the single gate for CLAUDE.md §8 (pre-commit) and §9 (end-of-batch).

The repo has three deterministic checks and they had to be remembered and run
one at a time, so any of them could be silently skipped. This runs all three, in
dependency order, and exits non-zero if ANY of them fails:

  1. build_graph.py      regenerates graph.*/index.md/MANIFEST.tsv, then runs the
                         structural + conformance audits and the size budgets
  2. find_duplicates.py  duplicate-concept detection (IAST/TRANSLIT/PHANTOM)
  3. check_chapters.py   concept→chapter coverage

Every check still runs even if an earlier one fails, so one command shows you
the whole picture instead of only the first problem.

    python graph/check_all.py          # full gate (regenerates artifacts)
    python graph/check_all.py -q       # summary only; per-check output on failure

Exit status: 0 only if all three pass.
"""

import subprocess
import sys
from pathlib import Path

GRAPH_DIR = Path(__file__).parent
CHECKS = [
    ("build_graph", "build_graph.py", "graph, audits, size budgets"),
    ("duplicates", "find_duplicates.py", "duplicate concepts"),
    ("chapters", "check_chapters.py", "chapter coverage"),
]


def main() -> int:
    quiet = "-q" in sys.argv or "--quiet" in sys.argv
    results = []
    for name, script, blurb in CHECKS:
        proc = subprocess.run(
            [sys.executable, str(GRAPH_DIR / script)],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        ok = proc.returncode == 0
        results.append((name, ok, blurb))
        if not quiet or not ok:
            print(f"{'=' * 12} {script} {'=' * 12}")
            print((proc.stdout or "").rstrip())
            if proc.stderr.strip():
                print((proc.stderr or "").rstrip(), file=sys.stderr)
            print()

    width = max(len(n) for n, _o, _b in results)
    print("=" * 46)
    for name, ok, blurb in results:
        print(f"  {'PASS' if ok else 'FAIL'}  {name:<{width}}  {blurb}")
    failed = [n for n, ok, _b in results if not ok]
    print("=" * 46)
    print("ALL CHECKS PASS" if not failed else f"FAILED: {', '.join(failed)}")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
