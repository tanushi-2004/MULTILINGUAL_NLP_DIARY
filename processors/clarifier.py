# processors/clarifier.py

def clarify_text(pronoun):
    return f"🤔 Who does '{pronoun}' refer to? Please clarify."

def ask_clarification(ambiguity_detail):
    return f"Could you please clarify what you meant by: {ambiguity_detail}?"

def clarify_response(text, clarification_answer):
    if "kal" in text.lower():
        resolved_text = text.replace("kal", f"kal ({clarification_answer})")
    else:
        resolved_text = f"Clarified Text: {text}\nClarification: {clarification_answer}"
    return resolved_text
