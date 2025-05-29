import streamlit as st
import fractions
from recipe_scanner import RecipeScanner

# Page configuration
st.set_page_config(page_title="Recipe Scanner", page_icon="📸", layout="centered")

# Styling
st.markdown("""
    <style>
        .main {
            background-color: #fff8f0;
            color: #333;
        }
        .stButton>button {
            background-color: #f6a192;
            color: white;
        }
        .stSelectbox, .stSlider {
            background-color: #ffe5d9;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📸 Recipe Scanner & Converter")
st.markdown("Scan recipe images, convert ingredients, and track prices with ease.")

# Select unit system
unit_system = st.selectbox("Select preferred unit system:", ["metric", "imperial"])
scanner = RecipeScanner(preferred_system=unit_system)

# Upload image
uploaded_file = st.file_uploader("Upload an image of the recipe:", type=["jpg", "png", "jpeg"])

# Scale factor input
scale_factor = st.slider("Scale recipe by a factor of:", 0.1, 5.0, 1.0, 0.1)

# Ingredient price input
st.subheader("💰 Ingredient Prices (Optional)")
ingredient_prices = {}

if uploaded_file:
    with open("temp_recipe.jpg", "wb") as f:
        f.write(uploaded_file.read())

    st.write("Processing image...")
    text = scanner.scan_image("temp_recipe.jpg")
    ingredients = scanner.parse_ingredients(text)
    scanner.convert_units()
    scanner.scale_recipe(scale_factor)

    # Price entry for each ingredient
    for ing in scanner.recognized_ingredients:
        price = st.number_input(f"Price for {ing['name']} ({ing['quantity']} {ing['unit']}):",
                                min_value=0.0, step=0.01, key=ing['name'])
        ingredient_prices[ing['name']] = price

    # Display results
    st.subheader("🧾 Scanned and Converted Ingredients")
    for ing in scanner.recognized_ingredients:
        quantity = str(fractions.Fraction(ing['quantity']).limit_denominator())
        price = ingredient_prices.get(ing['name'], 0.0)
        st.markdown(f"""
        <div style='padding: 6px; background-color: #ffe5d9; border-radius: 8px; margin-bottom: 4px;'>
            <b>{quantity} {ing['unit']} {ing['name']}</b><br>
            Price: <span style='color: green;'>${price:.2f}</span>
        </div>
        """, unsafe_allow_html=True)
