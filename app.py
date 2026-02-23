import streamlit as st
from services.stock_service import get_stock_Data
from components.stock_news import stock_news
from components.header import render_header
from components.search import render_search
from components.metrics import render_metrics
from components.charts import render_line_chart,render_scatter_chart
from components.key_stats import render_key_stats

st.set_page_config(layout="wide",page_title="Dashboard", page_icon="📊")


def init_session():
    if "symbol" not in st.session_state:
        st.session_state.symbol = "AAPL"
    
    if "period" not in st.session_state:
        st.session_state.period = "6mo"
    
def main():
    init_session()

    main_col1,main_col2 = st.columns(2,vertical_alignment="bottom")

    with main_col2:
        render_search()
            
            
    data,info,news = get_stock_Data(st.session_state.symbol,st.session_state.period)

    with main_col1:
        render_header(info)


    col1,col2 = st.columns(2)

    with col1:
        render_metrics(info,data)
        render_line_chart(data,"green")
        
    with col2:
        render_key_stats(data)


    bottom_col1,bottom_col2 = st.columns(2,vertical_alignment="top")

    with bottom_col1:
        render_scatter_chart(data,"orange")
        
    with bottom_col2:
        stock_news(news)
        
        
if __name__ == "__main__":
    main()