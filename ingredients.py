import streamlit as st
import pandas as pd

# Initialize session state for ingredients
if 'ingredients_db' not in st.session_state:
    st.session_state.ingredients_db = pd.DataFrame(columns=["Ingredient", "Unit", "Price per Unit"])

def manage_ingredients():
    st.title("📦 Ingredient Management")

    # === Manual Entry Form ===
    st.subheader("✍️ Add Ingredient Manually")
    with st.form("manual_ingredient_form"):
        name = st.text_input("Ingredient")
        unit = st.text_input("Unit")
        price = st.number_input("Price per Unit", min_value=0.0, step=0.01)
        submit = st.form_submit_button("Add Ingredient")
        if submit and name and unit:
            new_row = pd.DataFrame([{
                "Ingredient": name,
                "Unit": unit,
                "Price per Unit": price
            }])
            st.session_state.ingredients_db = pd.concat(
                [new_row, st.session_state.ingredients_db], ignore_index=True
            )
            st.success(f"{name} added!")

    # === Display Table ===
    st.subheader("📋 Ingredients List")
    st.dataframe(st.session_state.ingredients_db, use_container_width=True)

    )

    
