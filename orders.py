import streamlit as st

def manage_orders():
    st.title("📅 Order Management")

    st.text_input("Customer Name")
    st.text_input("Product Ordered")
    st.date_input("Delivery Date")
    st.selectbox("Status", ["Pending", "Paid", "Baking", "Delivered"])
    st.button("Add Order")

    st.markdown("---")
    st.markdown("### Current Orders")
    st.dataframe({
        "Customer": ["Alice", "Ben"],
        "Product": ["Scones", "Lemon Drizzle"],
        "Date": ["2025-05-29", "2025-05-30"],
        "Status": ["Paid", "Pending"]
    })
