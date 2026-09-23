# luce-textmate

Loads TextMate grammars (`.tmLanguage.json`) and tokenizes source a line at a time into scoped
spans, so an editor can color any language by dropping in its grammar file. It matches with
luce-regex and depends only on that plus the standard library.

The package parses grammar JSON with its own small reader that builds Luce values (objects,
arrays, strings), because it needs to hold the parsed tree — the standard JSON decoder hands back
borrowed cursors that a Luce program cannot keep.

Status: M2 in progress. `json` (the reader) is in; the grammar model and line tokenizer follow.
