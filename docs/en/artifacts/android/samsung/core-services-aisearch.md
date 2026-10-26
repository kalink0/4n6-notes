---
title: "Samsung Core Services - AISearch"
status: complete
completed: 2026-10-26
authors: [kalink0 (Marco Neumann)]
translation: machine
translation_of: de
topics: [file-existence]
---

# Samsung Core Services - AISearch

## Meaning

Samsung Core Services (com.samsung.android.scs) is a system component without its own user interface that provides basic functions for Samsung apps. The AI Search module indexes content on the device so that it can be found via search. For this, it extracts the text of documents and stores it.

From a digital forensics perspective, a text file in the index shows that a document with the given file name and this text content was present on the device for the given user and was indexed.

## Key facts

1. The extracted full text is stored per document as a text file in **`raw_txt/`**, confirmed for PDF files
2. File name of the text file: **`{USER_ID}_{FILE_ID}_{FILE_NAME}.txt`**; user ID 0 = main user, 150 = Secure Folder
3. Only the file name at the time of indexing is stored, not the original location
4. The text of deleted documents is retained (observed approx. 2 weeks after deletion)
5. The timestamp of the text file roughly corresponds to the time of indexing, not to the creation of the original
6. Location:  
   **`/data/data/com.samsung.android.scs/files/aisearch/`**

## References

2025-12: <https://bebinary4n6.blogspot.com/2025/12/samsung-core-services-module-ai-search.html>

## Tools

*No content yet.*
