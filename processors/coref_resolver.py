# processors/coref_resolver.py

import re

# List of common ambiguous pronouns in English and Hindi
AMBIGUOUS_PRONOUNS = ["he", "she", "they", "his", "her", "him", "उसने", "उसकी", "उनका"]

def resolve_coref(text):
    # Lowercase version for easy matching
    text_lower = text.lower()

    found_pronoun = None
    for pronoun in AMBIGUOUS_PRONOUNS:
        if re.search(rf"\b{pronoun}\b", text_lower):
            found_pronoun = pronoun
            break

    result = {
        "original_text": text,
        "resolved_text": text,  # Same for now — until clarified
        "ambiguous": bool(found_pronoun),
        "ambiguous_pronoun": found_pronoun
    }

    return result
