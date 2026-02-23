import streamlit as st

def render_metrics(info,data):
    metric_col1,metric_col2 = st.columns(2)

    with metric_col1:
        currency_symbol = {
        "USD": "$",
        "INR": "₹"
        }
        data = data.sort_index()
        symbol = currency_symbol.get(info.get("currency"), "")

        latest = data["Close"].iloc[-1]
        previous = data["Close"].iloc[-2]
        change = latest - previous
        
        st.metric(
        label="Stocks",
        label_visibility="collapsed",

        value=f"{symbol}{latest:.2f}",
        delta=f"{change:.2f}",
        delta_color="normal"
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
