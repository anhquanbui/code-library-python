# Long vs Short Cheat Sheet (Git & Python)

_Quick reference of verbose (long) vs concise (short) ways to write common commands and code._  
_Last updated: 2025-10-05 23:05:49_

---

## Git — Long vs Short

> Tip: These work best after you've set upstream (`git push -u origin main`).

| Purpose | Long form | Short / Common |
|---|---|---|
| First push & set upstream | `git push --set-upstream origin main` | `git push -u origin main` |
| Pull with rebase | `git pull --rebase origin main` | `git pull -r` (if upstream set) |
| Push force (prefer safe) | `git push --force-with-lease` | `git push -f` *(unsafe)* |
| Show status (compact) | `git status` | `git status -sb` |
| Create & switch branch | `git checkout -b feature/x` | `git switch -c feature/x` (modern) |
| Switch to branch | `git checkout main` | `git switch main` |
| Move/rename branch to `main` | `git branch -M main` | *(no shorter flag)* |
| Stage all changes | `git add --all` | `git add -A` or `git add .` |
| Commit with message | `git commit --message "msg"` | `git commit -m "msg"` |
| Commit tracked changes | `git commit -a -m "msg"` | *(same; just note `-a` skips new files)* |
| Diff staged | `git diff --staged` | `git diff --cached` (alias) |
| Show pretty log | `git log --oneline --graph --decorate --all` | alias: `git lg` → `log --oneline --graph --decorate --all` |
| Restore deleted file | `git checkout -- file` (legacy) | `git restore file` (modern) |
| Unstage a file | `git reset HEAD file` (legacy) | `git restore --staged file` (modern) |
| Set remote URL | `git remote set-url origin <url>` | *(no shorter flag; define alias if needed)* |

**Notes**
- `git push -f` overwrites remote; prefer `--force-with-lease` to avoid clobbering others' work.
- Once upstream is set, `git pull` ≈ `git pull origin <your-branch>` and `git push` ≈ `git push origin <your-branch>`.

---

## Python — Long vs Short

### Lists & Loops
| Task | Long form | Short form |
|---|---|---|
| Build list of squares | `out=[];\nfor x in nums:\n    out.append(x*x)` | `[x*x for x in nums]` |
| Filter evens | `out=[];\nfor x in nums:\n    if x%2==0:\n        out.append(x)` | `[x for x in nums if x%2==0]` |
| Map + Filter | `out=[];\nfor x in nums:\n    if x>0:\n        out.append(x*2)` | `[x*2 for x in nums if x>0]` |
| Iterate with index | `for i in range(len(a)):\n    v=a[i]` | `for i, v in enumerate(a):` |
| Reverse list | loop / `reversed(a)` | `a[::-1]` |

### Assignment & Conditionals
| Task | Long form | Short form |
|---|---|---|
| Swap variables | `tmp=a; a=b; b=tmp` | `a, b = b, a` |
| Conditional assign | `if cond: x=a\nelse: x=b` | `x = a if cond else b` |
| Provide default | `if not name: name="Guest"` | `name = name or "Guest"` |
| Count items by condition | `cnt=0;\nfor x in xs:\n    if pred(x): cnt+=1` | `cnt = sum(1 for x in xs if pred(x))` |
| Any/All flags | loop with break | `any(flags)`, `all(flags)` |

### Strings
| Task | Long form | Short form |
|---|---|---|
| Format string | `"Hello, %s" % name` / `str.format()` | `f"Hello, {name}"` |
| Join pieces | loop + `+=` | `" ".join(parts)` |
| Repeat string | loop | `"ha" * 3` |

### Dicts
| Task | Long form | Short form |
|---|---|---|
| Safe lookup with default | `x=d["k"] if "k" in d else 0` | `x = d.get("k", 0)` |
| Iterate keys & values | `for k in d.keys(): v=d[k]` | `for k, v in d.items():` |
| Invert dict | loop append | `{v: k for k, v in d.items()}` |

### Files
| Task | Long form | Short form |
|---|---|---|
| Read file | `f=open(p); data=f.read(); f.close()` | `with open(p) as f: data=f.read()` |
| Append line | manual open/close | `with open(p, "a") as f: f.write("line\n")` |

### Misc
| Task | Long form | Short form |
|---|---|---|
| Build set from list | `s=set();\nfor x in xs: s.add(x)` | `s = set(xs)` |
| Flatten nested list | nested loops | `[x for sub in nested for x in sub]` |
| Path joins (Windows-safe) | `os.path.join("a","b")` | `from pathlib import Path; Path("a")/"b"` |

---

## Tips
- Favor readability: short form is great if it remains clear.
- Be consistent with naming and structure.
- For Git, define helpful aliases like:  
  `git config --global alias.lg "log --oneline --graph --decorate --all"`  
  `git config --global alias.st "status -sb"`
