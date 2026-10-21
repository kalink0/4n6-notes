"""Gaps: entries a section does not cover yet, listed on the section's index page.

gaps/<section>.yml belongs to docs/<lang>/<section>/index.md, e.g. gaps/artifacts/windows.yml
or gaps/glossary.yml. It is a list of entries:

    - name: Browser-Historie
      note: optional short note
      topic: web-activity

name and note are text in any language or a mapping per language ({de: ..., en: ...}); a
language without its own text shows another one, in the order of extra.fallback_order. topic is
a key from extra.topics: if a file uses topics, every entry has one and the page groups the
entries by topic, in the order of extra.topics. Entries that already have a page or heading are
reported by scripts/check_content.py.
"""

from pathlib import Path

import yaml
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page

from i18n import fallback_languages


def gaps_dir(config_dir: Path) -> Path:
    return config_dir / "gaps"


def gap_file(config_dir: Path, section: str) -> Path:
    return gaps_dir(config_dir) / f"{section}.yml"


def localized(value, order: list[str]) -> str:
    if isinstance(value, dict):
        texts = [value.get(lang) for lang in order] + list(value.values())
        return str(next((t for t in texts if t), ""))
    return str(value or "")


def on_page_markdown(markdown: str, page: Page, config: MkDocsConfig, files: Files) -> str:
    if page.file.name != "index":
        return markdown
    section = Path(page.file.src_uri).parent.as_posix()
    path = gap_file(Path(config.config_file_path).parent, section)
    if section == "." or not path.is_file():
        return markdown
    lang = config.theme["language"]
    order = [lang, *fallback_languages(config)]
    # Malformed files are reported by scripts/check_content.py.
    entries = [e for e in yaml.safe_load(path.read_text(encoding="utf-8")) or [] if isinstance(e, dict)]
    topics = config.extra.get("topics", {})
    groups: dict[str, list[dict]] = {}
    for key in ["", *topics]:
        items = [
            {
                "name": localized(e.get("name"), order),
                "note": localized(e.get("note"), order),
            }
            for e in entries
            if (e.get("topic") or "") == key
        ]
        if items:
            groups[key] = items
    page.meta["dn_gaps"] = [
        {"title": topics[key][lang] if key else "", "entries": items} for key, items in groups.items()
    ]
    return markdown
