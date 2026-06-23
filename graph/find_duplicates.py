#!/usr/bin/env python3
"""
find_duplicates.py — Deterministic duplicate-concept detector for the repo.

The filename (= ASCII transliteration of term_iast) is the unique key for a
concept node (CLAUDE.md §3). Two files are duplicates when they encode the SAME
concept under different keys. Real keys can never collide (the filesystem would
overwrite), so duplication hides as:

  [DEVANAGARI]  same term_devanagari across >1 file  — same Sanskrit word.
                Often a LEGITIMATE tradition-split (ahimsa / ahimsa-buddhist),
                but must carry a typed edge between the pair (§5). Review each.
  [IAST]        same term_iast front-matter value across >1 filename. Hard.
  [SPLIT]       keys folding together that differ ONLY by a tradition suffix —
                an EXPECTED typed split (paramanu / paramanu-vaisheshika).
                Reported for review (does a typed edge exist?), never fails.
  [TRANSLIT]    keys with DISTINCT base spellings that still fold to one form —
                transliteration twins (sunyata/shunyata, v/w, double letters,
                diacritic folding). Strong duplicate signal. Hard.
  [PHANTOM]     a `## Links` target with no file, but within edit-distance 1 of a
                real file — a typo that spawns a stray graph node. Hard.

Exit status: 0 if no IAST/TRANSLIT/PHANTOM hard-collisions; 1 otherwise.
DEVANAGARI and SPLIT hits are reported but never fail the run (valid splits).
Read-only. Run from anywhere: python graph/find_duplicates.py
"""

import re
import sys
import unicodedata
from pathlib import Path
from collections import defaultdict

# Windows consoles default to cp1252 and choke on Devanagari; force UTF-8.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

REPO_ROOT = Path(__file__).parent.parent
CONCEPTS_DIR = REPO_ROOT / "concepts"

FM_DEVANAGARI = re.compile(r"^term_devanagari:\s*(.+?)\s*$", re.MULTILINE)
FM_IAST = re.compile(r"^term_iast:\s*(.+?)\s*$", re.MULTILINE)
LINKS_SECTION_RE = re.compile(r"## Links\s*\n(.*?)(?:\n## |\Z)", re.DOTALL)
LINK_LINE_RE = re.compile(r"^\s*-\s*[\w-]+:\s*([\w-]+)", re.MULTILINE)

# Tradition disambiguation suffixes — stripped before transliteration-folding so
# that `paramanu` and `paramanu-vaisheshika` are NOT flagged as translit twins
# (they are a deliberate, typed split, caught by [DEVANAGARI] instead).
TRADITION_SUFFIXES = (
    "jain", "buddhist", "vedic", "vedanta", "advaita", "samkhya", "nyaya",
    "vaisheshika", "mimamsa", "yoga", "carvaka", "greek", "stoic", "epicurus",
)


def strip_tradition_suffix(key: str) -> str:
    """Drop a single trailing tradition suffix, keeping the raw base spelling."""
    s = key.lower()
    for suf in TRADITION_SUFFIXES:
        if s.endswith("-" + suf):
            return s[: -(len(suf) + 1)]
    return s


def normalise_translit(key: str) -> str:
    """Fold a filename key to a canonical form so transliteration variants of the
    same word collapse together. Heuristic — meant to over-report, not to decide."""
    s = strip_tradition_suffix(key)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("-", "").replace("_", "")
    s = s.replace("sh", "s").replace("ss", "s")  # ś/ṣ romanisation drift
    s = s.replace("v", "w")                         # v/w drift
    s = s.replace("ph", "f")
    s = re.sub(r"(.)\1+", r"\1", s)                 # collapse doubled letters (vowel-length + geminates)
    return s


