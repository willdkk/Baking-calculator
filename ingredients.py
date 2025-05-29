import streamlit as st
import pandas as pd

# Simulated in-memory database
if 'ingredients_db' not in st.session_state:
    st.session_state.ingredients_db = pd.DataFrame(columns=["Ingredient", "Unit", "Price per Unit"])

def manage_ingredients():
    st.title("📦 Ingredient Management")

    st.subheader("🔍 Search & Sort")
    search_query = st.text_input("Search Ingredients")
    sort_order = st.radio("Sort Alphabetically", ["A → Z", "Z → A"])

    # Upload from Excel
    st.subheader("📤 Upload Ingredients from Excel")
    uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])
    if uploaded_file:
        try:
            df_uploaded = pd.read_excel(uploaded_file)
            if set(["Ingredient", "Unit", "Price per Unit"]).issubset(df_uploaded.columns):
                st.session_state.ingredients_db = pd.concat(
                    [df_uploaded, st.session_state.ingredients_db],
                    ignore_index=True
                )
                st.success("Ingredients added successfully!")
            else:
                st.error("Excel must contain 'Ingredient', 'Unit', and 'Price per Unit' columns.")
        except Exception as e:
            st.error(f"Upload failed: {e}")

    # Manual entry
    st.subheader("✍️ Add Ingredient Manually")
    with st.form("manual_entry_form"):
        ingredient = st.text_input("Ingredient Name")
        unit = st.text_input("Unit (e.g., g, kg, cups)")
        price = st.number_input("Price per Unit", min_value=0.0, format="%.2f")
        submitted = st.form_submit_button("Add Ingredient")

        if submitted and ingredient and unit:
            new_row = pd.DataFrame([{
                "Ingredient": ingredient,
                "Unit": unit,
                "Price per Unit": price
            }])
            st.session_state.ingredients_db = pd.concat(
                [new_row, st.session_state.ingredients_db],
                ignore_index=True
            )
            st.success(f"{ingredient} added successfully!")
        elif submitted:
            st.warning("Please fill in all fields.")

    # Filter and display
    df_display = st.session_state.ingredients_db.copy()
    if search_query:
        df_display = df_display[df_display["Ingredient"].str.contains(search_query, case=False)]

    df_display = df_display.sort_values(by="Ingredient", ascending=(sort_order == "A → Z"))

    st.subheader("📋 Current Ingredients")
    st.dataframe(df_display, use_container_width=True)

    # Download option
    st.download_button(
        label="📥 Download Ingredients as Excel",
        data=df_display.to_excel(index=False),
        file_name="ingredients_list.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    
