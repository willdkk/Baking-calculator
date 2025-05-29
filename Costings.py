import streamlit as st

def manage_costings():
    st.title("📑 Costings")

    st.markdown("View and manage detailed cost breakdowns for each recipe.")

    selected_recipe = st.selectbox("Select Recipe", ["Victoria Sponge", "Scones", "Macarons"])
    st.markdown(f"#### Cost Breakdown for {selected_recipe}")

    st.dataframe({
        "Ingredient": ["Flour", "Butter", "Sugar"],
        "Quantity": [200, 100, 150],
        "Unit": ["grams", "grams", "grams"],
        "Unit Cost": [0.002, 0.01, 0.005],
        "Total Cost": [0.4, 1.0, 0.75]
    })

    st.markdown("### Total Recipe Cost: £2.15")
    st.markdown("Profit Margin: 50%")