def levenshtein(a: str, b: str) -> int:
    if a == b:
        return 0
    if abs(len(a) - len(b)) > 1:
        return 2  # we only care about <=1
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[-1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def main() -> int:
    files = sorted(CONCEPTS_DIR.glob("*.md"))
    keys = [f.stem for f in files]
    keyset = set(keys)

    deva = defaultdict(list)
    iast = defaultdict(list)
    fold = defaultdict(list)
    targets = set()

    for f in files:
        text = f.read_text(encoding="utf-8")
        for m in FM_DEVANAGARI.findall(text):
            mc = m.strip().lower()
            # skip empties and prose placeholders (no real script value)
            if mc and mc not in ("", "none", "n/a", "~", "-") and "(" not in mc:
                deva[m.strip()].append(f.stem)
        im = FM_IAST.search(text)
        iast[im.group(1) if im else f.stem].append(f.stem)
        fold[normalise_translit(f.stem)].append(f.stem)
        sec = LINKS_SECTION_RE.search(text)
        if sec:
            targets.update(LINK_LINE_RE.findall(sec.group(1)))

    hard = 0

    print(f"Scanned {len(files)} concept files.\n")

    print("== [DEVANAGARI] same term_devanagari across >1 file (review: must be typed-split) ==")
    hits = {k: v for k, v in deva.items() if len(v) > 1}
    if hits:
        for dv, fs in sorted(hits.items()):
            print(f"  {dv} : {', '.join(sorted(fs))}")
    else:
        print("  none")

    print("\n== [IAST] same term_iast front-matter across >1 filename (hard collision) ==")
    hits = {k: v for k, v in iast.items() if len(v) > 1}
    if hits:
        for k, fs in sorted(hits.items()):
            print(f"  {k} : {', '.join(sorted(fs))}")
            hard += 1
    else:
        print("  none")

    # A fold-group whose members share ONE raw base spelling differs only by a
    # tradition suffix — an EXPECTED typed split, not a collision. A group with
    # >1 distinct base is a real transliteration twin (hard).
    print("\n== [SPLIT] same word across traditions (expected — verify a typed edge exists) ==")
    split_hits, twin_hits = {}, {}
    for k, fs in fold.items():
        members = sorted(set(fs))
        if len(members) < 2:
            continue
        if len({strip_tradition_suffix(m) for m in members}) == 1:
            split_hits[k] = members
        else:
            twin_hits[k] = members
    if split_hits:
        for k, fs in sorted(split_hits.items()):
            print(f"  ~{k} : {', '.join(fs)}")
    else:
        print("  none")

    print("\n== [TRANSLIT] distinct base spellings folding to one form — transliteration twins (hard collision) ==")
    if twin_hits:
        for k, fs in sorted(twin_hits.items()):
            print(f"  ~{k} : {', '.join(fs)}")
            hard += 1
    else:
        print("  none")

    print("\n== [PHANTOM] link targets within edit-distance 1 of a real file (typo nodes) ==")
    phantoms = [t for t in sorted(targets) if t not in keyset]
    found = False
    for t in phantoms:
        near = [k for k in keys if levenshtein(t, k) == 1]
        if near:
            print(f"  -> {t}  (no file; close to: {', '.join(near)})")
            found = True
            hard += 1
    if not found:
        print("  none")

    # MANIFEST.tsv is the dedup gate's fast accelerator; if it has drifted from
    # the filesystem the gate's status/links lookups go stale (existence is still
    # checked against concepts/ directly, so this never causes a missed dup — but
    # a forgotten `build_graph.py` should still be loud). Warn; don't fail.
    print("\n== [MANIFEST] freshness vs concepts/ (warn — run build_graph.py to refresh) ==")
    manifest = REPO_ROOT / "MANIFEST.tsv"
    if not manifest.exists():
        print("  MANIFEST.tsv MISSING — run: python graph/build_graph.py")
    else:
        man_keys = set()
        for line in manifest.read_text(encoding="utf-8").splitlines():
            if line and not line.startswith("#"):
                man_keys.add(line.split("\t", 1)[0])
        missing = sorted(keyset - man_keys)   # on disk, absent from manifest
        stale = sorted(man_keys - keyset)     # in manifest, file deleted
        if not missing and not stale:
            print("  in sync")
        else:
            if missing:
                print(f"  NOT YET IN MANIFEST ({len(missing)}): {', '.join(missing)}")
            if stale:
                print(f"  STALE ROWS (file gone) ({len(stale)}): {', '.join(stale)}")
            print("  -> run: python graph/build_graph.py")

    print(f"\nHard-collision groups (IAST/TRANSLIT/PHANTOM): {hard}")
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
