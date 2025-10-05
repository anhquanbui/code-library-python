# Python Code Tips of the Day

A compact collection of practical Python snippets you can rehearse every morning.
Each tip is short, memorable, and runnable in the companion notebook.

_Last updated: 2025-10-05 17:45:41_

------

## Quick Start

1. **Open the notebook** `python_tips.ipynb` and run cells from top to bottom.
2. Optionally copy any snippet into your own project (they are dependency‑free).
3. Come back tomorrow and re‑run a few different tips as a daily warm‑up.

---

## Tips Overview

### A. Core Language
- **Swap two variables** with tuple unpacking: `a, b = b, a`
- **Multiple assignment** in one line: `x, y, z = 1, 2, 3`
- **Truthiness** for emptiness checks: `if not items:`
- **Enumerate** with index and value: `for i, v in enumerate(seq): ...`
- **Slicing** for reverse: `seq[::-1]`

### B. Lists & Iteration
- **Comprehensions** for build + filter: `[x**2 for x in range(10) if x % 2 == 0]`
- **Flatten** a nested list: `[x for sub in nested for x in sub]`
- **Zip** to iterate in lockstep: `for a, b in zip(A, B): ...`

### C. Dictionaries
- **Safe lookup**: `d.get("key", default)`
- **Iterate keys & values**: `for k, v in d.items(): ...`
- **Invert dict** (if values are hashable & unique): `inv = {{v: k for k, v in d.items()}}`

### D. Strings
- **f-strings**: `f"Hello, {{name}}!"`
- **Join** pieces: `sep.join(parts)`
- **Repeat** strings: `"ha" * 3  # 'hahaha'`

### E. Numbers & Logic
- **any / all**: `any(flags)`, `all(flags)`
- **Defaulting with or**: `name = user_input or "Guest"`

### F. Functional-ish
- **Lambda** for a tiny function: `lambda x: x + 1`
- **map / sorted with key**: `sorted(items, key=lambda x: x.score, reverse=True)`
- `*args / **kwargs` for flexible APIs

### G. Files
- **Read file**: `with open("file.txt") as f: data = f.read()`
- **Append file**: `with open("log.txt", "a") as f: f.write("line\n")`

---

## How to Practice Daily (2–5 minutes)

- Pick 3 random tips and **rewrite them from memory**.
- Add a very small twist (e.g., filter then map, or print formatted output).
- Time-box to 5 minutes — momentum over perfection.

---

## Notebook Index

The notebook contains one cell (or more) per tip:

1. Swap variables, multiple assignment, slicing
2. Truthiness, emptiness checks, enumerate
3. List comprehensions (build + filter)
4. Flatten nested lists
5. Zip iteration
6. Dict get()/items(), invert dict
7. f-strings, join, repeat
8. any() / all(), defaulting with `or`
9. lambda, map(), sorted(key=...)
10. *args and **kwargs basics
11. File read/write minimal patterns

> Tip: Open the notebook and run the top cell to see the Python version and timestamp.

---

## License

Public domain / CC0-like intent. Use in projects, classes, or internal wikis.
Contributions welcome: add your own favorite tip as a new cell.
