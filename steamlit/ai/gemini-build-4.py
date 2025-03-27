from logging import warn
from narwhals import col
import streamlit as st
from google import genai
import os
from dotenv import load_dotenv
import time 
from streamlit_option_menu import option_menu


# Load environment variables from .env file
load_dotenv()

# Load API key from Streamlit Secrets
GOOGLE_API_KEY = st.secrets["general"]["GOOGLE_API_KEY"]

# # Initialize the genai client
if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY not found. Please check your .env file.")
    st.stop()



@st.cache_resource
def get_genai_client():
    return genai.Client(api_key=GOOGLE_API_KEY)

# Initialize the genai client
client = get_genai_client()


# navbar
# Check if screen width is small (mobile)
is_mobile = int(st.query_params.get("width", ["1080"])[0]) < 600

page = option_menu(
    menu_title=None,
    options=["Home", "About", "Contact", "Chat history"],
    icons=["house", "info-circle", "envelope", "clock-history"],
    menu_icon="cast",
    default_index=0,
     styles= {
        "container": {"padding": "0!important", "background-color": "#fafafa"} if is_mobile else {},
        "icon": { "font-size": "5px"} if is_mobile else {"font-size": "20px"}, 
        "nav-link": {"font-size": "1px", "margin":"0px", "--hover-color": "#eee"} if is_mobile else {"font-size": "18px","text-align": "center"},
    },
    orientation="vertical" if is_mobile else "horizontal",
)

# Streamlit app
st.title("Imọran-ai with Streamlit")

if page == "Home":
   with st.container():
    # Initialize session state for history, response and prompt
    if "thumbs_up_clicked" not in st.session_state:
        st.session_state.thumbs_up_clicked = False
    if "thumbs_down_clicked" not in st.session_state:
        st.session_state.thumbs_down_clicked = False
    if "response" not in st.session_state:
        st.session_state.response = ""
    if "prompt" not in st.session_state:
        st.session_state.prompt = ""
    if "history" not in st.session_state:
        st.session_state.history = []
    

    def generate_response():
        if st.session_state.prompt.strip():
            with st.spinner("Generating response..."):
                try:
                    response = client.models.generate_content(
                        model="gemini-2.0-flash", contents=st.session_state.prompt
                    )
                    st.session_state.response = response.text
                    st.session_state.history.append({"User Prompt": st.session_state.prompt, "AI Response": st.session_state.response})
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a prompt.")

    # User input with Enter key submission
    st.text_area("Enter a prompt:", value=st.session_state.prompt, key="prompt", on_change=generate_response)


    col1, col2 = st.columns(2)
    # Button for manual generation
    with col1:
        if st.button("Generate Response"):
            generate_response()
    with col2:
        if st.button("Clear Response"):
            st.session_state.response = ""
            success_placeholder = st.empty()
            success_placeholder.success("Response cleared successfully.")
            time.sleep(5)  # Wait for 5 seconds
            success_placeholder.empty()  # Remove the success message
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
                success_placeholder = st.empty()
                success_placeholder.success("Thank you for your feedback!")
                time.sleep(5)  # Wait for 5 seconds
                success_placeholder.empty()

        with col2:
            if st.button("👎 Thumbs Down"):
                st.session_state.thumbs_down_clicked = True
                warning_placeholder = st.empty()
                warning_placeholder.warning("Feedback noted. We’ll work on improving the responses.")
                time.sleep(5)   # Wait for 5 seconds
                warning_placeholder.empty()

    # Trigger balloons if thumbs up was clicked
    if st.session_state.thumbs_up_clicked:
        st.balloons()
        time.sleep(1)
        st.session_state.thumbs_up_clicked = False
    #trigger snow if thumbs down was clicked
    if st.session_state.thumbs_down_clicked:
        st.snow()
        time.sleep(1)
        st.session_state.thumbs_down_clicked = False
# Page Content
elif page == "About":
    st.title("About Page")
    st.write("""
    
     **Why the name 'Imọran-AI'?**
    
    "Imọran" is a Yoruba word that means *wisdom*, *insight*, or *guidance*. The purpose of **Imoran-AI** is to provide smart, insightful, and meaningful responses powered by AI, mimicking the wisdom of a knowledgeable guide.
    
    This AI-driven platform is built using **Google GenAI** and **Streamlit**, ensuring a seamless and interactive experience for users looking for intelligent conversations, AI-generated insights, and more.
    
    **Key Features:**
    - AI-powered text generation using Google's Gemini model.
    - Instant responses to various prompts with live feedback.
    - Simple and intuitive UI for seamless user experience.
    
    Whether you're seeking knowledge, insights, or just engaging AI interactions, **Imoran-AI** is designed to bring wisdom to your fingertips.
    
    **Technologies Used:**
    - Python
    - Streamlit
    - Google GenAI API
    - dotenv for environment variable management
    """)

elif page == "Contact":
    st.title("Contact Page")
    st.write("""
    If you have any inquiries or feedback, feel free to reach out through the following channels:
    
    🔗 **LinkedIn:** [ Dev Akintola ](https://www.linkedin.com/in/tope-akintola-b47b381b9/)  
    🐦 **Twitter:** [@Photofola](https://x.com/photofola)
    
    Love to hear your feedback and look forward to hearing from you!
    """)
elif page == "Chat history":
    st.title("Conversation History")
    st.write("""
    **Session History:**
    """)
    if st.session_state.history:
        for i, item in enumerate(st.session_state.history):
            with st.expander(f"Conversation {i+1}", expanded=False):
                st.write(f"**User Prompt:** {item['User Prompt']}")
                st.write(f"**AI Response:** {item['AI Response']}")
        # Clear history button
        if st.button("Clear History"):
            st.session_state.history = []
            success_placeholder = st.empty()
            success_placeholder.success("History cleared successfully.")
            time.sleep(2)  # Wait for 2 seconds
            success_placeholder.empty() 
            st.rerun()
    else:
        st.info("No history available.")

    


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