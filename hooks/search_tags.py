"""Search tags for artifact pages: platform and topics.

Pages under artifacts/<folder>/ get the platform from extra.platforms as a tag, plus the label
of each topic listed in the German page's front matter (topics: [key, ...]) in the build
language, from extra.topics. Topics are always read from the German source, so a translation
does not repeat them.

The search shows the tags next to each result and makes them searchable
(e.g. "+tags:ios +fsevents"). The topic labels of the other languages are added to the page as
hidden text, so "program execution" also finds the page on the German site. The pages
themselves do not show the tags.
"""

from html import escape
from pathlib import Path

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page
from mkdocs.utils.meta import get_data


def _source_topics(page: Page, config: MkDocsConfig) -> list:
    source = Path(config.config_file_path).parent / config.extra["source_docs_dir"]
    path = source / page.file.src_uri
    if not path.is_file():
        return []
    _, meta = get_data(path.read_text(encoding="utf-8"))
    return meta.get("topics") or []


def on_page_markdown(markdown: str, page: Page, config: MkDocsConfig, files: Files) -> str:
    parts = page.file.src_uri.split("/")
    if len(parts) < 3 or parts[0] != "artifacts":
        return markdown
    lang = config.theme["language"]
    tags: list[str] = []
    hidden: list[str] = []
    platform = config.extra.get("platforms", {}).get(parts[1])
    if platform:
        tags.append(platform)
    topics = config.extra.get("topics", {})
    for key in _source_topics(page, config):
        # Unknown keys are reported by scripts/check_content.py.
        labels = topics.get(key)
        if labels:
            tags.append(labels[lang])
            hidden += [label for code, label in labels.items() if code != lang and label != labels[lang]]
    page.meta["tags"] = tags
    page.meta["search_hidden_labels"] = hidden
    return markdown


def on_page_content(html: str, page: Page, config: MkDocsConfig, files: Files) -> str:
    hidden = page.meta.get("search_hidden_labels")
    if not hidden:
        return html
    # Right after the h1, so the labels belong to the page's own search entry.
    block = f"<div hidden>{escape(', '.join(hidden))}</div>"
    head, sep, rest = html.partition("</h1>")
    return head + sep + block + rest if sep else block + html
