---
title: "SQLite Databases"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
---

# SQLite Databases

## Description

SQLite is a relational "single-file" database system in the form of an embedded, serverless library. It is frequently used by applications (e.g. web browsers and messengers) to store data.
Translate Windows pages into English

The language for definition and querying is SQL. SQLite implements its own dialect with some deviations from the standard (e.g. dynamic typing / type affinity, limited `ALTER TABLE`).

## Key facts

### File types/components

#### Database file

The database file contains both the schema of the database and most of the active data (further data may be in rollback journals or the WAL).

The database file consists of tables and indexes, which are organised as B-trees (tables as B+ trees, i.e. the actual data is only in the leaf pages; indexes as B-trees). A B-tree is not a binary tree. The smallest unit is the page. The page size is a power of two between 512 and 65536 bytes; since SQLite 3.12.0 (2016) the default is 4096 bytes, older databases often use 1024 bytes. A B-tree page only ever contains data from one table or one index. A table/an index can, however, be spread over several pages.

The first page contains a 100-byte header with information about the database. Among other things, the following information can be taken from the header:

- Format signature "SQLite format 3\0" (offset 0) – this is not a version number
- SQLite version that last wrote to the file (offset 96)
- Page size (offset 16)
- Use of rollback journal or WAL (offset 18/19: 1 = legacy/rollback journal, 2 = WAL)
- File change counter (offset 24)
- Size of the database in pages (offset 28; only valid if the value at offset 92 matches the file change counter)
- First freelist trunk page (offset 32) and number of freelist pages (offset 36)
- Auto-vacuum setting (offset 52/64)
- Encoding (offset 56)
- user_version (offset 60) and application_id (offset 68) – can help to attribute the file to an application

In addition, the first page always holds the root page of the table `sqlite_master` (since 3.33.0 also called `sqlite_schema`). For extensive schemas, it is itself a B-tree spanning several pages. It contains the schema of the database, the root pages per table and index, and the definitions of views and triggers.

Besides the B-tree pages, further page types can exist:

- Overflow pages: continuation of records that do not fit into one page
- Freelist pages (trunk and leaf pages): pages that are no longer part of the current B-tree structure, e.g. because they became empty through deletion or a table/an index was dropped
- Pointer map pages: only with auto_vacuum enabled
- Lock-byte page: only for databases larger than 1 GiB

##### Forensic value

The database file contains the schema and therefore serves to interpret the data. In WAL mode, current data may still be exclusively in the WAL – the database file alone then does not necessarily show the current state.

Deleted entries can possibly be reconstructed from the database file itself:

- Freeblocks within a page: the first 4 bytes of a deleted cell are overwritten by the freeblock header, so the start of the record (payload length, rowid, parts of the record header) is usually missing.
- Unallocated area within a page (between the cell pointer array and the cell content area)
- Freelist pages

Prerequisites:

- `secure_delete` = OFF: all three sources can contain old data
- `secure_delete` = FAST (since 3.20): old data in B-tree pages is overwritten, but freelist pages remain untouched
- `secure_delete` = ON: old data is overwritten
- For freelist pages additionally: `auto_vacuum` != FULL (with FULL, freelist pages are truncated at commit) and no manual `VACUUM` (rebuilds the file completely)

The difficulty of interpretation lies in the fact that for freelist pages a reliable attribution to the original table must be possible, as the page is no longer part of the B-tree structure. For this, content and structure (e.g. number and types of the columns in the record header) have to be considered.

For tables with `AUTOINCREMENT`, `sqlite_sequence` stores the highest rowid ever assigned. If this value is greater than the highest existing rowid, or if the table has gaps in the rowid sequence, this indicates deleted entries (gaps can, however, also be caused by aborted transactions).

#### Rollback journal

Location:

- Same directory as the database file
- Name identical to the database file with the suffix "-journal"

##### How it works

The rollback journal serves to ensure the integrity of the database in the event of, for example, a system crash. To achieve this, the procedure is as follows, for example:

1. The original content of the page to be changed/deleted is copied from the database into the journal, and the journal is written to disk.
2. The change/deletion is written to the database.
3. Commit: the journal is invalidated (depending on the journal mode DELETE/TRUNCATE/PERSIST, see below). This makes clear that the change has been written completely.

A journal that is still valid after a crash or abort and must be rolled back at the next opening is called a "hot journal".

##### Forensic value

The journal contains the page contents before the change. What remains of it after the commit depends on the journal mode:

- DELETE (default): the journal file is deleted.
- TRUNCATE: the journal file is truncated to 0 bytes.
- PERSIST: only the journal header (incl. magic) is overwritten with zeros. The pages remain in the file (possibly limited by `journal_size_limit`).

With DELETE and TRUNCATE, the data is no longer allocated. Recovery is only possible via the file system. With PERSIST, the data can be read directly from the journal, independently of the file system.

This may make it possible to reconstruct earlier database states.

#### Rollback master journal (super-journal)

Officially called "super-journal" since SQLite 3.33.0 (2020).

The super-journal serves for coordination when several databases (connected via `ATTACH`) are changed within one transaction. It is only used if the databases are not operated in WAL mode.

Location:

- Same directory as the main database
- Name identical to the main database with the suffix "-mj" + 9 hex characters (according to the SQLite source code, the 7th character is always "9")

##### How it works

The super-journal contains the paths of all rollback journals involved, each separated by a NUL byte. Conversely, each rollback journal involved contains the name of the super-journal at its end. After a successful commit, the super-journal is deleted.

##### Forensic value

If a super-journal exists, you know that a cross-database transaction was not completed. Its content shows which databases the changes relate to. The respective rollback journals of the databases then show which changes were to be made.

