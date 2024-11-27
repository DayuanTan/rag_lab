import streamlit as st

# Create three columns
col1, col2, col3 = st.columns([1, 1, 3])  # Adjust width ratios as needed

# Sidebar 1
with col1:
    st.header("Sidebar 1")
    st.text_input("Input in Sidebar 1")
    st.button("Button 1")

# Sidebar 2
with col2:
    st.header("Sidebar 2")
    st.text_input("Input in Sidebar 2")
    st.button("Button 2")

# Main Content
with col3:
    st.header("Main Content")
    st.write("This is the main content area.")
    st.text_area("Main Content Input")