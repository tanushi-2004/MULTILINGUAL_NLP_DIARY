def detect_ambiguity(text):
    ambiguous_keywords = ["kya", "kaun", "kab", "kal"]
    for word in ambiguous_keywords:
        if word in text.lower():
            return True, f"Ambiguous word detected: '{word}'"
    return False, ""
