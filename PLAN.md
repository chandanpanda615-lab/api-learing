# 3-Day Learning Plan: REST API + Git (for use with Gemini)

> **How to use this file:** Paste one "Session" block at a time into Gemini.
> Do the steps in order. Do not skip the "Explain back" step — that is the
> whole point. When you can explain a concept in your own words without help,
> tick its box and move on.

---

## Who is learning (tell Gemini this first)

- CA finalist, doing articleship. Beginner at code. **Does not know Python syntax.**
- **Goal:** read an API script and judge if it is correct, safe and complete —
  NOT to write code from a blank page.
- **Method (important):** the AI writes all code. The learner reads it, predicts
  the output *before* running, explains it back, and finds planted bugs.
- Use **simple English** and **accounting examples** (vouchers, invoices, GST,
  NetSuite). If the learner is wrong, ask a guiding question — do not hand over
  the answer.
- Budget: ~1–2 hours per day.

**Paste-to-Gemini opener:**
> "I am a CA finalist learning REST APIs and Git. I do not know Python syntax.
> Teach me input-based: you write the code, I predict the output and explain it
> back, and you give me broken versions to fix. Use simple English and
> accounting examples. When I'm wrong, ask me a guiding question instead of
> giving the answer. Today's topic is: ______."

---

## The files this plan uses (already in your folder)

| File | What it is |
|---|---|
| `Jobs.py` | Calls a job-portal API, saves the reply to `all_jobs.json` |
| `test_api.py` | Sends a PATCH request to update a profile |
| `count_links.py` | Reads the JSON, counts how many jobs have a real link |
| `create_csv.py` | Turns the JSON into `jobs_report.csv` |
| `all_jobs.json` | The saved API reply (100 jobs) |

⚠️ **Real problem to fix on Day 1:** `Jobs.py` and `test_api.py` have your
**live API key and login token pasted straight into the code.** That token is
your identity on that website. This is a real security mistake — and the perfect
first lesson.

---

## DAY 1 — Secrets: stop leaking your token

**Concept goal (R9 + G6):** understand why a key must never live inside code,
and fix your own real leak.

### 1. Concept (no code yet)
Ask Gemini to explain, with an accounting analogy:
- What is an API key vs a Bearer token? (Hint: key = "which company is calling",
  token = "which logged-in person is calling".)
- Why is a hardcoded token like leaving your **digital signature / DSC PIN**
  written on a voucher that anyone can photocopy?
- What is the difference between **401** ("I don't know who you are") and
  **403** ("I know you, but you're not allowed")?

### 2. Predict
Ask Gemini: *"If I push `Jobs.py` to a public GitHub repo with the token still
inside, what exactly can a stranger do, and for how long?"* Write your guess
first, then let Gemini correct it.

### 3. Do (Gemini writes the code, you read it)
Ask Gemini to:
1. Show you how to make a `.env` file that holds the API key and token.
2. Rewrite `Jobs.py` and `test_api.py` so they **read** the secret from `.env`
   using `os.environ` / `python-dotenv`, instead of pasting it.
3. Show a `.gitignore` file that lists `.env`.

For each new line of code, predict what it does before Gemini explains it.

### 4. Explain back — tick when you can answer without help
- [ ] Why does the token belong in `.env` and not in `Jobs.py`?
- [ ] What does `.gitignore` do, and why must `.env` be in it?
- [ ] A key was pushed by mistake, then deleted in the next commit. Is it safe
      now? (Answer: no — old commits still hold it. It must be **revoked/rotated**.)
- [ ] Difference between 401 and 403, in your own words.

### 5. Find the bug
Ask Gemini for a version where `.env` exists but the code still fails
(e.g. wrong variable name, or `.env` not loaded). Find why it breaks.

---

## DAY 2 — Git: give this folder a memory

**Concept goal (G1–G3):** snapshots, the two-step save, and reading history.
You have 10 files and zero version history — fix that.

### 1. Concept (no code yet)
Ask Gemini:
- What is a **commit**? (Analogy: closing and dating a set of working papers —
  a snapshot of the exact state, not an average over a period.)
- Why two steps — `git add` then `git commit`? (Analogy: `add` = pick which
  vouchers go in this batch; `commit` = staple and file the batch.)

### 2. Predict
Before running anything, predict the output of `git status` in the folder
*right after* `git init` but *before* any `add`. Then check.

### 3. Do (you run these; Gemini explains each)
1. `git init`
2. `git status`  ← read every line with Gemini
3. Make sure `.env` is in `.gitignore` (from Day 1) — confirm it does NOT show up
4. `git add .`
5. `git commit -m "First snapshot: API learning scripts"`
6. `git log`  ← read it
7. Change one line in any file, then `git diff`  ← read it

