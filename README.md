# CZU Prague — ETE2AE Exam Prep Portal

Welcome to the CZU Prague IT / ETE2AE Exam Preparation Portal. This portal is a client-side suite of interactive dashboards, simulators, active recall flashcards, and automated checkers designed to help students study for and pass the final exams.

> [!NOTE]
> **Active Target Status**:
> The user has successfully passed all other modules (OS, Markup, ORSA, Math, Stats). The portal has been configured to **focus exclusively on Information Systems (INFOA5 / ETEA7E / ETE2AE)** as the active target, with other subjects visually marked as completed.

---

## 📊 Information Systems Study Suite

The Information Systems suite consists of four fully integrated components cross-referenced with a glassmorphic global navigation bar for seamless jumping:

1. **📊 Full Dashboard (`IS_EXAM_SUITE/index.html`)**
   - Active recall study tools, categories filtering, interactive questions, and a global TTS (Text-to-Speech) audio player that reads cards aloud for passive studying.
2. **🚀 2-Hour Master Guide (`IS_EXAM_SUITE/EXAM_MASTER_2H.html`)**
   - A rapid exam cram-sheet containing the core definitions and the official 50 practice questions, with inline self-checks and automated mock testing. It is dynamically generated using `IS_EXAM_SUITE/generate_is_master.py`.
3. **⚡ 2-Hour Blitz (`IS_EXAM_SUITE/EXAM_BLITZ_2HR.html`)**
   - A highly focused study guide containing 42 high-yield exam-specific concepts (SDLC, BPR, SAP modules, T-codes, CIA triad, ACID database properties, cloud service models).
4. **🃏 3D Cram Cards (`IS_EXAM_SUITE/smart_cram_cards.html`)**
   - A 3D flip-card study application with keyboard hotkeys (Left/Right arrows, Spacebar) for rapid spaced-repetition training.

---

## 📥 Anki Study Decks

The study decks are fully synchronized and available for direct import into Anki (located in `IS_EXAM_SUITE/anki_decks/`):

- **Moodle Dump Deck (50 Cards)**
  - `IS_Anki_Deck.txt` (Beautiful HTML cards containing category badges and descriptions)
  - `is_exam_suite_cards.txt` (Plain text tab-separated format: `Front[TAB]Back[TAB]Tag`)
  - `is_exam_suite_cards_cram.txt` (Plain text with quick-recall cram tags)
- **High-Yield Blitz Deck (42 Cards)**
  - `IS_High_Yield_Blitz_Anki_Deck.txt` (Beautiful HTML cards targeting core concepts)
  - `is_high_yield_blitz_cards.txt` (Plain text tab-separated format)

### How to Import to Anki:
1. Open Anki on your desktop or mobile device.
2. Go to **File > Import...**
3. Select one of the deck files (e.g. `IS_Anki_Deck.txt`).
4. Anki will automatically configure the fields based on tabs. Make sure to check **Allow HTML in fields** for the HTML decks.

---

## 🚀 Automated Deployment with GitHub Pages

The repository has been configured with a automated GitHub Actions deployment workflow at `.github/workflows/pages.yml`.

### How it works:
- On every push to the `main` or `master` branches, the GitHub Action automatically:
  1. Sets up Python.
  2. Runs `python IS_EXAM_SUITE/generate_is_master.py` to compile the latest `EXAM_MASTER_2H.html` from the source database.
  3. Runs `python IS_EXAM_SUITE/anki_decks/generate_anki_decks.py` to rebuild and synchronize all Anki deck files.
  4. Publishes the entire static folder to **GitHub Pages**, ensuring the hosted study website is always up to date with the latest commits.

---

## 💻 Running Locally

Since the entire application is built using client-side vanilla HTML, CSS, and JS, you can run it locally by opening the root `index.html` file in any modern web browser, or serve it with a local server:

```bash
# Using Python's built-in HTTP server
python -m http.server 8000
```
Then open `http://localhost:8000` in your browser.
