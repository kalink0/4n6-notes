# Contributing

Corrections, new pages, translations and reviews are welcome. This file describes how to submit them
and the rules for the pages. Template for new artifact pages:
[`templates/artifact.md`](templates/artifact.md).

## How to contribute

1. Fork the repository and create a branch.
2. Make your changes following the rules below.
3. Run the content checks and the build (see README, "Build locally"):
   `.venv/bin/python scripts/build.py`. It fails on rule violations and broken links.
4. Open a pull request. The same checks run there automatically.

For smaller corrections or suggestions, opening an issue is enough.

Headings and fixed phrases that appear on the pages are given here in German, exactly as they are
written on the page; their English wording is listed under [Languages](#languages).

## Languages

A page can be written in any language of the site (`docs/<lang>/`, currently `de` and `en`). The
same path in several languages gives the page's **language versions**. They are equal: none of them
is the original.

- Each version has its own title, status, `completed` date, authors and reviewers. Whoever writes,
  translates or extends a version is one of its authors.
- Each version may be extended on its own. When content is added to one version, the other
  versions should follow; a later `completed` date in another version is shown on the page
  ("Newer language version available").
- A version translated from another one says so: `translation: human` or `machine` and
  `translation_of: <lang>` (see README, "Page front matter"). It is marked as possibly outdated
  when that version has a later `completed` date; after updating the translation, set its own
  `completed`. A version that is extended on its own drops both fields.
- Whoever changes the content of a finished version updates its `completed` date; corrections
  that do not change the content (typos, formatting) leave it as it is.
- A machine translation is checked in the review, not by its author. Until then it shows a notice
  that no person has checked it; once `reviewed`, the notice says so. `translation: machine` stays.
- Topics belong to the page, not to a language; they may be set in any version, and the page gets
  the topics of all versions. `scripts/check_content.py` reports versions with differing topics.
- A page without a version in a language is shown there in another version, with a banner: English
  first (widest readership), then German (the repository's main language), then the others
  (`extra.fallback_order` in `mkdocs.base.yml`).

Adding a language (e.g. French, `fr`):

1. `mkdocs.fr.yml`: copy `mkdocs.en.yml` and change `docs_dir`, `site_dir`, `site_url`,
   `edit_uri`, `copyright`, `theme.language`, the search language and the status label.
2. `mkdocs.base.yml`: add the language to `extra.alternate` and a label to every topic in
   `extra.topics` (`scripts/check_content.py` reports missing labels).
3. `overrides/partials/dn-strings.html`: add the UI strings; until then the English ones are shown.
4. `docs/fr/index.md`: the start page, e.g. translated from `docs/en/index.md` or
   `docs/de/index.md`. All other pages are shown in another version until they exist in French.
5. Add the language's headings and phrases to the table below.

Fixed headings and phrases (each version uses the column of its language):

| German | English |
| --- | --- |
| `## Bedeutung` | `## Meaning` |
| `## Spezifische Kurzinformation` | `## Key facts` |
| `## Referenzen` | `## References` |
| `## Tools` | `## Tools` |
| `## Quellen` (glossary) | `## Sources` |
| `*Noch kein Inhalt.*` | `*No content yet.*` |
| `Ablageort` | `Location` |

## Structure

Every artifact page has exactly these four sections, in this order:

1. `## Bedeutung` (meaning)
2. `## Spezifische Kurzinformation` (key facts)
3. `## Referenzen` (references)
4. `## Tools`

A section without content stays in place and contains `*Noch kein Inhalt.*` (no content yet).
Subsections use `###`, not bold text (e.g. for individual entry types).

If a similar artifact exists on several platforms (e.g. FSEvents on macOS and iOS), these are
separate artifacts, each with its own complete page. Texts are not merged or replaced by links, even
if they are almost identical. The pages do not link to each other.

## Topics

Every artifact page gets at least one topic in its front matter (in any language version). Topics say
what the artifact gives evidence of; they are shown and searchable in the search, together with
the platform tag that every page gets automatically from its folder.

```yaml
topics: [program-execution, network]
```

- Only keys from `extra.topics` in `mkdocs.base.yml`. A new topic is added there first, with a
  label for every language.
- Keys never change. Only the labels may be edited.
- Topics are the same in every language version (see [Languages](#languages)).
- Collection artifacts (e.g. event logs, Unified Logs, Registry) get only their most important
  topics, not every topic that could apply.
- Missing topics are reported by `scripts/check_content.py`.

## Status

A page has one of three statuses:

| Status | Meaning | Shown on the page |
| --- | --- | --- |
| `draft` | Unfinished, sections missing or incomplete | **Entwurf** banner, icon in the navigation |
| `complete` | Finished and checked by the author | Authors, completion date, "not yet reviewed" |
| `reviewed` | Also checked by a second person | Authors, completion date, reviewers, review date, icon in the navigation |

Overview pages (`index.md`) have no status. They only hold the title; the list of pages in the
section is generated.

People are given as GitHub handles, optionally followed by the full name in parentheses. The
authors and reviewers are set per language version.

```yaml
status: reviewed
completed: 2026-10-19
authors: [some-handle (Full Name)]
reviewers: [other-handle]
reviewed: 2026-10-21
```

- New pages start as `draft`. The author may add themselves to `authors` right away.
- When the page is finished, the author sets `status: complete` and `completed` (date).
- Only a reviewer sets `status: reviewed`, after checking the content, and adds `reviewers` and
  `reviewed` (date). Nobody reviews their own change; an earlier author may review a later
  change by someone else.
- Anyone may review. Reviews, like all other changes, are submitted as a pull request.
- If the content of a `reviewed` page changes, it goes back to `complete` (or `draft`, if it is
  unfinished again) until it has been reviewed again; `reviewers` and `reviewed` are removed.
  Whoever makes the change adds themselves to `authors` and updates `completed`.

## Glossary

The glossary collects short explanations of terms, also meant as text modules for reports.

- One file per term, e.g. `docs/de/glossary/terms/carving.md`. Folders group related terms
  (`terms/`, `acquisition-types/`, `encryption-and-attacks/`); a new group is a new folder with an
  `index.md` that holds only the title.
- Each term has its own status and authors, like an artifact page. There is no fixed structure:
  title, then the explanation, optionally followed by `## Quellen` (sources).
- The first sentence defines the term. It is shown as the short description in the A–Z list on the
  glossary's index page, so it must make sense on its own.

## Gaps

What a section does not cover yet is listed in `gaps/<section>.yml`, e.g.
`gaps/artifacts/windows.yml` or `gaps/glossary.yml`. The list is shown on the section's index page
under "Noch nicht beschrieben" (not covered yet).

```yaml
- name: NetworkList
  note: bekannte Netzwerke mit erster und letzter Verbindung   # optional
  topic: network
```

- One entry per missing artifact or term, without rating.
- Artifact gaps get exactly one topic (key from `extra.topics`); the page groups them by topic.
  Lists without topics (e.g. the glossary) are shown as one flat list.
- File system structures (e.g. `$MFT`, FAT) are not artifact gaps; they belong to the deep dives.
- The note is short and factual.
- `name` and `note` are written in German or English, or given per language (`{de: …, en: …}`);
  a site without its own text shows the German one.
- When an entry gets its page (or, in the glossary, its section), it is removed from the list.
  `scripts/check_content.py` reports entries whose name already appears as a page title or heading.
- Gaps are listed in the gap file, not as checklists on the pages.

## Bedeutung (meaning)

Running text in two parts:

1. **What is the artifact?** Which component writes it, when, and for what purpose.
2. **What does it show forensically?** Which statement an entry supports ("shows that …") and where
   the limits are (what it does *not* show, common misinterpretations).

If the artifact contains a series of sub-artifacts (e.g. streams in KnowledgeC or Biome, event IDs in
Event Logs), a table follows. Properties of individual entries (e.g. flags in FSEvents) are not
sub-artifacts.

```markdown
| Eintragstyp | Belegt | Relevante Felder |
| --- | --- | --- |
| `/app/usage` | App war im Zeitraum im Vordergrund | `ZSTARTDATE`, `ZENDDATE`, `ZVALUESTRING` |
```

- "Belegt" (shows) is short and to the point, one sentence if possible.
- "Relevante Felder" (relevant fields) lists only the fields needed for that type's statement.
- If a type needs more than two sentences (limitations, pitfalls), it also gets a `###` subsection
  below the table.

Not in this section: paths, version lists, general table and field names (except in the type
table), tools. These go into the key facts.

## Spezifische Kurzinformation (key facts)

Numbered list, one fact per item, short. Items appear in this order (anything that does not apply
or is unknown is left out):

1. Availability: operating system/version, hardware if relevant
2. Prerequisites: enabled by default or opt-in, can be disabled
3. Retention: period, rotation, deletion behavior
4. Format and structure: file type
5. Timestamps: format, time zone, which timestamp means what
6. Particularities and pitfalls
7. Location (Ablageort), always the last item

Location: the path on its own line, indented by three spaces under the list item.
With several paths, one per line, with two spaces at the end of the line and the platform in front
(not bold):

```markdown
7. Ablageort:  
   **`/private/var/mobile/Library/…/datei.db`**

7. Ablageort:  
   iOS: **`/private/var/…`**  
   macOS: **`~/Library/…`**
```

### Writing paths

All paths on the pages (files, folders, registry keys) are written in bold and in backticks:

```markdown
**`C:\Windows\Prefetch\*.pf`**
**`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs`**
**`/private/var/db/diagnostics`**
```

- Backslashes are always single, never doubled (nothing is escaped inside backticks).
- Placeholders use curly braces, e.g. `{USER}`, `{USER_SID}`, `{DRIVE}`, `{UUID}`; never angle
  brackets.
- Applies to locations and to paths in running text.
- Exception: paths in table cells are only in backticks, not bold.

Statements that change with updates (versions, defaults, rollouts) get a point in time:
"seit iOS 16" (since iOS 16), "Stand 2026-07" (as of 2026-07).

## Referenzen (references)

- Format: `YYYY-MM: <URL>`, one source per paragraph.
- The date is the source's **publication date**, not the access date. If the publication date is
  not shown, check the page metadata (e.g. `datePublished`). If it is still unknown, use the access
  date with the suffix `(abgerufen)` (accessed).
- For revised documents, the date of the last revision applies.
- Order: newest first.
- Only sources that help an analyst understand or analyze the artifact (articles, talks, format
  descriptions). Sources that only prove a statement, such as operating system or tool source code,
  do not belong here.
- Only sources about this artifact. General sources (posters, cheat sheets for a whole platform)
  are not listed anywhere.
- Source without URL: `YYYY-MM: Author: Title *(Quelle wird ergänzt)*` (source to be added).

## Tools

- Format: `Name - <URL>`, one tool per paragraph. If only one module/plugin is relevant:
  `Name (Modul) - <URL>`.
- The URL points to the tool's main page (project page or repository), where the user can download
  it, not to the source code of a single module.
- No individual details on supported versions (e.g. "from iOS 17", "up to version 3"). For actively
  developed tools these go out of date quickly and cannot be maintained.
- Allowed is a note that no longer changes: if a tool is no longer developed and only handles older
  versions of the artifact, it is followed by `(nur alte Versionen)` (old versions only).
- Only free tools (open source or free to use), no commercial tools.
- Only tools that **decode this artifact** are listed, i.e. parse its content and output it in a
  structured form. Not sufficient:
  - format detection alone (e.g. by signature)
  - generic viewers (e.g. any SQLite browser for an SQLite-based artifact)

## Links

Pages contain no internal links (to artifacts, deep dives or glossary terms). They are hard to
keep up to date when pages are added, moved or renamed. Related pages are found through the
search. Links to external sources belong in the references and tools.
