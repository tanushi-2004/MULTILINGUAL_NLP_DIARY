# test_entities.py

from processors.entity_extractor import extract_entities
from langdetect import detect

# 📌 Test Cases

# 1. English
text_en = "Barack Obama was born in Hawaii and became the President of the USA in 2009."
lang_en = detect(text_en)
entities_en = extract_entities(text_en, lang_en)
print("📘 English")
print("Detected Language:", lang_en)
print("Entities:", entities_en)
print()

# 2. Hindi (if model is available)
text_hi = "नरेंद्र मोदी भारत के प्रधानमंत्री हैं।"
lang_hi = detect(text_hi)
entities_hi = extract_entities(text_hi, lang_hi)
print("📗 Hindi")
print("Detected Language:", lang_hi)
print("Entities:", entities_hi)
