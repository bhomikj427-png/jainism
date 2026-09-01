#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
check_staleness.py -- ADVISORY teaching-layer staleness detector (read-only).

WHAT IT ANSWERS
    "Which chapters teach a concept that has been edited since the chapter was
    last touched?"

WHY IT EXISTS
    check_chapters.py proves that every concept HAS a chapter row -- coverage.
    Nothing proved that the chapter still says what the concept says -- freshness.
    Chapters in this corpus are effectively write-once: they are drafted over a
    batch's new nodes and then never revisited, while the nodes underneath them
    keep being corrected by later batches. That drift was invisible to the gate.

    Concrete case (Batch 47): `patanjali.md` had its date corrected BY A CENTURY
    and gained a three-way conflation finding. Ch 15, which teaches it, was last
    touched 2026-07-10 and still carries the old account.

⚠ DELIBERATELY NOT WIRED INTO check_all.py, AND THAT IS A DESIGN DECISION.
    At the time of writing 14 of 34 chapters are stale by this test. Making it a
    gate would turn the repo red for every session and block unrelated work --
    the opposite of useful. It is advisory until the backlog is worked down.
    IF you drive the count to zero, wiring it in is then worth doing, because
    from that point it costs one chapter-edit per batch to stay green.

⚠ WHAT THIS TEST IS NOT
    It is a mtime-style heuristic on git history, not a semantic check. A chapter
    can be flagged because a covered concept had a typo fixed, and can be MISSED
    when a chapter is factually wrong but nothing underneath it changed. Treat a
    flag as "go look", never as "this chapter is wrong". The reverse -- a clean
    result -- is weak evidence of anything.

USAGE
    python graph/check_staleness.py          # table + summary
    python graph/check_staleness.py --quiet  # summary line only
Exit code is always 0. This never fails a build.
"""

import collections
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def last_commit_date(relpath):
    """Date of the last commit touching relpath, as YYYY-MM-DD, or '' if unknown."""
    try:
        out = subprocess.check_output(
            ["git", "log", "-1", "--format=%ad", "--date=short", "--", relpath],
            cwd=ROOT, stderr=subprocess.DEVNULL)
        return out.decode("utf-8", "replace").strip()
    except Exception:
        return ""


def chapter_files():
    """Map 'Ch NN' -> repo-relative chapter path, parsed from chapters/INDEX.md."""
    idx_path = os.path.join(ROOT, "chapters", "INDEX.md")
    if not os.path.exists(idx_path):
        return {}
    idx = io.open(idx_path, encoding="utf-8").read()
    out = {}
    for m in re.finditer(r"^\|\s*(\d\d)\s[^|]*\|\s*\[[^\]]*\]\(([^)]+)\)", idx, re.M):
        out["Ch " + m.group(1)] = os.path.join("chapters", m.group(2))
    return out


def coverage_rows():
    """[(concept_key, 'Ch NN')] from chapters/coverage.md."""
    cov_path = os.path.join(ROOT, "chapters", "coverage.md")
    if not os.path.exists(cov_path):
        return []
    cov = io.open(cov_path, encoding="utf-8").read()
    return re.findall(r"^\|\s*([^|]+?)\s*\|\s*(Ch \d\d)\s*\|", cov, re.M)


def main():
    quiet = "--quiet" in sys.argv
    chfile = chapter_files()
    by_chapter = collections.defaultdict(list)
    for key, ch in coverage_rows():
        rel = os.path.join("concepts", key + ".md")
        if os.path.exists(os.path.join(ROOT, rel)):
            by_chapter[ch].append(rel)

    stale, checked = [], 0
    for ch, files in by_chapter.items():
        rel_ch = chfile.get(ch)
        if not rel_ch or not os.path.exists(os.path.join(ROOT, rel_ch)):
            continue
        checked += 1
        ch_date = last_commit_date(rel_ch)
        if not ch_date:
            continue
        newest_date, newest_file = "", ""
        for f in files:
            d = last_commit_date(f)
            if d > newest_date:
                newest_date, newest_file = d, f
        if newest_date > ch_date:
            stale.append((ch_date, newest_date, ch, os.path.basename(rel_ch),
                          os.path.basename(newest_file), len(files)))
    stale.sort()

    if not quiet:
        print("== [STALE] chapters whose covered concepts were edited later "
              "(ADVISORY, never a gate) ==")
        if not stale:
            print("   none")
        else:
            print("   %-11s %-11s %-6s %-40s %s"
                  % ("CH TOUCHED", "NEWEST CPT", "CH", "chapter", "newest covered concept"))
            for cd, nd, ch, cf, nf, n in stale:
                print("   %-11s %-11s %-6s %-40s %s" % (cd, nd, ch, cf[:40], nf))
        print("")
    print("staleness: %d of %d chapters have a covered concept newer than the chapter"
          % (len(stale), checked))
    if stale and not quiet:
        print("=> ADVISORY ONLY. Go look at the oldest rows first; a flag means "
              "'check', not 'wrong'. See DRIFT.md item D3.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
