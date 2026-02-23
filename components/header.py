import streamlit as st

def render_header(info):
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

