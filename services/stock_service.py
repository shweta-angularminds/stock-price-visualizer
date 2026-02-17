import yfinance as yf
import streamlit as st

@st.cache_data(ttl=300)
def get_stock_Data(symbol,period):
    try:
        stock = yf.Ticker(symbol)
        
        data = stock.history(period=period)
        info = stock.info or {}
        news = stock.news or []
        
        return data,info,news
    
    except Exception as e:
        return None,{},[]