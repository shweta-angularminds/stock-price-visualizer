import streamlit as st

def update_symbol():
    st.session_state.symbol = st.session_state.symbol.upper()

def render_search():
    st.text_input("Search",label_visibility="collapsed",key = "symbol",placeholder="Enter stock symbol (AAPL, TSLA, INFY)", on_change= update_symbol)
    
    