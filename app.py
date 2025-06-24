import gradio as gr
from langdetect import detect

# 🌍 Language Detection Function
def detect_language(text):
    try:
        language = detect(text)
        return f"🔎 Detected Language Code: {language}"
    except:
        return "❌ Could not detect language. Please try again."

# 🎨 UI
iface = gr.Interface(
    fn=detect_language,
    inputs=gr.Textbox(lines=5, label="✍️ Write anything in any language"),
    outputs=gr.Textbox(label="🌐 Detected Language"),
    title="🧠 Multilingual NLP Diary - Phase 1",
    description="Write in Hindi, English, Hinglish or any language! We'll detect it for you 💡"
)

# 🚀 Launch the app
iface.launch()
