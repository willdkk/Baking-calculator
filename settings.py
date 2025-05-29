import streamlit as st
import pandas as pd
import os

def app_settings():
    st.title("⚙️ App Settings")
    
    st.subheader("Theme Settings")
    st.write("You can customize the theme and appearance of the Bake Off Manager here in the future.")
    
    st.subheader("Data Management")
    st.write("Back up data, export/import settings, or reset your app.")

    st.markdown("🚧 *More settings coming soon!*")


# Load or initialize ingredient data
if os.path.exists("ingredients.csv"):
    ingredients_df = pd.read_csv("ingredients.csv")
else:
    ingredients_df = pd.DataFrame(columns=["Ingredient", "Unit", "Price per Unit"])

st.title("🧂 Ingredients Management")

# --- Search and Filter ---
search_term = st.text_input("Search Ingredients")
filter_alpha = st.checkbox("Sort Alphabetically", value=False)

# --- Batch Upload ---
st.subheader("📥 Batch Upload from Excel")
uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])
if uploaded_file:
    batch_df = pd.read_excel(uploaded_file)
    if set(["Ingredient", "Unit", "Price per Unit"]).issubset(batch_df.columns):
        ingredients_df = pd.concat([batch_df, ingredients_df], ignore_index=True)
        ingredients_df.to_csv("ingredients.csv", index=False)
        st.success("Batch upload successful and added to the top of the list.")
    else:
        st.error("Excel file must contain 'Ingredient', 'Unit', 'Price per Unit' columns.")

# --- Manual Entry ---
st.subheader("✍️ Manually Add Ingredient")
with st.form("manual_entry"):
    ingredient = st.text_input("Ingredient")
    unit = st.selectbox("Unit", ["g", "kg", "oz", "lb", "ml", "l", "tsp", "tbsp", "cup"])
    price = st.number_input("Price per Unit", min_value=0.0, step=0.01)
    submitted = st.form_submit_button("Add Ingredient")

    if submitted and ingredient:
        new_entry = pd.DataFrame([[ingredient, unit, price]], columns=["Ingredient", "Unit", "Price per Unit"])
        ingredients_df = pd.concat([new_entry, ingredients_df], ignore_index=True)
        ingredients_df.to_csv("ingredients.csv", index=False)
        st.success(f"Added {ingredient} to ingredient list.")

# --- Display Table ---
st.subheader("📋 Ingredient List")
filtered_df = ingredients_df.copy()
if search_term:
    filtered_df = filtered_df[filtered_df["Ingredient"].str.contains(search_term, case=False, na=False)]

if filter_alpha:
    filtered_df = filtered_df.sort_values("Ingredient")

st.dataframe(filtered_df.reset_index(drop=True))

