import streamlit as st
from google import genai
import os
from dotenv import load_dotenv
import time 
from streamlit_option_menu import option_menu


# Load environment variables from .env file
load_dotenv()

# Initialize the genai client
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY not found. Please check your .env file.")
    st.stop()

# Initialize the genai client
client = genai.Client(api_key=GOOGLE_API_KEY)

#  horizontal navbar
selected = option_menu(
    menu_title=None,
    options=["Home", "About", "Contact"],
    icons=["house", "info-circle", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)
# Page Content



if selected == "About":
    st.title("About Page")
    st.write("""
    This application leverages **Google GenAI** to generate AI-driven responses. 
    It is built using **Streamlit**, an open-source framework for creating interactive web applications in Python.
    
    **Features:**
    - AI-powered text generation using Google's Gemini model.
    - User-friendly interface with live updates.
    - Feedback mechanism to improve response quality.
    
    **Technologies Used:**
    - Python
    - Streamlit
    - Google GenAI API
    - dotenv for environment variable management
    """)

if selected == "Contact":
    st.title("Contact Page")
    st.write("""
    If you have any inquiries or feedback, feel free to reach out through the following channels:
    
    🔗 **LinkedIn:** [ Dev Akintola ](https://www.linkedin.com/in/tope-akintola-b47b381b9/)  
    🐦 **Twitter:** [@Photofola](https://x.com/photofola)
    
    Love to hear your feedback and look forward to hearing from you!
    """)

# Streamlit app
if selected == "Home":
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