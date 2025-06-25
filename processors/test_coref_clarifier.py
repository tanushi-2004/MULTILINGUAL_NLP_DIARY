# processors/test_coref_clarifier.py

from processors.coref_resolver import resolve_coref
from processors.clarifier import clarify_text

sample_inputs = [
    "उसने मुझे कॉल किया",
    "He said he’ll arrive soon.",
    "Riya met Simran at the station.",
    "मैंने मम्मी से बात की और उसने कहा सब ठीक है"
]

for i, text in enumerate(sample_inputs):
    print(f"\n{i+1}. Input: {text}")
    result = resolve_coref(text)
    if result["ambiguous"]:
        print(f"🔍 Ambiguous Pronoun Found: {result['ambiguous_pronoun']}")
        print(f"🧠 Prompt: {clarify_text(result['ambiguous_pronoun'])}")
    else:
        print("✅ No ambiguity detected.")
