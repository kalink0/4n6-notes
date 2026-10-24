"""Check that the links in the reference and tool sections of artifact pages are reachable.

Collects every http(s) URL below the headings "Referenzen"/"References" and "Tools" of the
pages in docs/<lang>/artifacts/ and requests each URL once. Fails on links that are gone
(404, 410, unknown host, refused connection). Reports without failing links that could not be
verified (other 4xx/5xx such as bot protection, timeouts), since those are often temporary or
caused by the request coming from CI.

Writes a Markdown report to $GITHUB_STEP_SUMMARY when set.

Usage: python scripts/check_links.py
"""

import os
import re
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SECTIONS = {"referenzen", "references", "tools"}
# Parentheses only as balanced pairs, e.g. ".../Windows%20Prefetch%20File%20(PF)%20format.asciidoc"
URL = re.compile(r"https?://(?:[^\s<>()\[\]]|\([^\s<>()]*\))+")
GONE = {404, 410}
TIMEOUT = 20
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def collect() -> dict[str, list[str]]:
    """Return {url: [page, ...]} for the links in the reference and tool sections."""
    links: dict[str, list[str]] = defaultdict(list)
    for page in sorted(DOCS.glob("*/artifacts/**/*.md")):
        rel = page.relative_to(ROOT).as_posix()
        in_section = False
        for line in page.read_text(encoding="utf-8").splitlines():
            heading = re.match(r"^##\s+(.+?)\s*$", line)
            if heading:
                in_section = heading.group(1).casefold() in SECTIONS
            elif in_section:
                for url in URL.findall(line):
                    url = url.rstrip(".,;:")
                    if rel not in links[url]:
                        links[url].append(rel)
    return links


def check(url: str) -> tuple[str, str]:
    """Return (result, detail) with result "ok", "gone" or "unverified"."""
    session = requests.Session()
    session.headers.update(HEADERS)
    detail = ""
    # HEAD first; many servers answer HEAD wrongly, so fall back to GET and retry once.
    for method in ("HEAD", "GET", "GET"):
        try:
            response = session.request(method, url, timeout=TIMEOUT, allow_redirects=True, stream=True)
            response.close()
        except requests.exceptions.ConnectionError as e:
            detail = f"connection error: {e.__class__.__name__}"
            if "NameResolution" in str(e) or "Connection refused" in str(e):
                return "gone", detail
            continue
        except requests.RequestException as e:
            detail = e.__class__.__name__
            continue
        if response.status_code < 400:
            return "ok", str(response.status_code)
        detail = f"HTTP {response.status_code}"
        if method == "GET" and response.status_code in GONE:
            return "gone", detail
    return "unverified", detail


def main() -> int:
    links = collect()
    with ThreadPoolExecutor(max_workers=16) as pool:
        results = dict(zip(links, pool.map(check, links)))

    gone = {u: r for u, r in results.items() if r[0] == "gone"}
    unverified = {u: r for u, r in results.items() if r[0] == "unverified"}
    print(f"{len(links)} links checked: {len(gone)} broken, {len(unverified)} unverified")
    for title, group in (("Broken", gone), ("Unverified", unverified)):
        for url, (_, detail) in sorted(group.items()):
            print(f"{title}: {url} ({detail}) in {', '.join(links[url])}")

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        lines = [f"{len(links)} links checked: {len(gone)} broken, {len(unverified)} unverified", ""]
        for title, group in (("Broken links", gone), ("Unverified links", unverified)):
            if not group:
                continue
            lines += [f"## {title}", "", "| Link | Result | Pages |", "| --- | --- | --- |"]
            for url, (_, detail) in sorted(group.items()):
                lines.append(f"| <{url}> | {detail} | {'<br>'.join(links[url])} |")
            lines.append("")
        with open(summary, "a", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")

    return 1 if gone else 0


if __name__ == "__main__":
    sys.exit(main())
