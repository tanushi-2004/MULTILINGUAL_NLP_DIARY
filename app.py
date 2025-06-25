import gradio as gr
from langdetect import detect

# Import your phase 3 functions
from processors.ambiguity_detector import detect_ambiguity
from processors.clarifier import ask_clarification

def process_text(text):
    try:
        language = detect(text)
    except:
        language = None
    
    if not language:
        return "❌ Could not detect language. Please try again.", "", ""

    ambiguous, ambiguity_details = detect_ambiguity(text)
    
    if ambiguous:
        clarification_question = ask_clarification(ambiguity_details)
        return f"🔎 Detected Language Code: {language}", f"⚠️ Ambiguity detected: {ambiguity_details}", clarification_question
    else:
        return f"🔎 Detected Language Code: {language}", "✅ No ambiguity detected.", ""

def clarify_response(text, clarification_answer):
    resolved_text = f"Your clarification answer was: {clarification_answer}\nFinal text processed."
    return resolved_text

with gr.Blocks() as iface:
    input_text = gr.Textbox(lines=5, label="✍️ Write anything in any language")
    language_output = gr.Textbox(label="🌐 Detected Language")
    ambiguity_output = gr.Textbox(label="⚠️ Ambiguity Status")
    clarification_input = gr.Textbox(lines=2, label="❓ Please clarify (if asked)")
    final_output = gr.Textbox(label="✅ Final Output")
    
    detect_btn = gr.Button("Process Text")
    clarify_btn = gr.Button("Submit Clarification")
    
    detect_btn.click(process_text, inputs=input_text, outputs=[language_output, ambiguity_output, clarification_input])
    clarify_btn.click(clarify_response, inputs=[input_text, clarification_input], outputs=final_output)

iface.launch()
