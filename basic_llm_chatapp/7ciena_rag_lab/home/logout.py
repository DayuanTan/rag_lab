import streamlit as st

st.title("Welcome to Ciena RAG Lab site!")

st.markdown("Click the button to log out:")

if st.button("Log out"):
    st.session_state.logged_in = False
    st.rerun()

