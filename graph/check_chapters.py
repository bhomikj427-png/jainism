#!/usr/bin/env python3
"""
check_chapters.py — Deterministic checker for the teaching layer (read-only).

Every other structural claim in this repo is proven by a script. The one claim
that was not is "chapter coverage N/N", asserted by hand in progress.md and in
commit messages. It could not be verified because `chapters/INDEX.md` keys its
concept column by *display term* (diacritic IAST: `kaṣāya`, `viṣṇu`) while the
canonical key of a concept is its **filename** (CLAUDE.md §3). The two sets do
not join, so nobody could tell whether coverage was complete. It was not.

This script does the join and reports what breaks:

  [UNRESOLVED]  a concept→chapter row naming something with no concept file
  [UNCOVERED]   a written concept with no row in the concept→chapter map
  [DUPLICATE]   a concept with more than one row — the map's own header says
                "primary-covered in exactly one chapter". Rows that disagree
                about the *primary* chapter are flagged as CONFLICT.
  [MISSINGFILE] a chapter file named in the chapter table that is not on disk
  [KNOWN-GAP]   a real, already-recorded gap (see KNOWN_UNCOVERED / KNOWN_UNRESOLVED)
                - printed every run so it stays visible, but does not fail the run

Exit status: 0 if all clean, 1 otherwise. Read-only — never edits.
Run: python graph/check_chapters.py
"""

import re
import sys
import unicodedata
from pathlib import Path
from collections import defaultdict

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

REPO_ROOT = Path(__file__).parent.parent
CONCEPTS_DIR = REPO_ROOT / "concepts"
CHAPTERS_DIR = REPO_ROOT / "chapters"
INDEX_PATH = CHAPTERS_DIR / "INDEX.md"        # chapter list + roadmap
COVERAGE_PATH = CHAPTERS_DIR / "coverage.md"  # the concept -> chapter lookup table

# Display terms whose canonical filename key transliteration-folding cannot reach
# (the file is named for a *disambiguated* or differently-chosen key). Reviewed by
# hand once, recorded here so the join stays exact instead of heuristic. Add to
# this table only after checking the concept file actually exists.
ALIASES = {
    "manaḥparyāya-jñāna": "manah-paryaya-jnana",
    "ṣaḍāvaśyaka": "shad-avashyaka",
    "ākāśa": "akasha-dravya",
    "kāla": "kala-dravya",
    "loka": "loka-jain",
    "ṇamokāra-mantra": "namokara",
    "tathāgatagarbha": "tathagata-garbha",
    "pañcamahābhūta": "pancha-mahabhuta",
    "avatāra": "avatara-vedanta",
    "liṅga": "lingam",
    "prasaṅga": "prasanga-nagarjuna",
    "pramāṇasamuccaya": "pramana-samuccaya",
    "apratiṣṭhita-nirvāṇa": "nirvana-mahayana",
    "kārmaṇa-vargaṇā": "karma-vargana",
    "nyāyabindu (Dharmottaraṭīkā)": "dharmottara-nyayabindu",
    "saṃgraha-naya": "sangraha-naya",
    "samyagdarśana": "samyak-darshana",
    "sarvajñatva (omniscience-vedānta)": "omniscience-vedanta",
}


# Gaps that are REAL and already recorded in progress.md, not defects to re-discover
# on every run. A permanently-red check gets ignored, so each known gap is listed here
# with its reason and reported under [KNOWN-GAP] instead of failing the run. Anything
# NOT in these tables still fails. Remove an entry the moment it is actually closed.
KNOWN_UNCOVERED = {
    "dhamma": "no chapter teaches it or links to it; needs chapter prose (progress.md)",
}
KNOWN_UNRESOLVED = {
    "prasthānatrayī": "taught in Ch 11 and Ch 19 but no concept file exists yet; "
                      "a candidate node, not a bad row (progress.md)",
}


def fold(s: str) -> str:
    """Fold a display term or filename key to a comparison form. Deterministic
    transliteration folding only (the same idea as find_duplicates.normalise_translit)
    — NOT semantic similarity. Tradition suffixes are deliberately KEPT, so
    `mokṣa` and `mokṣa-advaita` never collapse onto each other."""
    s = re.sub(r"\(.*?\)", "", s).strip()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9-]", "", s)
    s = s.replace("ch", "c").replace("sh", "s").replace("ss", "s")
    s = s.replace("v", "w").replace("ph", "f").replace("ri", "r")
    return re.sub(r"(.)\1+", r"\1", s)


