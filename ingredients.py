import streamlit as st

def manage_ingredients():
    st.title("📦 Ingredients Management")

    st.markdown("Add or update your ingredient list below. Prices will reflect your local currency and update your recipe costings.")

    ingredient = st.text_input("Ingredient Name")
    unit = st.selectbox("Unit", ["grams", "kilograms", "ml", "liters", "cups", "tbsp", "tsp", "oz", "lb"])
    price = st.number_input("Price per Unit", min_value=0.0, format="%.2f")
    currency = st.selectbox("Currency", ["$", "£", "€", "₦"])

    if st.button("Add Ingredient"):
        st.success(f"Added {ingredient} at {currency}{price}/{unit}.")

    st.markdown("---")
    st.markdown("### Current Ingredients")
    st.dataframe({
        "Ingredient": ["Flour", "Butter", "Sugar"],
        "Unit": ["grams", "grams", "grams"],
        "Price": ["£0.002", "£0.01", "£0.005"]
    })

