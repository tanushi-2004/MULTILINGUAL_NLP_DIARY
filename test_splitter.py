# test_splitter.py

from processors.sentence_splitter import split_sentences

texts = {
    "English": "Hello Tanushi! How are you doing today? Hope everything is great.",
    "Hindi": "तुम कैसे हो? क्या सब ठीक है। मैं ठीक हूँ।",
    "Hinglish": "Kal main market gaya tha. Fir mom ne kaha ki jaldi ghar aa jao!"
}

for label, text in texts.items():
    print(f"\n📌 {label}")
    lang, sents = split_sentences(text)
    print(f"Detected Language: {lang}")
    print("📝 Sentences:")
    for s in sents:
        print(f"→ {s}")
