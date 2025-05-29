import streamlit as st

def show_dashboard():
    st.title("📊 Dashboard")
    st.markdown("Welcome to the Bake Off Business Manager dashboard!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Orders", "124")
    with col2:
        st.metric("Revenue", "$2,350.00")
    with col3:
        st.metric("Most Popular Item", "Victoria Sponge")

    st.markdown("### Recent Orders")
    st.dataframe({
        "Customer": ["Alice", "Ben", "Cara"],
        "Item": ["Macarons", "Lemon Tart", "Brownies"],
        "Date": ["2025-05-25", "2025-05-24", "2025-05-23"],
        "Status": ["Delivered", "Baking", "Paid"]
    })

