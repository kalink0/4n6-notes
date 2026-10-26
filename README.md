# 4n6 Notes

A collection of notes on digital forensics: artifact descriptions,
deep dives into file systems and file formats, and a glossary.

Since 2017 I have collected this knowledge in a private knowledge base. I have now decided to
continue it here in public.

Pages can be written in any of the site's languages (currently German and English); the language
versions of a page are equal and are added over time. Most pages currently exist in German only.
Further languages can be added, see CONTRIBUTING.md (Languages).

**Website:** https://4n6.be-binary.de/

## Content status

- `status: draft` pages are unfinished and shown with a **Draft** banner and an icon in the navigation.
- `status: complete` pages are finished by their author; `status: reviewed` pages were also
  checked by a second person. Both show the authors and dates, reviewed pages also the reviewers
  (see CONTRIBUTING.md).
- Sections without content say “Noch kein Inhalt.” or “No content yet.”.
- A page without a version in the site's language shows another version (English first, then
  German) with a banner.
- Machine translations, translations whose source version has changed since and pages with a
  newer version in another language are marked as such.

## Corrections and feedback

Please open an [issue](https://github.com/kalink0/4n6-notes/issues) or a pull request.

## Repository layout

| Path | Content |
| --- | --- |
| `docs/de/` | German pages |
| `docs/en/` | English pages, same paths as `docs/de/` |
| `mkdocs.base.yml` | Shared configuration |
| `mkdocs.de.yml`, `mkdocs.en.yml` | Per-language configuration |
| `hooks/i18n.py` | Language versions of each page, fallback, outdated-translation detection, navigation order |
| `hooks/search_tags.py` | Platform and topic tags for artifact pages in the search |
| `hooks/credits.py` | Authors and reviewers shown on the page |
| `gaps/`, `hooks/gaps.py` | Entries a section does not cover yet, listed on the section's index page |
| `hooks/az_index.py` | A–Z list with short descriptions on the glossary's index page |
| `overrides/` | Theme overrides: banners, authors and reviewers, section listings, language selector |
| `scripts/check_content.py` | Content checks (also run in CI) |
| `scripts/build.py` | Builds all languages into `site/` |
| `CONTRIBUTING.md`, `templates/` | How to contribute, rules and template for pages |

## Page front matter

A language version (here German, `docs/de/`):

```yaml
---
title: "BAM - Background Activity Moderator"
status: complete     # draft | complete | reviewed
completed: 2026-10-19   # with complete and reviewed
authors: [some-handle (Full Name)]   # GitHub handle, optionally with the full name
# reviewers: [other-handle]  with status: reviewed, never whoever made the change
# reviewed: 2026-10-21       review date, with status: reviewed
topics: [program-execution]   # artifact pages only, keys from extra.topics in mkdocs.base.yml
---
```

A version translated from another one (same path under another language, here `docs/en/`) has
its own status, dates, authors and reviewers, plus where it was translated from:

```yaml
---
title: "BAM - Background Activity Moderator"
status: complete
completed: 2026-10-21
authors: [some-translator]
translation: human   # human | machine
translation_of: de:sha256:0123456789ab   # language and hash of the version it was translated from
---
```

`translation_of` is printed by:

```sh
python scripts/check_content.py --hash docs/de/artifacts/windows/bam.md
```

When that version changes later, the translation is marked as possibly outdated until
`translation_of` is updated. A version extended on its own drops `translation` and
`translation_of`. Topics may be set in any version; see CONTRIBUTING.md (Languages).

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
