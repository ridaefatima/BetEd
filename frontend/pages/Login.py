import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase Admin SDK if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate('../beted-83806-firebase-adminsdk-1k71h-c002aa1ad7.json')
    firebase_admin.initialize_app(cred)

# Initialize session state for authentication
if "auth_state" not in st.session_state:
    st.session_state.auth_state = False  # Default to not logged in

# Sidebar Login/Signup functionality
def authenticate_user():
    st.sidebar.title("BetEd Authentication")

    if st.session_state.auth_state:
        # Display logout button when the user is logged in
        st.sidebar.success("You are logged in!")
        if st.sidebar.button("Logout"):
            st.session_state.auth_state = False  # Set auth state to logged out
            st.sidebar.warning("You have logged out.")
            #st.experimental_rerun()  # Refresh the app to reflect logout
    else:
        # Display login/signup options when the user is not logged in
        auth_choice = st.sidebar.radio("Login/Sign Up", ["Login", "Sign Up"])

        if auth_choice == "Login":
            email = st.sidebar.text_input("Email Address", key="login_email")
            password = st.sidebar.text_input("Password", type="password", key="login_password")
            if st.sidebar.button("Login"):
                try:
                    user = auth.get_user_by_email(email)
                    st.session_state.auth_state = True  # Set auth state to logged in
                    st.sidebar.success(f"Welcome back, {email}!")
                    #st.experimental_rerun()  # Refresh the app to show logged-in state
                except Exception as e:
                    st.sidebar.error("Login failed. Please check your credentials.")
        else:
            email = st.sidebar.text_input("Email Address", key="signup_email")
            password = st.sidebar.text_input("Password", type="password", key="signup_password")
            username = st.sidebar.text_input("Enter your unique username", key="signup_username")
            if st.sidebar.button("Sign Up"):
                try:
                    user = auth.create_user(email=email, password=password, uid=username)
                    st.sidebar.success("Account created successfully! Please log in.")
                except Exception as e:
                    st.sidebar.error(f"Sign up failed: {e}")

# Call the authentication function in the sidebar
authenticate_user()

# Example page content
if st.session_state.auth_state:
    st.title("Welcome to BetEd!")
    st.write("You are logged in. Enjoy exploring the platform.")
else:
    st.title("Welcome to BetEd!")
    st.write("Please log in or sign up using the sidebar to access more features.")
