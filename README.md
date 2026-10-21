# DFIR Notes

A collection of notes on digital forensics and incident response: artifact descriptions,
deep dives into file systems and file formats, and a glossary.

German is the original language, English is added gradually.

**Website:** https://kalink0.github.io/dfir-notes/

## Content status

- `status: draft` pages are unfinished and shown with a **Draft** banner and an icon in the navigation.
- `status: complete` pages are finished by their author; `status: reviewed` pages were also
  checked by a second person. Both show the authors and dates, reviewed pages also the reviewers
  (see CONTRIBUTING.md).
- Sections without content say “Noch kein Inhalt.” (no content yet).
- English pages without a translation show the German original with a **Not yet translated** banner.
- Machine translations and translations whose German original has changed since are marked as such.

## Corrections and feedback

Please open an [issue](https://github.com/kalink0/dfir-notes/issues) or a pull request.

## Repository layout

| Path | Content |
| --- | --- |
| `docs/de/` | German pages (source) |
| `docs/en/` | English translations, same paths as `docs/de/` |
| `mkdocs.base.yml` | Shared configuration |
| `mkdocs.de.yml`, `mkdocs.en.yml` | Per-language configuration |
| `hooks/i18n.py` | Fallback to German, outdated-translation detection, navigation order |
| `hooks/search_tags.py` | Platform and topic tags for artifact pages in the search |
| `hooks/credits.py` | Authors (from the German page) and reviewers shown on the page |
| `gaps/`, `hooks/gaps.py` | Entries a section does not cover yet, listed on the section's index page |
| `hooks/az_index.py` | A–Z list with short descriptions on the glossary's index page |
| `overrides/` | Theme overrides: banners, authors and reviewers, section listings, language selector |
| `scripts/check_content.py` | Content checks (also run in CI) |
| `scripts/build.py` | Builds all languages into `site/` |
| `CONTRIBUTING.md`, `templates/` | Rules and template for artifact pages |

## Page front matter

German page:

```yaml
---
title: "BAM - Background Activity Moderator"
status: complete     # draft | complete | reviewed
completed: 2026-10-19   # with complete and reviewed
authors: [kalink0 (Marco Neumann)]   # GitHub handle, optionally with the full name
# reviewers: [some-handle]   with status: reviewed, never one of the authors
# reviewed: 2026-10-21       review date, with status: reviewed
topics: [program-execution]   # artifact pages only, keys from extra.topics in mkdocs.base.yml
---
```

English translation (same path under `docs/en/`):

```yaml
---
title: "BAM - Background Activity Moderator"
status: draft
translation: human   # human | machine
translation_of: sha256:0123456789ab
---
```

`translation_of` is the hash of the German page the translation is based on:

```sh
python scripts/check_content.py --hash docs/de/artifacts/windows/bam.md
```

When the German page changes later, the English page is marked as possibly outdated
until `translation_of` is updated.

## Build locally

```sh
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/build.py
.venv/bin/python -m http.server -d site
```

Then open http://localhost:8000/. For editing a single language with live reload:
`.venv/bin/mkdocs serve -f mkdocs.de.yml` (the language selector only works in the full build).

## License

The content is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).
Linked third-party documents are subject to the terms of their respective authors.
