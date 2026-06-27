# -*- coding: utf-8 -*-
import os
import re

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # points to IS_EXAM_SUITE

def clean_html_brackets(text):
    # Normalize quote escapes or similar if needed
    return text.replace('\\"', '"').replace("\\'", "'").replace('\\/', '/')

def parse_index_cards():
    index_path = os.path.join(base_dir, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract cramCardsData array content
    match = re.search(r'const\s+cramCardsData\s*=\s*(\[.*?\])\s*;', content, re.DOTALL)
    if not match:
        raise ValueError("Could not find cramCardsData in index.html")
        
    array_str = match.group(1)
    
    # We will parse item by item using regex
    # Match { ... } blocks
    item_pattern = r'\{([^{}]*?)\}'
    items_raw = re.findall(item_pattern, array_str, re.DOTALL)
    
    cards = []
    for item in items_raw:
        id_match = re.search(r'"id"\s*:\s*(\d+)', item)
        cat_match = re.search(r'"category"\s*:\s*"(.*?)"', item)
        q_match = re.search(r'"q"\s*:\s*"(.*?)"', item)
        desc_match = re.search(r'"desc"\s*:\s*"(.*?)"', item)
        ans_match = re.search(r'"ans"\s*:\s*"(.*?)"', item)
        
        cid = int(id_match.group(1)) if id_match else 0
        cat = cat_match.group(1) if cat_match else ""
        q = q_match.group(1) if q_match else ""
        desc = desc_match.group(1) if desc_match else ""
        ans = ans_match.group(1) if ans_match else ""
        
        cards.append({
            "id": cid,
            "category": clean_html_brackets(cat),
            "q": clean_html_brackets(q),
            "desc": clean_html_brackets(desc),
            "ans": clean_html_brackets(ans)
        })
    return cards

def parse_blitz_cards():
    blitz_path = os.path.join(base_dir, "EXAM_BLITZ_2HR.html")
    with open(blitz_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    match = re.search(r'const\s+allCards\s*=\s*(\[.*?\])\s*;', content, re.DOTALL)
    if not match:
        raise ValueError("Could not find allCards in EXAM_BLITZ_2HR.html")
        
    array_str = match.group(1)
    
    # Match { ... } blocks
    item_pattern = r'\{([^{}]*?)\}'
    items_raw = re.findall(item_pattern, array_str, re.DOTALL)
    
    cards = []
    for item in items_raw:
        deck_match = re.search(r'deck\s*:\s*([\'"`])(.*?)\1', item)
        cat_match = re.search(r'cat\s*:\s*([\'"`])(.*?)\1', item)
        q_match = re.search(r'q\s*:\s*([\'"`])(.*?)\1', item)
        a_match = re.search(r'a\s*:\s*([\'"`])(.*?)\1', item)
        
        deck = deck_match.group(2) if deck_match else ""
        cat = cat_match.group(2) if cat_match else ""
        q = q_match.group(2) if q_match else ""
        a = a_match.group(2) if a_match else ""
        
        cards.append({
            "deck": clean_html_brackets(deck),
            "cat": clean_html_brackets(cat),
            "q": clean_html_brackets(q),
            "a": clean_html_brackets(a)
        })
    return cards

def generate_decks():
    print("Parsing index.html cards...")
    index_cards = parse_index_cards()
    print(f"Loaded {len(index_cards)} cards from index.html")
    
    print("Parsing EXAM_BLITZ_2HR.html cards...")
    blitz_cards = parse_blitz_cards()
    print(f"Loaded {len(blitz_cards)} cards from EXAM_BLITZ_2HR.html")
    
    # Output paths
    anki_dir = os.path.join(base_dir, "anki_decks")
    os.makedirs(anki_dir, exist_ok=True)
    
    # 1. Generate is_exam_suite_cards.txt (plain text, 50 cards)
    p1 = os.path.join(anki_dir, "is_exam_suite_cards.txt")
    with open(p1, "w", encoding="utf-8") as f:
        f.write("# ============================================================\n")
        f.write("# Information Systems \u2014 CZU Prague \u2014 Anki Import Deck\n")
        f.write("# DW/SINV | ERP | DSS | BI/BPM | AI/ML | Cloud | CI \u2014 50 exam-targeted cards\n")
        f.write("# Format: Front[TAB]Back[TAB]Tag\n")
        f.write("# Import in Anki: File > Import > select this file\n")
        f.write("# ============================================================\n")
        for card in index_cards:
            front = f"{card['q']} \u2014 {card['desc']}"
            back = card['ans']
            tag = card['category'].lower().replace('&', '').replace(' ', '_').replace('__', '_')
            f.write(f"{front}\t{back}\t{tag}\n")
    print(f"Generated {p1}")
            
    # 2. Generate is_exam_suite_cards_cram.txt (plain text, 50 cards with cram tag)
    p2 = os.path.join(anki_dir, "is_exam_suite_cards_cram.txt")
    with open(p2, "w", encoding="utf-8") as f:
        f.write("# ============================================================\n")
        f.write("# Information Systems \u2014 CZU Prague \u2014 CRAM Deck (Quick Review Mode)\n")
        f.write("# DW/SINV | ERP | DSS | BI/BPM | AI/ML | Cloud | CI \u2014 50 exam-targeted cards\n")
        f.write("# Format: Front[TAB]Back[TAB]Tag\n")
        f.write("# ============================================================\n")
        for card in index_cards:
            front = f"{card['q']} \u2014 {card['desc']}"
            back = card['ans']
            tag = "cram_" + card['category'].lower().replace('&', '').replace(' ', '_').replace('__', '_')
            f.write(f"{front}\t{back}\t{tag}\n")
    print(f"Generated {p2}")
            
    # 3. Generate IS_Anki_Deck.txt (HTML styled, 50 cards)
    p3 = os.path.join(anki_dir, "IS_Anki_Deck.txt")
    with open(p3, "w", encoding="utf-8") as f:
        f.write("#separator:tab\n#html:true\n#tags column:3\n")
        for card in index_cards:
            front = f'<div class="anki-card"><div class="anki-category">{card["category"]}</div><div class="anki-q-title">{card["q"]}</div><div class="anki-desc">{card["desc"]}</div></div>'
            back = f'<div class="anki-card-back"><div class="anki-ans">{card["ans"]}</div></div>'
            tag = "IS_Exam_" + card['category'].lower().replace('&', '').replace(' ', '_').replace('__', '_')
            f.write(f"{front}\t{back}\t{tag}\n")
    print(f"Generated {p3}")
            
    # 4. Generate is_high_yield_blitz_cards.txt (plain text, 42 cards)
    p4 = os.path.join(anki_dir, "is_high_yield_blitz_cards.txt")
    with open(p4, "w", encoding="utf-8") as f:
        f.write("# ============================================================\n")
        f.write("# Information Systems \u2014 CZU Prague \u2014 High Yield Blitz Deck\n")
        f.write("# SDLC, BPR, SAP Org levels, SAP modules, P2P/O2C, CIA, ACID, Encryption, etc.\n")
        f.write("# Format: Front[TAB]Back[TAB]Tag\n")
        f.write("# ============================================================\n")
        for card in blitz_cards:
            front = card['q']
            back = card['a']
            tag = "blitz_" + card['cat'].lower().replace('&', '').replace(' ', '_').replace('__', '_')
            f.write(f"{front}\t{back}\t{tag}\n")
    print(f"Generated {p4}")
            
    # 5. Generate IS_High_Yield_Blitz_Anki_Deck.txt (HTML styled, 42 cards)
    p5 = os.path.join(anki_dir, "IS_High_Yield_Blitz_Anki_Deck.txt")
    with open(p5, "w", encoding="utf-8") as f:
        f.write("#separator:tab\n#html:true\n#tags column:3\n")
        for card in blitz_cards:
            front = f'<div class="anki-card"><div class="anki-category">{card["cat"]}</div><div class="anki-q-title">{card["q"]}</div></div>'
            back = f'<div class="anki-card-back"><div class="anki-ans">{card["a"]}</div></div>'
            tag = "IS_Exam_Blitz_" + card['cat'].lower().replace('&', '').replace(' ', '_').replace('__', '_')
            f.write(f"{front}\t{back}\t{tag}\n")
    print(f"Generated {p5}")

if __name__ == "__main__":
    generate_decks()
