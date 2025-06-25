# processors/sentence_splitter.py

from langdetect import detect
import nltk
import re

# Download punkt tokenizer (only once)
nltk.download('punkt', quiet=True)

from nltk.tokenize import sent_tokenize

# Split sentences based on detected language
def split_sentences(text):
    try:
        lang = detect(text)

        if lang == 'en':
            sentences = sent_tokenize(text)
        elif lang == 'hi':
            # rudimentary sentence split for Hindi
            sentences = re.split(r'[।!?]', text)
            sentences = [s.strip() for s in sentences if s.strip()]
        else:
            # fallback for other languages
            sentences = re.split(r'[.!?]', text)
            sentences = [s.strip() for s in sentences if s.strip()]

        return lang, sentences

    except Exception as e:
        return "unknown", [f"Error: {str(e)}"]
