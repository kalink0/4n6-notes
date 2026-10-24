"""Content checks for docs/. Exits non-zero on any error.

Checks:
- every page has a title and a valid status (draft, complete, reviewed); index.md may omit it
- complete and reviewed pages have a completion date (`completed: YYYY-MM-DD`) and authors;
  reviewed pages also have a review date (`reviewed: YYYY-MM-DD`) and reviewers.
  Dates are valid and only set with the matching status
- authors (`authors: [...]`) and reviewers (`reviewers: [...]`) of each language version are
  GitHub handles, optionally with the full name: `some-handle (Full Name)`; nobody reviews a
  version they wrote
- every folder under docs/ is a language of extra.alternate; a version that says it is a
  translation (translation, translation_of: <lang>:<hash>) names an existing version
- topics (`topics: [key, ...]`) only on artifact pages and only with keys from
  extra.topics in mkdocs.base.yml; every topic has a label for every language
- gap lists (gaps/<section>.yml) belong to an existing section and have a name for every entry;
  if a list uses topics, every entry has one known topic
Reports (without failing) translations whose source version changed, language versions with
differing topics, overview pages (index.md, except the start page) with more than the title,
artifact pages without topics, topics no page uses and gap entries that already have a page or
heading in their section.

Usage:
    python scripts/check_content.py              run all checks
    python scripts/check_content.py --hash FILE  print the translation_of value for a version
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
from i18n import TRANSLATION_OF, source_hash  # noqa: E402

DOCS = ROOT / "docs"
STATUSES = {"draft", "complete", "reviewed"}
TRANSLATIONS = {"machine", "human"}


def check_gaps(errors: list[str], topics: dict, languages: list[str]) -> list[str]:
    """Validate gaps/*.yml; return entries that already have a page title or heading."""
    covered: list[str] = []
    for path in sorted(GAPS.rglob("*.yml")) if GAPS.is_dir() else []:
        rel = path.relative_to(ROOT).as_posix()
        section = path.relative_to(GAPS).with_suffix("").as_posix()
        dirs = [DOCS / lang / section for lang in languages if (DOCS / lang / section / "index.md").is_file()]
        if not dirs:
            errors.append(f"{rel}: no section index at docs/<lang>/{section}/index.md")
            continue
        entries = yaml.safe_load(path.read_text(encoding="utf-8")) or []
        if not isinstance(entries, list):
            errors.append(f"{rel}: must be a list of entries")
            continue
        uses_topics = any(isinstance(e, dict) and e.get("topic") for e in entries)
        existing: set[str] = set()
        for page in (p for d in dirs for p in d.rglob("*.md")):
            text = page.read_text(encoding="utf-8")
            _, meta = get_data(text)
            existing.add(str(meta.get("title", "")).strip().casefold())
            existing.update(m.strip().casefold() for m in re.findall(r"^##\s+(.+)$", text, re.M))
        for i, entry in enumerate(entries, 1):
            name = entry.get("name") if isinstance(entry, dict) else None
            names = [str(n).strip() for n in (name.values() if isinstance(name, dict) else [name]) if str(n or "").strip()]
            if not names:
                errors.append(f"{rel}: entry {i} has no name")
            elif any(n.casefold() in existing for n in names):
                covered.append(f"{rel}: {names[0]}")
            topic = entry.get("topic") if isinstance(entry, dict) else None
            if topic is not None and topic not in topics:
                errors.append(f"{rel}: entry {i} has unknown topic {topic!r} (see extra.topics in mkdocs.base.yml)")
            elif topic is None and uses_topics:
                errors.append(f"{rel}: entry {i} has no topic, but other entries in the list have one")
    return covered


def check_dates(errors: list[str], rel: str, meta: dict) -> None:
    status = meta.get("status")
    for field, statuses in (("completed", {"complete", "reviewed"}), ("reviewed", {"reviewed"})):
        value = meta.get(field)
        if status in statuses:
            if value is None:
                errors.append(f"{rel}: status is {status} but {field} (date) is missing")
            elif not isinstance(value, date) or isinstance(value, datetime):
                errors.append(f"{rel}: {field} must be a date YYYY-MM-DD, got {value!r}")
        elif value is not None:
            errors.append(f"{rel}: {field} date set but status is {status!r}")


def main() -> int:
    if len(sys.argv) == 3 and sys.argv[1] == "--hash":
        path = Path(sys.argv[2]).resolve()
        lang = path.relative_to(DOCS).parts[0]
        print(f"{lang}:{source_hash(path.read_text(encoding='utf-8'))}")
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
    for lang_dir in sorted(p for p in DOCS.iterdir() if p.is_dir()):
        if lang_dir.name not in languages:
            errors.append(f"docs/{lang_dir.name}: not a language in extra.alternate (mkdocs.base.yml)")

    # Every version of a page: uri -> {lang: (rel, text, body, meta)}
    pages: dict[str, dict[str, tuple]] = {}
    for lang in languages:
        lang_dir = DOCS / lang
        for page in sorted(lang_dir.rglob("*.md")) if lang_dir.is_dir() else []:
            text = page.read_text(encoding="utf-8")
            body, meta = get_data(text)
            uri = page.relative_to(lang_dir).as_posix()
            pages.setdefault(uri, {})[lang] = (page.relative_to(DOCS).as_posix(), text, body, meta)

    used_topics: set[str] = set()
    differing_topics: list[str] = []
    for uri, versions in sorted(pages.items()):
        is_index = uri.rsplit("/", 1)[-1] == "index.md"
        is_artifact = uri.split("/")[0] == "artifacts" and not is_index
        page_topics: dict[str, list] = {}
        for lang, (rel, text, body, meta) in versions.items():
            if is_index and uri != "index.md":
                # Only the title; the list of pages is generated.
                rest = re.sub(r"^# .*$", "", body, count=1, flags=re.M)
                if rest.strip():
                    busy_index.append(rel)
            if not str(meta.get("title", "")).strip():
                errors.append(f"{rel}: missing title")
            # Overview pages (index.md) may omit the status; the section listing is generated.
            status = meta.get("status")
            if not (is_index and "status" not in meta) and status not in STATUSES:
                errors.append(f"{rel}: status must be one of {sorted(STATUSES)}, got {status!r}")
            check_dates(errors, rel, meta)
            authors = parse_people(meta.get("authors"))
            if authors is None:
                errors.append(f"{rel}: authors must be GitHub handles, optionally 'handle (Full Name)'")
            elif not authors and status in {"complete", "reviewed"}:
                errors.append(f"{rel}: status is {status} but authors are missing")
            reviewers = parse_people(meta.get("reviewers"))
            if reviewers is None:
                errors.append(f"{rel}: reviewers must be GitHub handles, optionally 'handle (Full Name)'")
            elif reviewers and status != "reviewed":
                errors.append(f"{rel}: reviewers set but status is {status!r}")
            elif not reviewers and status == "reviewed":
                errors.append(f"{rel}: status is reviewed but reviewers are missing")
            own = {p["handle"].casefold() for p in authors or []} & {p["handle"].casefold() for p in reviewers or []}
            if own:
                errors.append(f"{rel}: reviewed by its own author(s): {', '.join(sorted(own))}")
            keys = meta.get("topics")
            if keys is not None and not is_artifact:
                errors.append(f"{rel}: topics are only for artifact pages")
            elif keys is not None and not isinstance(keys, list):
                errors.append(f"{rel}: topics must be a list of keys, got {keys!r}")
            elif keys:
                page_topics[lang] = keys
                for key in keys:
                    if key in topics:
                        used_topics.add(key)
                    else:
                        errors.append(f"{rel}: unknown topic {key!r} (see extra.topics in mkdocs.base.yml)")
            translation, source = meta.get("translation"), meta.get("translation_of")
            if translation is None and source is None:
                continue
            if translation not in TRANSLATIONS:
                errors.append(f"{rel}: translation must be one of {sorted(TRANSLATIONS)}")
            m = TRANSLATION_OF.fullmatch(str(source or ""))
            if not m:
                errors.append(f"{rel}: translation_of must be '<lang>:sha256:<12 hex>', got {source!r}")
            elif m["lang"] == lang or m["lang"] not in versions:
                errors.append(f"{rel}: translation_of names {m['lang']!r}, but there is no version of this page in that language")
            elif m["hash"] != source_hash(versions[m["lang"]][1]):
                outdated.append(rel)
        if is_artifact and not page_topics:
            without_topics.append(versions[next(iter(versions))][0])
        if len({tuple(sorted(k)) for k in page_topics.values()}) > 1:
            differing_topics.append(f"{uri}: " + "; ".join(f"{lang}: {', '.join(k)}" for lang, k in page_topics.items()))

    for rel in outdated:
        print(f"outdated translation (source version changed): {rel}")
    for entry in differing_topics:
        print(f"topics differ between language versions: {entry}")
    for rel in busy_index:
        print(f"overview page with more than the title: {rel}")
    for rel in without_topics:
        print(f"artifact page without topics: {rel}")
    covered_gaps = check_gaps(errors, topics, languages)
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
        f"{len(differing_topics)} page(s) with differing topics, "
        f"{len(unused_topics)} unused topic(s), {len(covered_gaps)} covered gap entr(y/ies)"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
