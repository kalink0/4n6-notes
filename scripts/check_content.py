"""Content checks for docs/. Exits non-zero on any error.

Checks:
- no references to the private Nextcloud host or its link formats
- every page has a title and a valid status (draft, complete, reviewed); index.md may omit it
- complete and reviewed pages have a completion date (`completed: YYYY-MM-DD`) and, on German
  pages, authors; reviewed pages also have a review date (`reviewed: YYYY-MM-DD`) and reviewers.
  Dates are valid, not in the future and only set with the matching status
- authors (`authors: [...]`, German pages only) and reviewers (`reviewers: [...]`) are GitHub
  handles, optionally with the full name: `kalink0 (Max Mustermann)`; nobody reviews a page they
  wrote
- every translated page has a German original and valid translation metadata
- topics (`topics: [key, ...]`) only on German artifact pages and only with keys from
  extra.topics in mkdocs.base.yml; every topic has a label for every language
- gap lists (gaps/<section>.yml) belong to an existing section and have a name for every entry;
  if a list uses topics, every entry has one known topic
Reports (without failing) translations whose German original changed, overview pages (index.md,
except the start page) with more than the title,
artifact pages without topics, topics no page uses and gap entries that already have a page or heading in their section.

Usage:
    python scripts/check_content.py              run all checks
    python scripts/check_content.py --hash FILE  print translation_of value for a German page
"""

import re
import sys
from datetime import date, datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
GAPS = ROOT / "gaps"
sys.path.insert(0, str(ROOT / "hooks"))

from mkdocs.utils.meta import get_data  # noqa: E402

from credits import parse_people  # noqa: E402
from i18n import source_hash  # noqa: E402

DOCS = ROOT / "docs"
SOURCE_LANG = "de"
STATUSES = {"draft", "complete", "reviewed"}
TRANSLATIONS = {"machine", "human"}
FORBIDDEN = [
    re.compile(r"REDACTED"),
    re.compile(r"REDACTED"),
    re.compile(r"/apps/collectives/"),
    re.compile(r"[?&]fileId="),
]


def check_gaps(errors: list[str], topics: dict) -> list[str]:
    """Validate gaps/*.yml; return entries that already have a page title or heading."""
    covered: list[str] = []
    for path in sorted(GAPS.rglob("*.yml")) if GAPS.is_dir() else []:
        rel = path.relative_to(ROOT).as_posix()
        section = DOCS / SOURCE_LANG / path.relative_to(GAPS).with_suffix("")
        if not (section / "index.md").is_file():
            errors.append(f"{rel}: no section index at {(section / 'index.md').relative_to(DOCS).as_posix()}")
            continue
        entries = yaml.safe_load(path.read_text(encoding="utf-8")) or []
        if not isinstance(entries, list):
            errors.append(f"{rel}: must be a list of entries")
            continue
        uses_topics = any(isinstance(e, dict) and e.get("topic") for e in entries)
        existing: set[str] = set()
        for page in section.rglob("*.md"):
            text = page.read_text(encoding="utf-8")
            _, meta = get_data(text)
            existing.add(str(meta.get("title", "")).strip().casefold())
            existing.update(m.strip().casefold() for m in re.findall(r"^##\s+(.+)$", text, re.M))
        for i, entry in enumerate(entries, 1):
            name = entry.get("name") if isinstance(entry, dict) else None
            if isinstance(name, dict):
                name = name.get(SOURCE_LANG)
            if not str(name or "").strip():
                errors.append(f"{rel}: entry {i} has no (German) name")
            elif str(name).strip().casefold() in existing:
                covered.append(f"{rel}: {name}")
            topic = entry.get("topic") if isinstance(entry, dict) else None
            if topic is not None and topic not in topics:
                errors.append(f"{rel}: entry {i} has unknown topic {topic!r} (see extra.topics in mkdocs.base.yml)")
            elif topic is None and uses_topics:
                errors.append(f"{rel}: entry {i} has no topic, but other entries in the list have one")
    return covered


