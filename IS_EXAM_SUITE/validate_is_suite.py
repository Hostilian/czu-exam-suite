# -*- coding: utf-8 -*-
import os
import sys
import re
import subprocess

# Ensure UTF-8 output if supported
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass
if sys.stderr.encoding != 'utf-8':
    try:
        sys.stderr.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

print("======================================================================")
print("[START] CZU EXAM SUITE INTEGRITY & VALIDATION CHECKS")
print("======================================================================\n")

failed = False

def log_success(msg):
    print(f"[OK] SUCCESS: {msg}")

def log_failure(msg):
    global failed
    print(f"[ERR] FAILURE: {msg}", file=sys.stderr)
    failed = True

# 1. Check Python Generation Scripts
print("--- 1. Testing Code Generation Scripts ---")
try:
    # Run generate_is_master.py
    print("Running generate_is_master.py...")
    res1 = subprocess.run([sys.executable, "IS_EXAM_SUITE/generate_is_master.py"], capture_output=True, text=True, encoding="utf-8")
    if res1.returncode != 0:
        log_failure(f"generate_is_master.py failed with return code {res1.returncode}\nStderr: {res1.stderr}")
    else:
        log_success("generate_is_master.py executed successfully and generated EXAM_MASTER_2H.html")
except Exception as e:
    log_failure(f"Failed to execute generate_is_master.py: {e}")

try:
    # Run generate_anki_decks.py
    print("Running generate_anki_decks.py...")
    res2 = subprocess.run([sys.executable, "IS_EXAM_SUITE/anki_decks/generate_anki_decks.py"], capture_output=True, text=True, encoding="utf-8")
    if res2.returncode != 0:
        log_failure(f"generate_anki_decks.py failed with return code {res2.returncode}\nStderr: {res2.stderr}")
    else:
        log_success("generate_anki_decks.py executed successfully and synchronized Anki decks")
except Exception as e:
    log_failure(f"Failed to execute generate_anki_decks.py: {e}")

# 2. Check existence and non-emptiness of HTML files
print("\n--- 2. Checking HTML Files Integrity ---")
html_files = [
    "index.html", # Root
    "IS_EXAM_SUITE/index.html",
    "IS_EXAM_SUITE/EXAM_MASTER_2H.html",
    "IS_EXAM_SUITE/EXAM_BLITZ_2HR.html",
    "IS_EXAM_SUITE/smart_cram_cards.html"
]

for fpath in html_files:
    if not os.path.exists(fpath):
        log_failure(f"Required HTML file does not exist: {fpath}")
    elif os.path.getsize(fpath) == 0:
        log_failure(f"HTML file is empty: {fpath}")
    else:
        log_success(f"HTML file exists and has valid size ({os.path.getsize(fpath)} bytes): {fpath}")

# 3. Check existence of Anki files
print("\n--- 3. Checking Anki Deck Exports ---")
anki_files = [
    "IS_EXAM_SUITE/anki_decks/IS_Anki_Deck.txt",
    "IS_EXAM_SUITE/anki_decks/is_exam_suite_cards.txt",
    "IS_EXAM_SUITE/anki_decks/is_exam_suite_cards_cram.txt",
    "IS_EXAM_SUITE/anki_decks/IS_High_Yield_Blitz_Anki_Deck.txt",
    "IS_EXAM_SUITE/anki_decks/is_high_yield_blitz_cards.txt"
]

for fpath in anki_files:
    if not os.path.exists(fpath):
        log_failure(f"Required Anki file does not exist: {fpath}")
    elif os.path.getsize(fpath) == 0:
        log_failure(f"Anki file is empty: {fpath}")
    else:
        # Check UTF-8 read
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                lines = f.readlines()
            log_success(f"Anki file is valid UTF-8 and contains {len(lines)} cards/lines: {fpath}")
        except Exception as e:
            log_failure(f"Anki file {fpath} has encoding/read issues: {e}")

# 4. Validate Cross-Referencing Links in Global Navigation Bar
print("\n--- 4. Checking Global Navigation Link Targets ---")
for fpath in html_files[1:]: # Check the 4 IS sub-files
    print(f"Verifying links in {fpath}...")
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Find global-nav-bar block or matches
        # We will parse all <a href="..."> elements inside the global-nav-bar
        nav_match = re.search(r'<div class="global-nav-bar">.*?</div>', content, re.DOTALL)
        if not nav_match:
            log_failure(f"Global navigation bar markup not found in {fpath}")
            continue
            
        nav_html = nav_match.group(0)
        links = re.findall(r'href="([^"]+)"', nav_html)
        
        dir_name = os.path.dirname(fpath)
        for link in links:
            if link.startswith("#"):
                continue
            # Resolve relative link target
            target_path = os.path.normpath(os.path.join(dir_name, link))
            # Clean download/query params
            target_path = target_path.split("?")[0]
            
            if not os.path.exists(target_path):
                log_failure(f"Broken link in navigation of {fpath}: '{link}' resolves to non-existent file '{target_path}'")
            else:
                log_success(f"Link target verified: '{link}' -> '{target_path}'")
    except Exception as e:
        log_failure(f"Failed to read/verify links in {fpath}: {e}")

# 5. Check for common template remnants
print("\n--- 5. Checking for brackets or syntax templates ---")
for fpath in html_files:
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        # Look for {database_json} or {anki_tsv} that didn't get replaced
        for remnant in ["{database_json}", "{anki_tsv}"]:
            if remnant in content:
                log_failure(f"Unreplaced template placeholder '{remnant}' found in {fpath}")
            else:
                pass
    except Exception as e:
        pass

print("\n======================================================================")
if failed:
    print("[FAIL] INTEGRITY VALIDATION FAILED! Please review the errors above.", file=sys.stderr)
    sys.exit(1)
else:
    print("[PASS] ALL INTEGRITY & VALIDATION CHECKS PASSED SUCCESSFULLY!")
    sys.exit(0)
