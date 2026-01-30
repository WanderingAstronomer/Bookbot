# BookBot 🚀

**BookBot** is a small CLI project from a Boot.dev exercise that analyzes a plain-text book and prints a concise report:

- total word count
- per-character frequency (lowercased), sorted from most to least common

## Features ✅

- Read a book from `books/frankenstein.txt` (or another text file)
- Count words and characters
- Print a formatted report showing word count and the most common characters
- No external dependencies — pure Python

## Quickstart 🔧

1. Ensure you have Python 3 installed.
2. From the project root, run:

```bash
python3 main.py
```

You should see output similar to:

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
... (trimmed for brevity)
============= END ===============
```

## Project layout 🗂️

- `main.py` — CLI entrypoint, orchestrates reading, counting and printing the report
- `stats.py` — pure functions:
  - `get_book_as_str(path: str) -> str`
  - `get_words(book_string: str) -> list`
  - `get_wordcount(words: list) -> int`
  - `get_char_count(book_string: str) -> dict` (returns lowercased char -> count)
  - `sort_dict(char_counts: dict) -> list` (returns list of `{"char":..., "num":...}` sorted by `num` desc)
- `books/frankenstein.txt` — sample book used for the exercise

## Tests 🧪

This project includes CLI tests used by the Boot.dev environment. Run a test with the provided test id:

```bash
bootdev run <test-id> -s
```

If the printed report matches the expected output, the tests should pass.

## Notes & tips 💡

- The code intentionally skips non-alphabetic characters when printing the character section (uses `str.isalpha()`).
- Use `encoding="utf-8"` when reading files if you expect accented characters.
- The implementation favors small, composable functions to make testing and reasoning easy.

---

**Author:** Andrew Brown
