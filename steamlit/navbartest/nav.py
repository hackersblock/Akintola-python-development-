import streamlit as st
from streamlit_option_menu import option_menu

# Create a horizontal navbar
selected = option_menu(
    menu_title=None,
    options=["Home", "About", "Contact"],
    icons=["house", "info-circle", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)
# Create a vertical navbar
selected = option_menu(
    menu_title=None,
    options=["Home", "About", "Contact"],
    icons=["house", "info-circle", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="vertical",
)
#with tabs
tab1, tab2, tab3 = st.tabs(
    ["Home", "About", "Contact"]
)

# Page Content
with tab1:
    st.title("Home Page")
    st.write("Welcome to the Home Page!")
with tab2:
   st.title("About Page")
   st.write("This is an app using Google aGenAI with Streamlit.")
with tab3:
    st.title("Contact Page")
    st.write("Feel free to reach out.")
    

# Sidebar Navigation
st.sidebar.title("Navigation")
selected = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Page Content
if selected == "Home":
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

elif selected == "About":
    st.title("About Page")
    st.write("This is an app using Google aGenAI with Streamlit.")

elif selected == "Contact":
    st.title("Contact Page")
    st.write("Feel free to reach out.")
