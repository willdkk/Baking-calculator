import streamlit as st

def manage_recipes():
    st.title("📘 Recipes")

    st.markdown("Manage and scale your recipes. You can also scan recipes from images.")

    st.text_input("Recipe Name")
    st.text_area("Ingredients (one per line: quantity unit ingredient)", height=200)

    col1, col2 = st.columns(2)
    with col1:
        scale_factor = st.number_input("Scale Factor", value=1.0, step=0.1)
    with col2:
        st.button("Scale Recipe")

    st.markdown("---")
    st.markdown("### Upload and Scan Recipe Image")
    image = st.file_uploader("Upload Recipe Image", type=["jpg", "png"])

    if image:
        st.image(image, caption="Uploaded Recipe", use_column_width=True)
        st.info("OCR feature will extract ingredients from this image (feature in progress).")