#### Write-ahead log (WAL)

Location:

- Same directory as the database file
- Name identical to the database file with the suffix "-wal"

##### How it works

The write-ahead log has the same goal as the rollback journal but works the other way round: changes are not written directly to the database but are first appended to the WAL as complete page copies.

The WAL consists of a 32-byte header (including two salt values) and frames. Each frame consists of a 24-byte frame header and a complete page. A frame that completes a transaction (commit frame) can be recognised by the database size field in the frame header being non-zero.

1. Pages to be changed/deleted/added are written to the WAL as frames.
2. The transaction is confirmed in the WAL (commit frame).
3. Further pages are changed/deleted/added.
4. The transaction is confirmed in the WAL (commit frame).
5. At the checkpoint, the changes are transferred to the database file. Triggers are:
   1. Automatically, as soon as the WAL reaches 1000 frames (default, `wal_autocheckpoint`). The checkpoint is carried out at the commit that exceeds this limit.
   2. Explicitly via `PRAGMA wal_checkpoint` or the corresponding API function.
   3. When the last database connection is closed cleanly. The WAL is usually deleted in the process (exception: persistent WAL). A crash or killing the app does not trigger a checkpoint; the WAL then remains and is taken into account at the next opening.

After a complete checkpoint, the WAL is rewritten from the beginning at the next write operation. New salt values are set in the WAL header. By default, the file is not truncated (exception: `journal_size_limit` is set).

##### Forensic value

As long as the WAL exists, older frames remain in the file after a checkpoint until they are overwritten. Frames whose salt values do not match the current WAL header come from earlier runs. If the WAL was deleted (clean close), recovery is only possible via the file system.

Older frames contain older versions of a page. Old database states can therefore be reconstructed even if `secure_delete` is active.

The WAL can even contain entries that were never in the database file. Example: a message arrives and is deleted before the next checkpoint.

Timelines can only be reconstructed if the data itself contains timestamps.

#### Shared memory file (shm)

Location:

- Same directory as the database file
- Name identical to the database file with the suffix "-shm"

##### How it works

Serves as an index (wal-index) of the frames in the WAL in order to find the last valid version of a page faster. A new frame in the WAL leads to a new entry in the shm. The shm is not crash-safe, is stored in the native byte order of the system and can be rebuilt from the WAL at any time. In the mode `locking_mode=EXCLUSIVE`, no shm file is created.

##### Forensic value

The forensic value is low, as the index data of the shm can also be obtained from the WAL and the shm only exists as long as the WAL. Helpful are the values `mxFrame` (last valid frame) and `nBackfill` (up to which frame a checkpoint has already taken place) for classifying which frames are current.

## Analysis checklist

- [ ] **Acquisition:** secure the database file, `-wal`, `-shm` and `-journal` together.
- [ ] **Only work on copies.**
- [ ] **Check companion files and header:** which files exist (size, timestamps)? Read the page size, journal/WAL use and number of freelist pages from the header.
- [ ] **Analyse the schema:** check tables, indexes, views and triggers in `sqlite_master` to understand where which data ends up.
- [ ] **Compare DB vs. DB+WAL state:** open one copy without and one with the WAL.
  - Pitfall: the comparison only shows the differences of the final states. Intermediate states within the WAL require an analysis of the individual frames.
- [ ] **Check old data:** freeblocks, unallocated areas, freelist pages, old WAL frames, journal pages. Normal SQL queries only show active data.

## References

2026-05: [beBinary: What Hides in the WAL – SQLite Forensics with crush](https://bebinary4n6.blogspot.com/2026/05/what-hides-in-wal-sqlite-forensics-with.html)

2025: [Lee et al.: Survey of techniques for recovering deleted SQLite records (FSI: Digital Investigation)](https://www.sciencedirect.com/science/article/abs/pii/S2666281725001714)

2022: [Mobile Forensics – The File Format Handbook, chapter 5: SQLite (Springer, open access)](https://doi.org/10.1007/978-3-030-98467-0_5)

2021-07: [SANS/GIAC: Missing SQLite Records Analysis](https://www.sans.org/white-papers/40195)

2018: Extensive explanations of the structure and internal workings in the book "SQLite Forensics" by Paul Sanderson - ISBN 9781980293071

2015-03: [Sanderson Forensics: Forensic examination of SQLite WAL files](https://sqliteforensictoolkit.com/forensic-examination-of-sqlite-write-ahead-log-wal-files/)

[Belkasoft: SQLite Forensics with Belkasoft X)](https://belkasoft.com/sqlite)

SQLite documentation:
- File format: <https://www.sqlite.org/fileformat2.html>
- WAL index and locking: <https://www.sqlite.org/walformat.html>
- Journal modes: <https://www.sqlite.org/pragma.html#pragma_journal_mode>

crush format reference:
- <https://kalink0.github.io/crush-forensics/formats/de/sqlite/>
- <https://kalink0.github.io/crush-forensics/formats/de/sqlite-journal/>
- <https://kalink0.github.io/crush-forensics/formats/de/sqlite-wal/>

## Tools

crush - <https://github.com/kalink0/crush-forensics>

DB Browser for SQLite - <https://sqlitebrowser.org/>

DBeaver Community - <https://dbeaver.io/>

fqlite - <https://github.com/pawlaszczyk/fqlite>

SQBite - <https://github.com/SpyderForensics/SQLite_Forensics/tree/main/SQBite>

sqlite-dissect - <https://github.com/dod-cyber-crime-center/sqlite-dissect>

sqlite-gui-analyzer - <https://github.com/akhil-dara/sqlite-gui-analyzer>
