import streamlit as st
from dashboard import show_dashboard
from ingredients import manage_ingredients
from recipes import manage_recipes
from orders import manage_orders
from costings import manage_costings
from inventory import manage_inventory
from calendar_view import show_calendar
from settings import app_settings

# App configuration
st.set_page_config(
    page_title="Bake Off Business Manager",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Bake Off Theme Styling
st.markdown("""
    <style>
    body {
        background-color: #fffaf0;
        color: #5a4a42;
        font-family: 'Georgia', serif;
    }
    .stButton>button {
        background-color: #f7c8da;
        color: #3b2e2a;
        border-radius: 20px;
        border: none;
        padding: 0.5em 1em;
    }
    .stTabs [role="tab"] {
        font-weight: bold;
        background-color: #f0e6ef;
        border-radius: 20px 20px 0 0;
        margin-right: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.image("/app/static/logo.png", width=150)
st.sidebar.title("🎀 Bake Off Manager")
page = st.sidebar.radio("Navigate", [
    "📊 Dashboard",
    "📦 Ingredients",
    "📘 Recipes",
    "📑 Costings",
    "📅 Orders",
    "📁 Inventory",
    "🗓️ Calendar",
    "⚙️ Settings"
])

# Page Routing
if page == "📊 Dashboard":
    show_dashboard()
elif page == "📦 Ingredients":
    manage_ingredients()
elif page == "📘 Recipes":
    manage_recipes()
elif page == "📑 Costings":
    manage_costings()
elif page == "📅 Orders":
    manage_orders()
elif page == "📁 Inventory":
    manage_inventory()
elif page == "🗓️ Calendar":
    show_calendar()
elif page == "⚙️ Settings":
    app_settings()
