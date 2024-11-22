import streamlit as st

st.title("Echo Bot")

# Initialize chat history
# Check to see if the messages key is in st.session_state. If it's not, we initialize it to an empty list. This is because we'll be adding messages to the list later on, and we don't want to overwrite the list every time the app reruns.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# React to user input
# We used the := operator to assign the user's input to the prompt variable and checked if it's not None in the same line.
if prompt := st.chat_input("What is up?"):
    # If the user has sent a message
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    