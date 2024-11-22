import streamlit as st


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("Welcome to Ciena RAG Lab site!")
    st.markdown("Please click the button to log in:")
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()



## Define sub pages

login_page = st.Page(login, title="Log in", icon=":material/login:")


home = st.Page(
    "home/home.py", title="Home", icon=":material/home:", default=True
)
logout_page = st.Page(
    "home/logout.py", title="Log out", icon=":material/logout:"
)


chatbot = st.Page(
    "chatbot/chatbot.py", title="CienaRAG Chatbot", icon=":material/smart_toy:"
)

chatbot_arena = st.Page(
    "arena/arena.py", title="CienaRAG Arena", icon=":material/swords:"
)


bugs = st.Page("reports/bugs.py", title="Bug reports", icon=":material/bug_report:")
alerts = st.Page(
    "reports/alerts.py", title="System alerts", icon=":material/notification_important:"
)

search = st.Page("tools/search.py", title="Search", icon=":material/search:")
history = st.Page("tools/history.py", title="History", icon=":material/history:")


## Main page
# Set the Streamlit app's title, favicon, and page title

# page title and favicon consistently across pages
st.set_page_config(page_title="CienaRAG Lab", page_icon=":material/science:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Home": [home, logout_page],
            "CienaRAG Chatbot": [chatbot],
            "CienaRAG Arena": [chatbot_arena],
            "Reports": [bugs, alerts],
            "Tools": [search, history],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()