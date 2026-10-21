"""Search tags for artifact pages: platform and topics.

Pages under artifacts/<folder>/ get the platform from extra.platforms as a tag, plus the label
of each topic in the build language, from extra.topics. Topics (topics: [key, ...]) belong to the
page, not to a language version: they may be set in any version, and every version gets the
topics of all versions.

The search shows the tags next to each result and makes them searchable
(e.g. "+tags:ios +fsevents"). The topic labels of the other languages are added to the page as
hidden text, so "program execution" also finds the page on the German site. The pages
themselves do not show the tags.
"""

from html import escape

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page

from i18n import versions


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
    keys = [key for meta in versions(config, page.file.src_uri).values() for key in meta.get("topics") or []]
    for key in dict.fromkeys(keys):
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
