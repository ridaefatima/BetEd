import streamlit as st
from pages.Login import authenticate_user

authenticate_user()

# Check if the user is authenticated
if "auth_state" in st.session_state and st.session_state.auth_state:
    st.title('Profile')
    st.write("Welcome to your profile page!")
else:
    st.warning("You need to log in to access this page.")
    st.stop()
