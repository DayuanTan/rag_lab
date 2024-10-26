import streamlit as st
import random
import time

st.title("Simple chat, reply with random predefined responses")

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)
        

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
    
    # Fake assistant response
    # Just echo users input
    # response = f"Echo: {prompt}" # Replace "echo", we randomly show a predefined response
    response = response_generator()
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        # st.markdown(response) # Display string formatted as Markdown.
        st.write_stream(response) # Stream a generator, iterable, or stream-like sequence to the app.
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})