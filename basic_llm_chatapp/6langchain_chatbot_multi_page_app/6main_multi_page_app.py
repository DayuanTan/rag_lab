import streamlit as st


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()



## Define sub pages

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

langchain_chatbot = st.Page(
    "langchain_chatbot/6langchain_chatbot.py", title="Langchain Chatbot", icon=":material/smart_toy:"
)

chatbot_arena = st.Page(
    "arena/arena.py", title="Chatbot Arena", icon=":material/swords:"
)

dashboard = st.Page(
    "reports/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True
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
st.set_page_config(page_title="Multi Page App", page_icon=":material/science:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Langchain Chatbot": [langchain_chatbot],
            "Chatbot Arena": [chatbot_arena],
            "Reports": [dashboard, bugs, alerts],
            "Tools": [search, history],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()