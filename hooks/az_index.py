"""A-Z list on the index page of the sections in extra.az_index (e.g. the glossary).

Instead of the usual list of pages and subsections, the index page lists every page below the
section alphabetically, grouped by first letter, each with the first sentence of its text as a
short description. Subsections (folders) still group the pages in the navigation.
"""

import re
import unicodedata
from pathlib import PurePosixPath

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page
from mkdocs.utils.meta import get_data

MAX_EXCERPT = 220
ABBREVIATIONS = {"bzw", "ca", "evtl", "ggf", "inkl", "nr", "usw", "vgl", "etc", "bspw", "max", "min", "sog"}


def _fold(text: str) -> str:
    """Lower case without accents, for sorting and grouping (Ä sorts as A)."""
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().casefold()


def excerpt(body: str) -> str:
    """First sentence of the first text paragraph (no headings, lists, tables or placeholders)."""
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    for para in re.split(r"\n\s*\n", body):
        para = para.strip()
        if not para or para.startswith(("#", "|", "-", "*Noch kein", "!!!", "<", "```")) or re.match(r"\d+\.", para):
            continue
        text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", para)
        text = " ".join(re.sub(r"[*_`]", "", text).split())
        for m in re.finditer(r"[.!?](?=\s+[A-ZÄÖÜ])", text):
            # Skip abbreviations such as "z. B.", "z.B." or "ca.".
            word = text[: m.start()].split()[-1].lstrip("([\"'„“")
            if "." not in word and word.casefold() not in ABBREVIATIONS and len(word) > 1:
                text = text[: m.end()]
                break
        if len(text) > MAX_EXCERPT:
            text = text[:MAX_EXCERPT].rsplit(" ", 1)[0] + " …"
        return text
    return ""


def on_page_markdown(markdown: str, page: Page, config: MkDocsConfig, files: Files) -> str:
    section = PurePosixPath(page.file.src_uri).parent.as_posix()
    if page.file.name != "index" or section not in config.extra.get("az_index", []):
        return markdown
    entries = []
    for file in files.documentation_pages():
        if not file.src_uri.startswith(section + "/") or file.name == "index":
            continue
        body, meta = get_data(file.content_string)
        title = str(meta.get("title") or file.name)
        entries.append({
            "title": title,
            "url": file.url,
            "status": meta.get("status"),
            "excerpt": excerpt(body),
        })
    groups: dict[str, list[dict]] = {}
    for entry in sorted(entries, key=lambda e: _fold(e["title"])):
        letter = _fold(entry["title"])[:1].upper()
        groups.setdefault(letter if letter.isalpha() else "#", []).append(entry)
    page.meta["dn_az"] = [{"letter": letter, "entries": items} for letter, items in groups.items()]
    return markdown
