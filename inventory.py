import streamlit as st

def manage_inventory():
    st.title("📁 Inventory Management")

    st.markdown("Track stock levels of your ingredients and receive low stock alerts.")

    st.dataframe({
        "Ingredient": ["Flour", "Butter", "Sugar"],
        "Stock Level": [3000, 1200, 500],
        "Unit": ["grams", "grams", "grams"],
        "Low Stock Threshold": [1000, 1000, 300]
    })

    st.warning("⚠️ Sugar is low in stock. Consider restocking.")
