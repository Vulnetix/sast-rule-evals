# vnx-sec-027 eval target: Hugging Face API token hardcoded
from transformers import pipeline

# TRIGGERS rule
HF_TOKEN = "hf_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh"

pipe = pipeline("text-generation", token=HF_TOKEN)
