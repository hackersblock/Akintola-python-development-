import streamlit as st
from google import genai
import os
from dotenv import load_dotenv
import time 

    # Navbar
st.markdown(
    """
    <style>
    .nav {
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: red;
        color: light-dark(#333b3c, #efefec);
        background-color: light-dark(#efedea, #223a2c);
        text-align: center;
    }
    .link{
        link-decoration:: none;
    }
    </style>
    <nav class="nav">
        <p>Made with ❤️ by <a href="https://x.com/photofola" classname="link">Dev Akintola</a> using Streamlit.</p>
    </nav>
    """,
    unsafe_allow_html=True,
)

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
st.divider()

# Initialize session state for feedback and response
if "thumbs_up_clicked" not in st.session_state:
    st.session_state.thumbs_up_clicked = False
if "response" not in st.session_state:
    st.session_state.response = ""


# User input
prompt = st.text_area("Enter a prompt:", "Explain how AI works in a few words")

if st.button("Generate Response"):
    with st.spinner("Generating response..."):
        try:
            # Check if prompt is not empty
            if prompt.strip():
                # Generate content
                response = client.models.generate_content(
                    model="gemini-2.0-flash", contents=prompt
                )
                st.session_state.response = response.text
            else:
                st.warning("Please enter a prompt.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Display response if available
if st.session_state.response:
    st.subheader("Response:")
    st.write(st.session_state.response)

    # Feedback section
    st.subheader("Was this response helpful?")
    col1, col2 = st.columns(2)
    row1, row2 = st.columns(2)
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

    # Footer
st.markdown(
    """
    <style>
    .footer {
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: red;
        color: light-dark(#333b3c, #efefec);
        background-color: light-dark(#efedea, #223a2c);
        text-align: center;
    }
    .link{
        link-decoration:: none;
    }
    </style>
    <Footer class="footer">
        <p>Made with ❤️ by <a href="https://x.com/photofola" classname="link">Dev Akintola</a> using Streamlit.</p>
    </Footer>
    """,
    unsafe_allow_html=True,
)