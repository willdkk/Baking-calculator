import streamlit as st
import pandas as pd
import datetime

def show_calendar():
    st.title("🗓️ Order Calendar")

    st.markdown("Here’s a visual of upcoming orders.")

    orders = pd.DataFrame({
        "Order": ["Macarons", "Scones", "Cupcakes"],
        "Customer": ["Alice", "Ben", "Cara"],
        "Date": ["2025-05-28", "2025-05-29", "2025-05-30"]
    })

    for _, row in orders.iterrows():
        st.markdown(f"📌 **{row['Date']}**: {row['Customer']} - *{row['Order']}*")
