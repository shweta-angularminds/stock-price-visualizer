

import streamlit as st
from services.stock_service import get_stock_Data

from components.stock_news import stock_news
st.set_page_config(layout="wide")

#-----------SESSION STATE DEFAULTS --------
if "symbol" not in st.session_state:
    st.session_state.symbol = "AAPL"
    
if "period" not in st.session_state:
    st.session_state.period = "6mo"
    

main_col1,main_col2 = st.columns(2,vertical_alignment="bottom")


with main_col2:
    symbol_input = st.text_input(
        "Search",
        label_visibility="collapsed",
        value=st.session_state.symbol,
        placeholder="Enter stock symbol (AAPL, TSLA, INFY)"
    )
    if symbol_input:
        st.session_state.symbol = symbol_input.upper()
        
data,info,news = get_stock_Data(st.session_state.symbol,st.session_state.period)

with main_col1:
        st.markdown(
        f"""
        <h2 style="margin:0;">
            {info['shortName']}
            <span style="font-size:16px; color:gray; font-weight:normal;">
                {info['symbol']}
            </span>
        </h2>
        """,
        unsafe_allow_html=True
        )

col1,col2 = st.columns(2)

with col1:
    
    metric_col1,metric_col2 = st.columns(2)

    with metric_col1:
        currency_symbol = {
        "USD": "$",
        "INR": "₹"
        }
        symbol = currency_symbol.get(info.get("currency"), "")

        latest = data["Close"].iloc[-1]
        previous = data["Close"].iloc[-2]
        change = latest - previous
        
        
        
        st.metric(
        label="Stocks",
        label_visibility="collapsed",

        value=f"{symbol}{latest:.2f}",
        delta=f"{symbol}{change:.2f}"
        )

    with metric_col2:

        option_map = {
            0: "6mo",
            1: "3mo",
            2: "1mo",
            3: "1d",
            4: "1y",
        }

        selection = st.pills(
            "Select Period",
            label_visibility="collapsed",
            options=list(option_map.keys()),
            format_func=lambda option: option_map[option],
            selection_mode="single",
            default=list(option_map.keys())[list(option_map.values()).index(st.session_state.period)]
        )

        if selection is not None:
            st.session_state.period = option_map[selection]

    st.line_chart(data["Close"],color="green")
    
with col2:
    st.subheader("Key Stats")
    df_ohlcv = data[['Open', 'High', 'Low', 'Close', 'Volume']]

    st.dataframe(df_ohlcv, width="stretch")
    


bottom_col1,bottom_col2 = st.columns(2,vertical_alignment="top")

with bottom_col1:
    st.subheader("Stock Volume")
    st.scatter_chart(data[["Volume"]],color="orange", width="stretch")
    
with bottom_col2:
    stock_news(news)