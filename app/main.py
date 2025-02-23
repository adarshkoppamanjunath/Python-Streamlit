import streamlit as st
import time
from api_requests import api_requests

def authenticate(username, password):
    response = api_requests.execute_token_login(username,password)
    if response.status_code == 201:
        return response.json().get("access_token")
    return None

def main():
    st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")
    st.markdown("""
        <style>
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-size: 20px;
            border-radius: 10px;
            width: 100%;
            padding: 10px;
        }
        .stTextInput > div > div > input {
            font-size: 18px;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("📦 Inventory Management Login")
    st.subheader("Please enter your credentials")
    
    username = st.text_input("Username", key="username")
    password = st.text_input("Password", type="password", key="password")
    
    if st.button("Login"):
        with st.spinner("Authenticating..."):
            time.sleep(1)
            token = authenticate(username, password)
            if token:
                st.success("Login successful! Redirecting...")
                st.session_state["authenticated"] = True
                st.session_state["jwt_token"] = token
                time.sleep(1)
                st.switch_page("pages/homepage.py")  # Navigate to home page
            else:
                st.error("Invalid username or password")

if __name__ == "__main__":
    main()
