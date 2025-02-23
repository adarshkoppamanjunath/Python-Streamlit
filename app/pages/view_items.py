import streamlit as st
from api_requests import api_requests

st.markdown("""
    <style>
        .stTextInput > div > div > input {
            font-size: 20px;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ddd;
        }
        .stButton > button {
            background-color: #6200ea;
            color: white;
            border-radius: 5px;
            font-size: 16px;
            padding: 10px 20px;
        }
        .stButton > button:hover {
            background-color: #3700b3;
        }
        .stJson {
            font-family: "Courier New", Courier, monospace;
            background-color: #f7f7f7;
            padding: 15px;
            border-radius: 5px;
            border: 1px solid #ddd;
        }
    </style>
""", unsafe_allow_html=True)

if "jwt_token" not in st.session_state:
        st.warning("You must log in first!")
        st.stop()
        
st.title("View All Item Information")

if st.button("View All Items"):
    response = api_requests.execute_view_all_items(st.session_state["jwt_token"])
    if response.status_code == 200:
        st.json(response.json()["all_items"])
    else:
        st.error("An error occurred while fetching items.")
        
item_number = st.text_input("Enter Item Number:", "")
if st.button("Fetch Item Data"):
    if item_number:
        response = api_requests.execute_view_item(st.session_state["jwt_token"],item_number)
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("An error occurred while fetching items.")
    else:
        st.warning("Please enter an item number.")

if st.button("Logout"):
    st.session_state.clear()
    st.success("Logged out successfully!")
    st.switch_page("main.py")

