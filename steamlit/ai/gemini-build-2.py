import streamlit as st
from google import genai
import os
from dotenv import load_dotenv
import time 

# Load environment variables from .env file
load_dotenv()

# Initialize the genai client
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY not found. Please check your .env file.")
    st.stop()

# Initialize the genai client
client = genai.Client(api_key=GOOGLE_API_KEY)

# Streamlit app
st.title("Google GenAI with Streamlit")

# Initialize session state for feedback, response and prompt
if "thumbs_up_clicked" not in st.session_state:
    st.session_state.thumbs_up_clicked = False
if "response" not in st.session_state:
    st.session_state.response = ""
if "prompt" not in st.session_state:
    st.session_state.prompt = ""

def generate_response():
    if st.session_state.prompt.strip():
        with st.spinner("Generating response..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.0-flash", contents=st.session_state.prompt
                )
                st.session_state.response = response.text
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt.")

# User input with Enter key submission
st.text_area("Enter a prompt:", value=st.session_state.prompt, key="prompt", on_change=generate_response)

# Button for manual generation
if st.button("Generate Response"):
    generate_response()

# Display response if available
if st.session_state.response:
    st.subheader("Response:")
    st.write(st.session_state.response)

    # Feedback section
    st.subheader("Was this response helpful?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👍 Thumbs Up"):
            st.session_state.thumbs_up_clicked = True
            st.success("Thank you for your feedback!")

    with col2:
        if st.button("👎 Thumbs Down"):
            st.warning("Feedback noted. We’ll work on improving the responses.")

# Trigger balloons if thumbs up was clicked
if st.session_state.thumbs_up_clicked:
    st.balloons()
    time.sleep(1)
    st.session_state.thumbs_up_clicked = False
