from transformers import pipeline
import streamlit as st

@st.cache_resource
def load_model():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-base"
    )

def generate_summary(text):
    summarizer = load_model()
    prompt = f"""
    Summarize the following company information in 4 bullet points,
    focusing on business model and services:

    {text}
    """
    text = text[:1200]  # prevent long input error
    
    result = summarizer(
        prompt,
        max_length=180,
        do_sample=False
    )

    return result[0]["generated_text"]