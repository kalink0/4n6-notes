"""Language handling for the per-language MkDocs builds.

Every language of extra.alternate has its own docs/<lang>/ folder. The versions of a page (same
path in several languages) are equal: each has its own title, status, authors and reviewers. A
version may say it was translated from another one:
    translation: machine | human
    translation_of: <lang>
If that version was completed later than this one, the translation is marked outdated.

Every language build contains every page: a page without a version in the build language is
added from another version, chosen by extra.fallback_order and then the order of
extra.alternate, and marked as fallback. Each page lists its versions in the other languages with
their completion date, and points out versions completed later than itself.
"""

import re
from pathlib import Path

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import File, Files
from mkdocs.structure.nav import Navigation, Section
from mkdocs.structure.pages import Page
from mkdocs.utils.meta import get_data

TRANSLATION_OF = re.compile(r"(?P<lang>[a-z]{2,3}(?:-[A-Za-z]+)?)")

# Pages of the current build taken from another language: src_uri -> language of that version.
_fallback: dict[str, str] = {}


def languages(config: MkDocsConfig) -> list[str]:
    return [alt["lang"] for alt in config.extra["alternate"]]


def fallback_languages(config: MkDocsConfig) -> list[str]:
    """Languages in the order in which a missing version is taken from them."""
    langs = languages(config)
    preferred = [lang for lang in config.extra.get("fallback_order", []) if lang in langs]
    return preferred + [lang for lang in langs if lang not in preferred]


def docs_root(config: MkDocsConfig) -> Path:
    return Path(config.config_file_path).parent / "docs"


def versions(config: MkDocsConfig, uri: str) -> dict[str, dict]:
    """Front matter of every version of a page, by language (in the order of extra.alternate)."""
    found = {}
    for lang in languages(config):
        path = docs_root(config) / lang / uri
        if path.is_file():
            _, meta = get_data(path.read_text(encoding="utf-8"))
            found[lang] = meta
    return found


def on_files(files: Files, config: MkDocsConfig) -> Files:
    _fallback.clear()
    docs = docs_root(config)
    build_lang = config.theme["language"]
    uris = sorted({
        path.relative_to(docs / lang).as_posix()
        for lang in languages(config)
        if lang != build_lang and (docs / lang).is_dir()
        for path in (docs / lang).rglob("*.md")
    })
    for uri in uris:
        if files.get_file_from_path(uri) is not None:
            continue
        for lang in fallback_languages(config):
            path = docs / lang / uri
            if path.is_file():
                files.append(File.generated(config, uri, abs_src_path=str(path)))
                _fallback[uri] = lang
                break
    return files


def _front_title(page: Page) -> str:
    _, meta = get_data(page.file.content_string)
    return str(meta.get("title") or page.file.name)


def _section_index(section: Section) -> Page | None:
    for child in section.children:
        if isinstance(child, Page) and child.file.name == "index":
            return child
    return None


def on_nav(nav: Navigation, config: MkDocsConfig, files: Files) -> Navigation:
    # Section labels come from the title of the section's index page, not the folder name.
    # Below the top level, entries are sorted by title (index page first); the top level
    # follows extra.nav_order (folder names).
    def label(item: Page | Section) -> str:
        if isinstance(item, Section):
            index = _section_index(item)
            if index is not None:
                item.title = _front_title(index)
            return str(item.title)
        return _front_title(item)

    def sort_key(item: Page | Section) -> tuple[int, str]:
        is_index = isinstance(item, Page) and item.file.name == "index"
        return (0 if is_index else 1, label(item).casefold())

    def walk(items: list) -> None:
        for item in items:
            if isinstance(item, Section):
                item.children.sort(key=sort_key)
                walk(item.children)

    order = config.extra.get("nav_order", [])

    def top_key(item: Page | Section) -> tuple[int, str]:
        if isinstance(item, Page):
            return (-1, "")
        index = _section_index(item)
        folder = index.file.src_uri.split("/")[0] if index else ""
        return (order.index(folder) if folder in order else len(order), label(item).casefold())

    walk(nav.items)
    nav.items.sort(key=top_key)
    return nav


def on_page_markdown(markdown: str, page: Page, config: MkDocsConfig, files: Files) -> str:
    uri = page.file.src_uri
    lang = _fallback.get(uri, config.theme["language"])
    page.meta["i18n_fallback"] = uri in _fallback
    page.meta["i18n_lang"] = lang
    if page.meta["i18n_fallback"]:
        # Edits belong to the version that is shown.
        page.edit_url = f"{config.repo_url}/edit/main/docs/{lang}/{uri}"
    names = {alt["lang"]: alt["name"] for alt in config.extra["alternate"]}
    own_date = page.meta.get("completed")
    others = {other: meta for other, meta in versions(config, uri).items() if other != lang}
    # Malformed values are reported by scripts/check_content.py.
    m = TRANSLATION_OF.fullmatch(str(page.meta.get("translation_of", "")))
    source_lang = m["lang"] if m and m["lang"] in others else None
    # A translation of this version is completed after it, which does not make it newer.
    page.meta["i18n_versions"] = [
        {
            "lang": other,
            "name": names[other],
            "completed": meta.get("completed"),
            "newer": bool(own_date and meta.get("completed") and meta["completed"] > own_date
                          and str(meta.get("translation_of", "")) != lang),
        }
        for other, meta in others.items()
    ]
    if source_lang:
        page.meta["i18n_source"] = {"lang": source_lang, "name": names.get(source_lang, source_lang)}
        # A newer source is shown as an outdated translation, not again as a newer version.
        for version in page.meta["i18n_versions"]:
            if version["lang"] == source_lang:
                page.meta["i18n_outdated"] = version["newer"]
                version["newer"] = False
    return markdown
