import streamlit as st

def render_key_stats(data):
    st.subheader("Key Stats")
    df_ohlcv = data[['Open', 'High', 'Low', 'Close', 'Volume']]
    
    st.dataframe(df_ohlcv, width="stretch")
    