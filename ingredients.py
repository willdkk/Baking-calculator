import pandas as pd
import streamlit as st

# Mock storage for demonstration
ingredients_list = []

def manage_ingredients():
    st.title("🧂 Ingredients Management")

    # Batch upload section
    st.subheader("📥 Batch Upload Ingredients from Excel")
    uploaded_file = st.file_uploader("Upload Ingredients Excel File", type=["xlsx"])

    if uploaded_file:
        try:
            df = pd.read_excel(uploaded_file)
            required_columns = {'Ingredient', 'Unit', 'Price per Unit'}

            if not required_columns.issubset(df.columns):
                st.error(f"Uploaded file must contain the following columns: {required_columns}")
            else:
                st.success("✅ Ingredients uploaded successfully!")
                st.dataframe(df)

                # Simulate adding to storage
                for _, row in df.iterrows():
                    ingredient = {
                        "name": row['Ingredient'],
                        "unit": row['Unit'],
                        "price_per_unit": row['Price per Unit']
                    }
                    ingredients_list.append(ingredient)

        except Exception as e:
            st.error(f"❌ Error reading Excel file: {e}")

    # Display current ingredients
    st.subheader("📋 Current Ingredients")
    if ingredients_list:
        st.table(ingredients_list)
    else:
        st.info("No ingredients uploaded yet.")
