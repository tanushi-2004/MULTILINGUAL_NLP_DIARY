from transformers import XLMRobertaModel, XLMRobertaTokenizer
import torch

# Model aur tokenizer ka naam
model_name = "xlm-roberta-base"

# Load tokenizer and model
tokenizer = XLMRobertaTokenizer.from_pretrained(model_name)
model = XLMRobertaModel.from_pretrained(model_name)

def get_embedding(text):
    # Text ko tokenize karo
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    # Model me input do, output lo
    with torch.no_grad():
        outputs = model(**inputs)
    # Last hidden state le lo
    last_hidden_state = outputs.last_hidden_state
    # Tokens ka average nikal kar sentence embedding banao
    sentence_embedding = last_hidden_state.mean(dim=1).squeeze()
    return sentence_embedding.numpy()

if __name__ == "__main__":
    sample_text = "मैं आज खुश हूँ।"
    embedding = get_embedding(sample_text)
    print("Embedding shape:", embedding.shape)
    print("Embedding vector (first 5 values):", embedding[:5])
