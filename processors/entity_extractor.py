# processors/entity_extractor.py

import spacy

# 📘 Load spaCy models (English and Hindi)
# If you haven't downloaded them yet, do:
# python -m spacy download en_core_web_sm
# pip install https://github.com/rohitsaluja/spacy-hindi/releases/download/v0.1.0/spacy_hindi-0.1.0-py3-none-any.whl

try:
    nlp_en = spacy.load("en_core_web_sm")
except:
    raise Exception("Please run: python -m spacy download en_core_web_sm")

try:
    import spacy_hindi
    nlp_hi = spacy_hindi.load()
except:
    nlp_hi = None
    print("⚠️ Hindi model not found. Hindi extraction will be skipped.")


# 🧠 Main Entity Extraction Function
def extract_entities(text, lang_code='en'):
    if lang_code == 'hi' and nlp_hi:
        doc = nlp_hi(text)
    else:
        doc = nlp_en(text)

    entities = {}
    for ent in doc.ents:
        label = ent.label_
        if label not in entities:
            entities[label] = []
        entities[label].append(ent.text)

    return entities
