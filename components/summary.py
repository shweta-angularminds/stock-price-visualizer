from services.text_summerize_service import generate_summary

import streamlit as st

def prepare_combined_text(info, news):

    company_text = info.get("longBusinessSummary", "")
    company_text = company_text[:800]
    news_text = ""
    for article in news[:2]:
        content = article.get("content") or {}
        news_text += content.get("summary", "") + " "

    combined = f"""
    Company Overview:
    {company_text}

    Recent News:
    {news_text}
    """

    return combined


def render_text_summarizer(info,news):
   
    combined_text = prepare_combined_text(info, news)
    
    if st.button("Generate Summary"):
        with st.spinner("Generating summary..."):
            summary = generate_summary(combined_text)

        st.success(summary)