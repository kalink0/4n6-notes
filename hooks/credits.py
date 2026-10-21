"""Authors and reviewers shown on the page.

Front matter:
    authors: [handle, ...]     on the German page only; translations take them from there
    reviewers: [handle, ...]   on each page, together with status and reviewed

Each entry is a GitHub handle, optionally followed by the full name in parentheses:
"kalink0" or "kalink0 (Max Mustermann)". The handle links to the GitHub profile.
The format and the rule that nobody reviews their own page are checked by
scripts/check_content.py.
"""

import re
from pathlib import Path

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page
from mkdocs.utils.meta import get_data

PERSON = re.compile(r"(?P<handle>[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?)(?: \((?P<name>[^()]+)\))?")


def parse_people(value) -> list[dict] | None:
    """Front matter value as a list of {handle, name}; None if it is malformed."""
    if value is None:
        return []
    if isinstance(value, str):
        value = [value]
    if not isinstance(value, list):
        return None
    people = []
    for entry in value:
        m = PERSON.fullmatch(str(entry).strip())
        if not m:
            return None
        people.append({"handle": m["handle"], "name": (m["name"] or "").strip()})
    return people


def _source_authors(page: Page, config: MkDocsConfig) -> object:
    source = Path(config.config_file_path).parent / config.extra["source_docs_dir"]
    path = source / page.file.src_uri
    if not path.is_file():
        return None
    _, meta = get_data(path.read_text(encoding="utf-8"))
    return meta.get("authors")


def on_page_markdown(markdown: str, page: Page, config: MkDocsConfig, files: Files) -> str:
    # Malformed entries are reported by scripts/check_content.py and not shown.
    page.meta["dn_authors"] = parse_people(_source_authors(page, config)) or []
    page.meta["dn_reviewers"] = parse_people(page.meta.get("reviewers")) or []
    return markdown
