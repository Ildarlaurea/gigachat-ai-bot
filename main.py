import streamlit as st

# Import necessary functions from gigachat_api
from gigachat_api import get_access_token, send_prompt, sent_prompt_and_get_response

# Set the title of the Streamlit app
st.title("IbotX AI")

# Check if the access token is already stored in the session
if "access_token" not in st.session_state:
    try:
        # Attempt to get an access token
        st.session_state.access_token = get_access_token()
        st.toast("Received a token") # Notify the user that the token was received
    except Exception as e:
        st.toast(f"Couldn't get a token: {e}") # Show error message if token retrieval fails

# Initialize chat history if not already stored in session
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "ai", "content": "How can i help you?"}]

# Display previous chat messages stored in session
for msg in st.session_state.messages:
    if msg.get("is_image"):
        # If the message contains an image, display it
        st.chat_message(msg["role"]).image(msg["content"])
    else:
        # Otherwise, display text message
        st.chat_message(msg["role"]).write(msg["content"])

# Capture user input from chat input field
if user_prompt := st.chat_input():
    # Display the user's message
    st.chat_message("user").write(user_prompt)
    # Store the user's message in session history
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # Show a spinner while processing the response
    with st.spinner("In process..."):
        # Send user prompt and get AI response
        response, is_image = sent_prompt_and_get_response(user_prompt, st.session_state.access_token)
        if is_image:
            # If the response is an image, display it
            st.chat_message("ai").image(response)
            # Store the AI image response in session history
            st.session_state.messages.append({"role": "ai", "content": response, "is_image": True})
        else:
            # Otherwise, display text response
            st.chat_message("ai").write(response)
            # Store the AI text response in session history
            st.session_state.messages.append({"role": "ai", "content": response})