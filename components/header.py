import streamlit as st

def render_header(info):
    price = info.get("currentPrice", 0)
    prev = info.get("previousClose", 0)
    change = price - prev
    pct_change = (change / prev) * 100 if prev else 0

    st.markdown(f"""
        <h2 style="margin:0;">
            {info.get("shortName")} 
            <span style="font-size:16px; color:gray;">
                ({info.get("symbol")})
            </span>
        </h2>
    """, unsafe_allow_html=True)

    import streamlit as st

def render_header(info):
    
    st.markdown(f"""
        <h2 style="margin:0;">
            {info.get("shortName")} 
            <span style="font-size:16px; color:gray;">
                ({info.get("symbol")})
            </span>
        </h2>
    """, unsafe_allow_html=True)

    
def render_market_prices(info):
    price = info.get("currentPrice", 0)
    prev = info.get("previousClose", 0)
    change = price - prev
    pct_change = (change / prev) * 100 if prev else 0

    st.markdown(
    f"<span style='font-size:18px; font-weight:600;'>"
    f"${price:.2f} "
    f"{'🟢' if change >= 0 else '🔴'} "
    f"{change:.2f} ({pct_change:.2f}%)"
    f"</span>",
    unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    col1.markdown(f"**Market Cap**  \n${info.get('marketCap'):,}")
    col2.markdown(f"**P/E**  \n{info.get('trailingPE')}")
    col3.markdown(f"**Div Yield**  \n{info.get('dividendYield',0)*100:.2f}%")
    