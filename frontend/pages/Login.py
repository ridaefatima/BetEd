import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth

# Check if the default app is already initialized

if not firebase_admin._apps:
    cred = credentials.Certificate('../beted-83806-firebase-adminsdk-1k71h-c002aa1ad7.json')
    firebase_admin.initialize_app(cred)


st.sidebar.title('BetEd')

firebaseConfig = {
  'apiKey': "AIzaSyC1tQ8iuQkGsgtpFZsNDkcMp9uruvPHuGc",
  'authDomain': "beted-83806.firebaseapp.com",
  'projectId': "beted-83806",
  'storageBucket': "beted-83806.firebasestorage.app",
  'messagingSenderId': "758279482712",
  'appId': "1:758279482712:web:f5d1aed199bf88e548092d",
  'measurementId': "G-5J78FB98NS"
}

#Authetication
def app():
    st.title('Login')
    choice = st.selectbox("Login/Signup", ["Login", "Sign Up"])
    
    def f():
        try:
            user = auth.get_user_by_email(email)
            st.write('Login successful')
            #print(user.uid)
        except:
            st.warning("Login Failed. User not found.")
    
    
    
    
    if choice == "Login":
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")
        if st.button("Login", on_click=f):
            try:
                user = auth.get_user_by_email(email)
                st.success(f"Logged in successfully! User ID: {user.uid}")
            except:
                st.warning("Login Failed. User not found.")
    else:
        email = st.text_input("Email Address", value='Default')
        password = st.text_input("Password", type="password")
        username = st.text_input("Enter your unique username")
        
        if st.button("Create my account"):
            try:
                user = auth.create_user(
                    email=email,
                    password=password,
                    uid=username,
                    #email_verified=False,
                    #password=password,
                    #display_name=username
                )
                st.success("Account created successfully!")
                st.markdown(f"User ID: {user.uid}")
                st.markdown('Please Login using your email and password.')
                st.balloons()
            except Exception as e:
                st.error(f"Failed to create account: {e}")
                #st.markdown(f"User ID: {user.uid}")

# Call the app function
app()
