import streamlit as st

def render_line_chart(data,color):
    st.line_chart(data["Close"],color=color)
    
    
def render_scatter_chart(data,color):
    st.subheader("Stock Volume")
    st.scatter_chart(data[["Volume"]],color=color, width="stretch")