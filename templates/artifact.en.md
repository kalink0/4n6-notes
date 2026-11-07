---
title: "Name of the artifact"
status: draft
authors: [github-handle]  # optionally with name: [github-handle (First Last)]
topics: []  # at least one key from extra.topics in mkdocs.base.yml
---

<!--
Template for artifact pages (English version). All rules in detail: CONTRIBUTING.md.
Notes are in comments like this one; they are not shown on the website.
A section without content stays in place and contains only: *No content yet.*
Status: draft (unfinished) → complete (finished by the author) → reviewed (checked by a second
person). People as GitHub handle, optionally with the name in parentheses.

Finished, set by the author:
    status: complete
    completed: 2026-10-19
    authors: [github-handle (First Last)]

Reviewed, added by the reviewer (never by whoever made the change); completed and authors stay:
    status: reviewed
    completed: 2026-10-19
    authors: [github-handle (First Last)]
    reviewers: [jane-doe (Jane Doe), john-d]
    reviewed: 2026-10-21

If the content of a reviewed page changes, it goes back to complete (or draft);
reviewers and reviewed are removed.
-->

# Name of the artifact

## Meaning

<!--
Running text in two parts:
1. What is the artifact? Which component writes it, when and for what purpose?
2. What does an entry show forensically, and what does it NOT show (limits, misinterpretations)?
No paths, version lists or tools; these go into the key facts.
Table and field names only in the "Relevant fields" column of the type table.
No internal links (to artifacts, deep dives or glossary).
-->

What is the artifact, which component writes it and when? What does the system use it for?

From a digital forensics point of view, an entry shows that … It does not show, however, that …

<!--
Table only for artifacts with a series of sub-artifacts (e.g. streams in KnowledgeC
or Biome). Otherwise delete the table.
"Shows": short, one sentence if possible. "Relevant fields": only those needed for this statement.
-->

| Entry type | Shows | Relevant fields |
| --- | --- | --- |
| `type/a` | … | `FIELD_X`, `FIELD_Y` |

<!-- Own subsection only if a type needs more than two sentences. Otherwise delete it. -->

### `type/a`

Detailed meaning of this entry type.

## Key facts

<!--
One entry per category, short, in this order; an entry may contain several statements.
Anything that does not apply or is unknown is left out.
Each entry starts with its category's label, exactly as below (e.g. "3. Retention: …").
Statements that change with updates say since when they apply: "since iOS 16", "since 2026-07".
This is the version or point in time from which it applies, not the date it was last checked.
Paths (files, folders, registry keys) are always bold and in backticks, in the location
as in running text:
    **`C:\Windows\Prefetch\*.pf`**
    **`HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs`**
    **`/private/var/db/diagnostics`**
Backslashes single, never doubled (nothing is escaped inside backticks).
Placeholders in curly braces: {USER}, {USER_SID}, {DRIVE}, {UUID}; never angle brackets.
Exception: in table cells, paths are only in backticks, not bold.
Location: path indented (3 spaces, under the list entry).
With several locations one per line, with two spaces at the end of the line:
7. Location:  
   iOS: **`/private/var/…`**  
   macOS: **`~/Library/…`**
-->

1. Availability: operating system/version, hardware if relevant
2. Prerequisites: enabled by default or opt-in, can be disabled by …
3. Retention: period, rotation, deletion behavior
4. Format and structure: file type
5. Timestamps: format, time zone, meaning of each timestamp
6. Particularities and pitfalls
7. Location:  
   **`/path/to/file`**

## References

<!--
Format: YYYY-MM: <URL>, one source per paragraph, newest first.
Date = publication or last revision. Not shown?
Check the page metadata (e.g. datePublished). Otherwise the access date with the suffix (accessed).
Only sources about this artifact that help an analyst (articles, talks,
format descriptions). No source code as mere proof.
Without URL: YYYY-MM: Author: Title *(source to be added)*
-->

YYYY-MM: <https://…>

## Tools

<!--
Format: Name - <URL> or Name (module) - <URL>, one tool per paragraph.
URL = the tool's main page (for download), not the source code of a module.
Only free tools (open source or free to use), no commercial ones.
Only tools that decode the artifact; format detection or generic viewers are not enough.
No version details. The only allowed addition: (old versions only), if the tool is no longer
developed and only handles older versions of the artifact.
-->

Name - <https://…>
