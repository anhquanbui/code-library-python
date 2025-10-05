# Git Quick Commands & Troubleshooting (for my workflow)

A concise, **English-only** cheat sheet of important Git commands and the exact pitfalls I hit recently, plus fixes.

---

## 1) Daily essentials

```powershell
# Where am I and what changed?
git status
git branch -vv
git remote -v

# Stage & commit everything
git add -A
git commit -m "Update"

# Sync with remote (avoid non-fast-forward merge commits)
git pull --rebase origin main

# Push (after first push with -u, see below)
git push
```

---

## 2) First-time setup (new repo or new machine)

```powershell
git init
git branch -M main
git remote add origin https://github.com/<username>/<repo>.git

# add something then:
git add -A
git commit -m "Initial commit"

# first push sets upstream so later just 'git push'
git push -u origin main
```

---

## 3) Typical errors I encountered (and fixes)

### A) `fatal: No configured push destination`
**Cause:** no remote set.  
**Fix:**
```powershell
git remote add origin https://github.com/<username>/<repo>.git
git push -u origin main
```

### B) `error: src refspec main does not match any`
**Cause:** branch `main` doesn't exist _or_ no commits yet.  
**Fix:**
```powershell
git add -A
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```

### C) `non-fast-forward` (push rejected, branch is behind remote)
**Preferred fix (keep both sides clean):**
```powershell
git pull --rebase origin main
# resolve conflicts if any:
#   edit files -> remove <<<<<<< ======= >>>>>>>
git add <fixed-file>
git rebase --continue
git push
```
**Only if you intentionally want to overwrite remote history:**
```powershell
git push --force-with-lease origin main
```

### D) “Everything up-to-date” but the file isn’t on GitHub
**Cause:** the change wasn’t committed (file is `U` or `M` only locally), **or** you pushed in the wrong repo/folder, **or** it’s ignored by `.gitignore`.  
**Fix checklist:**
```powershell
git status                 # must show files staged/committed
git add -A
git commit -m "Add files"
git push

# check .gitignore if the file pattern is ignored (e.g., *.ipynb)
# to unignore a specific file:
#   !python_tips.ipynb
```

### E) Deleted file showing `D` (and you want it back)
```powershell
# if not staged yet:
git restore <path>

# if already staged as deleted:
git restore --staged <path>
git restore <path>
```

### F) Wrong directory / nested repo vs parent repo
- Make sure you run Git commands **in the repo that actually tracks the files**:
```powershell
cd "D:\Code python\code-library-python"
git status
```
- VS Code badges: **U**=Untracked, **M**=Modified, **A**=Added (staged), **D**=Deleted.

### G) Submodule confusion (folder tracked as a separate repo)
**Symptoms:** `modified: <folder> (modified content, untracked content)` or GitHub shows folder as a repo link.  
**Detect:**
```powershell
# in the parent repo
dir .gitmodules             # exists?
git submodule status
git ls-files -s <folder>    # shows 160000 mode for submodule
```
**Convert submodule -> normal folder (Windows PowerShell):**
```powershell
# parent repo root
git rm --cached <folder>         # remove submodule from index (keeps files)
if (Test-Path .gitmodules) { del .gitmodules }

# remove nested .git so it's no longer a repo inside
cd <folder>
rmdir /S /Q .git
cd ..

git add <folder>
git commit -m "Convert submodule to regular folder"
git push
```

---

## 4) Moving/renaming files safely (keep history)
```powershell
git mv OLD_PATH NEW_PATH
git commit -m "Move file"
git push
```

---

## 5) Helpful diagnostics
```powershell
git log --oneline --graph --decorate --all
git diff                          # unstaged changes
git diff --staged                 # staged vs last commit
git show <commit>                 # inspect a commit
```

---

## 6) Notes for notebooks & README
- If `*.ipynb` is in `.gitignore`, the notebook won’t be tracked. Add an exception:
  ```
  !python_tips.ipynb
  ```
- Moving `README.md` from root to a subfolder removes the root README preview on GitHub.  
  Keep a short README at root if you want a repo landing page.

---

## 7) Quick mental model
- **Working tree** → your files (show as U/M/D).  
- **Index (staging)** → what will be committed (`git add`).  
- **HEAD (commit)** → history.  
- Push = send commits; **uncommitted files never get pushed**.

---

## 8) Short “first aid” flow
1. `git status`
2. If U/M → `git add -A && git commit -m "msg"`
3. `git pull --rebase origin main`
4. Fix conflicts → `git add` → `git rebase --continue`
5. `git push`

That’s it — copy/paste friendly and tailored to the issues I actually ran into.