### 4. Explain back — tick when you can answer without help
- [ ] What is inside the `.git` folder, and did `git init` take a snapshot by itself?
      (Answer: no — `init` only sets up the mechanism; the commit is the manual save.)
- [ ] In your own words: what does `git add` do that `git commit` does not?
- [ ] Reading a `git log` entry — what is the long hash, the author, the date, the message?
- [ ] What does `git diff` show, and when would you use it before a commit?

### 5. Find the bug
Ask Gemini: *"I edited a file but `git commit` says 'nothing to commit'. Why?"*
Explain what step was missed.

---

## DAY 3 — Backfill: explain the API code you already wrote

**Concept goal (R2, R3, R4, R6):** you already *used* HTTP, JSON and pagination
in `Jobs.py`. Today you prove you can *explain* them. This is the core skill —
judging a script you did not write.

### 1. The HTTP request (R2) — use your own `Jobs.py`
Open `Jobs.py` with Gemini and point to:
- [ ] the **method** (GET), the **URL**, the **headers**, the **params**
- [ ] Why does this GET have **no body**, but `test_api.py`'s PATCH **does**?

### 2. The HTTP response (R3)
- [ ] What do **200, 201, 400, 401, 403, 404, 422, 500** mean? Which are the
      *client's* fault and which are the *server's*?
- [ ] Ask Gemini to add `print(response.status_code)` to `Jobs.py`. Predict the
      number before running.

### 3. JSON (R4) — use your `all_jobs.json`
- [ ] Point to one **object** `{ }` and one **list** `[ ]` in the file.
- [ ] Describe one job as JSON in words (Company, Location, Salary, is_exclusive).
- [ ] Ask Gemini for a *broken* JSON snippet (missing comma or bracket). Find the error.

### 4. Pagination (R6) — the part you already hacked
In `Jobs.py` the params include `offset` and `limit`.
- [ ] What do `offset` and `limit` do? (Analogy: "show me 100 vouchers starting
      from row 0".)
- [ ] Predict: if you set `limit` to `10`, how many jobs land in `all_jobs.json`?
- [ ] Why do real APIs force pagination instead of sending everything at once?

### 5. Read-and-review test (the real goal)
Ask Gemini for a **short unfamiliar API script with 3 planted problems**
(e.g. a missing `timeout`, a hardcoded token, a wrong status-code check).
In 10 minutes, tell Gemini:
1. What the script does
2. What could break
3. What is unsafe

Finding **2 of 3** = you're ready to move past the basics.

---

## After these 3 days — where the full plan continues

The complete concept ladder (R7–R13 REST, G4–G11 Git: reading `requests` code
line by line, timeouts/retries, building a tiny FastAPI server, validation,
branches, pull requests, GitHub-as-an-API) is kept below for later. Come back to
it once Days 1–3 are ticked off.

---

## Status

| Field | Value |
|---|---|
| Plan rewritten | 2026-09-28 — 3-day Gemini plan |
| Day 1 (Secrets / .env) | [ ] not started |
| Day 2 (Git init + history) | [ ] not started |
| Day 3 (Explain HTTP/JSON/pagination) | [ ] not started |
| Real risk open | ⚠️ live token still in `Jobs.py` and `test_api.py` — fix Day 1 |

---

## Full concept ladder (reference for after Day 3)

### Track R: REST API
- R1 Client and server · R2 The HTTP request · R3 The HTTP response · R4 JSON
- R5 REST rules (GET/POST/PUT/PATCH/DELETE, idempotency, nouns not verbs)
- R6 URL parts (path vs query params, pagination) · R7 Reading `requests` code
- R8 Errors, timeouts, retries · R9 Authentication and secrets
- R10 The server side (a mini FastAPI + SQLite journal-entry API)
- R11 Validation (why the server rejects debit ≠ credit) · R12 Evaluating code
- R13 The real world (rate limits/429, webhook vs polling, OpenAPI docs)

### Track G: Git and GitHub
- G1 Snapshots · G2 Staging area · G3 History · G4 Local vs remote
- G5 Push/pull/fetch/clone · G6 .gitignore and secrets · G7 Branches
- G8 Merge and conflicts · G9 Pull Requests · G10 Undo safely (revert vs reset)
- G11 Bridge: GitHub is a REST API

### Final test
Given an unfamiliar API script, explain in 15 minutes, without help:
1. What it does · 2. What could break · 3. What is unsafe
