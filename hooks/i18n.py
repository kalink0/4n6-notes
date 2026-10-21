"""Language handling for the per-language MkDocs builds.

German (extra.source_docs_dir) is the source language. Every other language build
contains every German page: a page without a translation is added from the German
source and marked as fallback, so a missing translation is visible instead of absent.

Front matter of a translated page:
    translation_of: <hash of the German page body, see scripts/check_content.py --hash>
    translation: machine | human
If the German body no longer matches translation_of, the page is marked outdated.
"""

import hashlib
from pathlib import Path

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import File, Files
from mkdocs.structure.nav import Navigation, Section
from mkdocs.structure.pages import Page
from mkdocs.utils.meta import get_data

_fallback: set[str] = set()


def source_hash(text: str) -> str:
    """Hash of a page body without front matter, used for translation_of.

    The "sha256:" prefix keeps YAML from reading an all-digit hash as a number.
    """
    body, _ = get_data(text.replace("\r\n", "\n"))
    return "sha256:" + hashlib.sha256(body.strip().encode("utf-8")).hexdigest()[:12]


def _is_source_build(config: MkDocsConfig) -> bool:
    return config.theme["language"] == config.extra["source_language"]


def _source_dir(config: MkDocsConfig) -> Path:
    return Path(config.config_file_path).parent / config.extra["source_docs_dir"]


def on_files(files: Files, config: MkDocsConfig) -> Files:
    _fallback.clear()
    if _is_source_build(config):
        return files
    src = _source_dir(config)
    for path in sorted(src.rglob("*.md")):
        uri = path.relative_to(src).as_posix()
        if files.get_file_from_path(uri) is None:
            files.append(File.generated(config, uri, abs_src_path=str(path)))
            _fallback.add(uri)
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
    page.meta["i18n_fallback"] = uri in _fallback
    if _is_source_build(config):
        return markdown
    source = _source_dir(config) / uri
    if page.meta["i18n_fallback"]:
        # Edits belong to the German source, not to a translation that does not exist yet.
        page.edit_url = f"{config.repo_url}/edit/main/{config.extra['source_docs_dir']}/{uri}"
    elif source.is_file():
        expected = source_hash(source.read_text(encoding="utf-8"))
        page.meta["i18n_outdated"] = page.meta.get("translation_of") != expected
    return markdown
