import streamlit as st
 
st.title("Simple ATM")
 
balance = 10000
 
st.metric(
    "Current Balance",
    f"₱{balance:,.2f}"
)