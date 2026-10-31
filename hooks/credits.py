"""Authors and reviewers shown on the page.

Front matter:
    authors: [handle, ...]     who wrote this language version (or translated it)
    reviewers: [handle, ...]   who reviewed it, together with status and reviewed

Each language version has its own authors and reviewers.

Each entry is a GitHub handle, optionally followed by the full name in parentheses:
"some-handle" or "some-handle (Full Name)". The handle links to the GitHub profile.
The format is checked by scripts/check_content.py.
"""

import re

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page

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


def on_page_markdown(markdown: str, page: Page, config: MkDocsConfig, files: Files) -> str:
    # Malformed entries are reported by scripts/check_content.py and not shown.
    page.meta["dn_authors"] = parse_people(page.meta.get("authors")) or []
    page.meta["dn_reviewers"] = parse_people(page.meta.get("reviewers")) or []
    return markdown