def main() -> int:
    if len(sys.argv) == 3 and sys.argv[1] == "--hash":
        print(source_hash(Path(sys.argv[2]).read_text(encoding="utf-8")))
        return 0

    errors: list[str] = []
    outdated: list[str] = []
    without_topics: list[str] = []
    busy_index: list[str] = []
    extra = yaml.safe_load((ROOT / "mkdocs.base.yml").read_text(encoding="utf-8"))["extra"]
    topics = extra.get("topics") or {}
    languages = [alt["lang"] for alt in extra["alternate"]]
    for key, labels in topics.items():
        missing = [lang for lang in languages if not str((labels or {}).get(lang, "")).strip()]
        if missing:
            errors.append(f"mkdocs.base.yml: topic {key!r} has no label for {', '.join(missing)}")
    used_topics: set[str] = set()
    source_dir = DOCS / SOURCE_LANG
    for lang_dir in sorted(p for p in DOCS.iterdir() if p.is_dir()):
        for page in sorted(lang_dir.rglob("*.md")):
            rel = page.relative_to(DOCS).as_posix()
            text = page.read_text(encoding="utf-8")
            for pattern in FORBIDDEN:
                for m in pattern.finditer(text):
                    line = text.count("\n", 0, m.start()) + 1
                    errors.append(f"{rel}:{line}: private Nextcloud reference '{m.group(0)}'")
            body, meta = get_data(text)
            if page.name == "index.md" and page.parent != lang_dir:
                # Only the title; the list of pages is generated.
                rest = re.sub(r"^# .*$", "", body, count=1, flags=re.M)
                if rest.strip():
                    busy_index.append(rel)
            if not str(meta.get("title", "")).strip():
                errors.append(f"{rel}: missing title")
            # Overview pages (index.md) may omit the status; the section listing is generated.
            if not (page.name == "index.md" and "status" not in meta) and meta.get("status") not in STATUSES:
                errors.append(f"{rel}: status must be one of {sorted(STATUSES)}, got {meta.get('status')!r}")
            status = meta.get("status")
            for field, statuses in (("completed", {"complete", "reviewed"}), ("reviewed", {"reviewed"})):
                value = meta.get(field)
                if status in statuses:
                    if value is None:
                        errors.append(f"{rel}: status is {status} but {field} (date) is missing")
                    elif not isinstance(value, date) or isinstance(value, datetime):
                        errors.append(f"{rel}: {field} must be a date YYYY-MM-DD, got {value!r}")
                    elif value > date.today():
                        errors.append(f"{rel}: {field} date {value} is in the future")
                elif value is not None:
                    errors.append(f"{rel}: {field} date set but status is {status!r}")
            reviewers = parse_people(meta.get("reviewers"))
            if reviewers is None:
                errors.append(f"{rel}: reviewers must be GitHub handles, optionally 'handle (Full Name)'")
            elif reviewers and meta.get("status") != "reviewed":
                errors.append(f"{rel}: reviewers set but status is {meta.get('status')!r}")
            elif not reviewers and meta.get("status") == "reviewed":
                errors.append(f"{rel}: status is reviewed but reviewers are missing")
            if lang_dir.name == SOURCE_LANG:
                authors = parse_people(meta.get("authors"))
                if authors is None:
                    errors.append(f"{rel}: authors must be GitHub handles, optionally 'handle (Full Name)'")
                elif not authors and status in {"complete", "reviewed"}:
                    errors.append(f"{rel}: status is {status} but authors are missing")
            else:
                if meta.get("authors") is not None:
                    errors.append(f"{rel}: authors belong on the German page only")
                original = source_dir / page.relative_to(lang_dir)
                _, original_meta = get_data(original.read_text(encoding="utf-8")) if original.is_file() else ("", {})
                authors = parse_people(original_meta.get("authors"))
            own = {p["handle"].casefold() for p in authors or []} & {p["handle"].casefold() for p in reviewers or []}
            if own:
                errors.append(f"{rel}: reviewed by its own author(s): {', '.join(sorted(own))}")
            page_topics = meta.get("topics")
            is_artifact = page.relative_to(lang_dir).parts[0] == "artifacts" and page.name != "index.md"
            if lang_dir.name != SOURCE_LANG:
                if page_topics is not None:
                    errors.append(f"{rel}: topics belong on the German page only")
            elif page_topics is not None and not is_artifact:
                errors.append(f"{rel}: topics are only for artifact pages")
            elif page_topics is not None and not isinstance(page_topics, list):
                errors.append(f"{rel}: topics must be a list of keys, got {page_topics!r}")
            elif is_artifact:
                for key in page_topics or []:
                    if key in topics:
                        used_topics.add(key)
                    else:
                        errors.append(f"{rel}: unknown topic {key!r} (see extra.topics in mkdocs.base.yml)")
                if not page_topics:
                    without_topics.append(rel)
            if lang_dir.name == SOURCE_LANG:
                continue
            original = source_dir / page.relative_to(lang_dir)
            if not original.is_file():
                errors.append(f"{rel}: no German original at {original.relative_to(DOCS).as_posix()}")
                continue
            if meta.get("translation") not in TRANSLATIONS:
                errors.append(f"{rel}: translation must be one of {sorted(TRANSLATIONS)}")
            if not re.fullmatch(r"sha256:[0-9a-f]{12}", str(meta.get("translation_of", ""))):
                errors.append(f"{rel}: translation_of missing or malformed")
            elif meta["translation_of"] != source_hash(original.read_text(encoding="utf-8")):
                outdated.append(rel)

    for rel in outdated:
        print(f"outdated translation (German original changed): {rel}")
    for rel in busy_index:
        print(f"overview page with more than the title: {rel}")
    for rel in without_topics:
        print(f"artifact page without topics: {rel}")
    covered_gaps = check_gaps(errors, topics)
    for gap in covered_gaps:
        print(f"gap entry already covered, remove it: {gap}")
    unused_topics = sorted(set(topics) - used_topics)
    for key in unused_topics:
        print(f"topic not used by any page: {key}")
    for err in errors:
        print(f"ERROR {err}")
    print(
        f"{len(errors)} error(s), {len(outdated)} outdated translation(s), "
        f"{len(busy_index)} overview page(s) with extra content, "
        f"{len(without_topics)} artifact page(s) without topics, "
        f"{len(unused_topics)} unused topic(s), {len(covered_gaps)} covered gap entr(y/ies)"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
