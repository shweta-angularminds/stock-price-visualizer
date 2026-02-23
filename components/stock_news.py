import streamlit as st
from utils.helper import truncate_words

def stock_news(news_list):
    st.subheader("Latest News")

    if not news_list:
        st.info("No news available")
        return

    for article in news_list[:5]:

        content = article.get("content") or {}

        title = content.get("title", "No title")
        summary = content.get("summary", "")
        
        # Image
        thumbnail = content.get("thumbnail") or {}
        image_url = thumbnail.get("originalUrl") or None

        # Link
        link = (content.get("clickThroughUrl") or {}).get("url", "#")

        # Provider
        provider = content.get("provider", {}).get("displayName", "")

        # Card container
        with st.container(border=True):

            col1, col2 = st.columns([1, 3])

            with col1:
                if image_url:
                    st.image(image_url, width=150)

            with col2:
                st.markdown(f"### {title}")

                if provider:
                    st.caption(provider)

                if summary:
                    st.caption(truncate_words(summary, 25))


                st.markdown(f"[Read full article →]({link})")
    
    