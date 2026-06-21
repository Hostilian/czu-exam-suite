import os
import re
import asyncio
import edge_tts

def clean_html(text):
    # Replace common HTML breaks/tags with natural speech breaks
    text = text.replace("<br>", ". ").replace("<br/>", ". ").replace("<br />", ". ")
    text = text.replace("<b>", "").replace("</b>", "")
    text = text.replace("<i>", "").replace("</i>", "")
    text = text.replace("&nbsp;", " ")
    # Strip any remaining HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # Normalize spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def load_cards():
    cards_path = os.path.join("anki_decks", "is_exam_suite_cards.txt")
    if not os.path.exists(cards_path):
        # Fallback to root or alternative paths if needed
        cards_path = "is_exam_suite_cards.txt"
        
    cards = []
    with open(cards_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) >= 2:
                front = clean_html(parts[0])
                back = clean_html(parts[1])
                category = parts[2].strip() if len(parts) > 2 else "General"
                cards.append({
                    "category": category,
                    "q": front,
                    "ans": back
                })
    return cards

def build_narration_script(cards):
    script_parts = [
        "Welcome to the Information Systems Active Recall Cram Session.",
        "We will review fifty high-yield concepts for the Information Systems exam.",
        "Listen to the concepts and their definitions, organized by category.",
        "Let us begin."
    ]
    
    current_cat = None
    card_index = 1
    for card in cards:
        cat = card["category"].upper()
        if cat != current_cat:
            current_cat = cat
            script_parts.append(f"Category: {cat}.")
            
        script_parts.append(f"Concept {card_index}: {card['q']}.")
        script_parts.append(f"Explanation: {card['ans']}.")
        script_parts.append("") # Pause
        card_index += 1
        
    script_parts.append("This concludes the Information Systems study guide. Good luck on your exam!")
    return "\n".join(script_parts)

async def generate_voice(text, voice_name, filename):
    print(f"Generating voice: {voice_name} -> {filename}...")
    try:
        communicate = edge_tts.Communicate(text, voice_name, rate="+4%")
        await communicate.save(filename)
        print(f"Successfully generated {filename}!")
    except Exception as e:
        print(f"Error generating {filename}: {e}")

async def main():
    cards = load_cards()
    print(f"Loaded {len(cards)} cards for narration.")
    script = build_narration_script(cards)
    
    # Define voices
    voices = {
        "en-US-SteffanNeural": "is_audio_guide_us_male.mp3",
        "en-US-JennyNeural": "is_audio_guide_us_female.mp3",
        "en-GB-RyanNeural": "is_audio_guide_uk_male.mp3",
        "en-GB-SoniaNeural": "is_audio_guide_uk_female.mp3"
    }
    
    # Generate them concurrently
    tasks = []
    for voice_name, filename in voices.items():
        tasks.append(generate_voice(script, voice_name, filename))
        
    await asyncio.gather(*tasks)
    
    # Create the primary file copy
    if os.path.exists("is_audio_guide_us_male.mp3"):
        import shutil
        shutil.copyfile("is_audio_guide_us_male.mp3", "is_audio_guide.mp3")
        print("Created default copy: is_audio_guide.mp3")

if __name__ == "__main__":
    asyncio.run(main())