def parse_index():
    """Return (chapter_rows, concept_rows) from chapters/INDEX.md.

    chapter_rows: [(lineno, chapter_label, file_cell)]      — the 4-column table
    concept_rows: [(lineno, display_term, primary, xrefs)]  — the 3-column map
    """
    chapter_rows, concept_rows = [], []
    # chapter rows (4 cols) live in INDEX.md; concept rows (3 cols) in coverage.md.
    # Both are scanned; the column count decides which table a row belongs to.
    for path in (INDEX_PATH, COVERAGE_PATH):
      for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.startswith("|"):
            continue
        c = [x.strip() for x in line.split("|")]
        head = c[1] if len(c) > 1 else ""
        if not head or set(head) <= set("-: ") or head.lower() in ("chapter", "concept"):
            continue
        if len(c) == 6:
            chapter_rows.append((i, head, c[2]))
        elif len(c) == 5:
            concept_rows.append((i, head, c[2], c[3]))
    return chapter_rows, concept_rows


def main() -> int:
    if not INDEX_PATH.exists():
        print(f"MISSING: {INDEX_PATH}")
        return 1

    keys = [p.stem for p in sorted(CONCEPTS_DIR.glob("*.md"))]
    by_fold = defaultdict(list)
    for k in keys:
        by_fold[fold(k)].append(k)
    keyset = set(keys)

    chapter_rows, concept_rows = parse_index()
    print(f"concept files {len(keys)} | chapter rows {len(chapter_rows)} "
          f"| concept->chapter rows {len(concept_rows)}")

    resolved, unresolved = {}, []
    for lineno, display, primary, _x in concept_rows:
        key = ALIASES.get(display)
        if key is None:
            cands = by_fold.get(fold(display), [])
            key = cands[0] if len(cands) == 1 else None
        if key is None or key not in keyset:
            unresolved.append((lineno, display))
        else:
            resolved.setdefault(key, []).append((lineno, primary))

    uncovered_all = [k for k in keys if k not in resolved]
    uncovered = [k for k in uncovered_all if k not in KNOWN_UNCOVERED]
    known_unc = [k for k in uncovered_all if k in KNOWN_UNCOVERED]
    known_unres = [r for r in unresolved if r[1] in KNOWN_UNRESOLVED]
    unresolved = [r for r in unresolved if r[1] not in KNOWN_UNRESOLVED]
    dups = {k: v for k, v in resolved.items() if len(v) > 1}

    missing_files = []
    for lineno, label, cell in chapter_rows:
        m = re.search(r"\(([^)]+\.md)\)", cell)
        if m and not (CHAPTERS_DIR / m.group(1)).exists():
            missing_files.append((lineno, label, m.group(1)))

    print(f"\n== [UNRESOLVED] map rows naming no concept file ({len(unresolved)}) ==")
    for lineno, d in unresolved:
        print(f"   coverage.md:{lineno}  {d!r}")
    if not unresolved:
        print("   none")

    print(f"\n== [UNCOVERED] written concepts with no row ({len(uncovered)}) ==")
    for k in uncovered:
        print(f"   {k}")
    if not uncovered:
        print("   none")

    print(f"\n== [DUPLICATE] concepts with >1 row ({len(dups)}) ==")
    conflicts = 0
    for k, rows in sorted(dups.items()):
        prims = {p for _l, p in rows}
        tag = ""
        if len(prims) > 1:
            tag = f"   <<< CONFLICT: {sorted(prims)}"
            conflicts += 1
        print(f"   {k}: lines {[l for l, _p in rows]}{tag}")
    if not dups:
        print("   none")

    print(f"\n== [MISSINGFILE] chapter files named but absent ({len(missing_files)}) ==")
    for lineno, label, f in missing_files:
        print(f"   INDEX.md:{lineno}  {label} -> {f}")
    if not missing_files:
        print("   none")

    print(f"\n== [KNOWN-GAP] recorded in progress.md, not failing "
          f"({len(known_unc) + len(known_unres)}) ==")
    for k in known_unc:
        print(f"   uncovered concept {k!r}: {KNOWN_UNCOVERED[k]}")
    for lineno, d in known_unres:
        print(f"   coverage.md:{lineno} {d!r}: {KNOWN_UNRESOLVED[d]}")
    if not (known_unc or known_unres):
        print("   none")

    covered = len(keys) - len(uncovered_all)
    clean = not (unresolved or uncovered or dups or missing_files)
    print(f"\ncoverage: {covered}/{len(keys)} concepts have a chapter row"
          f"{'' if not conflicts else f'  ({conflicts} primary-chapter conflict(s))'}")
    print(f"=> {'CLEAN' if clean else 'DEFECTS PRESENT'}")
    return 0 if clean else 1


if __name__ == "__main__":
    sys.exit(main())
