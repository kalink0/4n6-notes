"""Build all languages into site/: site/de/, site/en/, plus a root redirect and 404 page.

Usage: python scripts/build.py
"""

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DEFAULT_LANG = "de"

REDIRECT = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>4n6 Notes</title>
<meta http-equiv="refresh" content="0; url={lang}/">
<link rel="canonical" href="{lang}/">
</head>
<body>
<p><a href="{lang}/">4n6 Notes</a></p>
</body>
</html>
"""


def main() -> int:
    check = subprocess.run([sys.executable, str(ROOT / "scripts" / "check_content.py")])
    if check.returncode != 0:
        return check.returncode

    configs = sorted(p for p in ROOT.glob("mkdocs.*.yml") if p.name != "mkdocs.base.yml")
    if SITE.exists():
        shutil.rmtree(SITE)
    for config in configs:
        result = subprocess.run(
            [sys.executable, "-m", "mkdocs", "build", "--strict", "--config-file", str(config)],
            cwd=ROOT,
        )
        if result.returncode != 0:
            return result.returncode

    (SITE / "index.html").write_text(REDIRECT.format(lang=DEFAULT_LANG), encoding="utf-8")
    # GitHub Pages serves /404.html for every unknown path; the German one uses absolute asset URLs.
    shutil.copy(SITE / DEFAULT_LANG / "404.html", SITE / "404.html")
    return 0


if __name__ == "__main__":
    sys.exit(main())
