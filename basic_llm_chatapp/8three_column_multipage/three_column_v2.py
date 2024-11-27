import streamlit as st

# Session state to manage navigation
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "home_welcome"  # Default page

# Navigation tree
navigation = {
    "Home": {
        "Welcome Page": "home_welcome",
        "Log In and Log Out": "home_login_logout",
    },
    "RAG": {
        "RAG Manually": {
            "RAG Blob Storage Page": "rag_blob_storage",
            "RAG SharePoint Page": "rag_sharepoint",
        },
    },
    "Arena": {
        "Two Competitors": {
            "ChatGPT and Gemini": "arena_chatgpt_gemini",
            "ChatGPT and Claude": "arena_chatgpt_claude",
        },
        "Three Competitors": {
            "ChatGPT and Gemini and Claude": "arena_chatgpt_gemini_claude",
        },
    },
}

# Helper function to render navigation tree
def render_navigation(nav_tree, level=0):
    for label, page in nav_tree.items():
        if isinstance(page, dict):  # Submenu
            st.markdown(f"{'  ' * level}**{label}**")
            render_navigation(page, level + 1)
        else:  # Page link
            if st.button(f"{'  ' * level}{label}", key=label):
                st.session_state["current_page"] = page

# Render sidebar navigation
with st.sidebar:
    st.header("Navigation")
    render_navigation(navigation)

# Include pages based on `st.session_state["current_page"]`
if st.session_state["current_page"] == "home_welcome":
    st.write("Welcome to the Home Page!")
elif st.session_state["current_page"] == "home_login_logout":
    st.write("Log In and Log Out Page")
elif st.session_state["current_page"] == "rag_blob_storage":
    st.write("RAG Blob Storage Page")
elif st.session_state["current_page"] == "rag_sharepoint":
    st.write("RAG SharePoint Page")
elif st.session_state["current_page"] == "arena_chatgpt_gemini":
    st.write("Arena: ChatGPT and Gemini")
elif st.session_state["current_page"] == "arena_chatgpt_claude":
    st.write("Arena: ChatGPT and Claude")
elif st.session_state["current_page"] == "arena_chatgpt_gemini_claude":
    st.write("Arena: ChatGPT, Gemini, and Claude")