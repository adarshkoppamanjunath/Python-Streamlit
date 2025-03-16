import streamlit as st
from api_requests import api_requests

def main():
    st.set_page_config(page_title="Home", page_icon="🏠", layout="centered")
    st.title("📦 Inventory Management System")
    st.markdown("""
        <style>
        .stButton > button {
            background-color: #008CBA;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    if "jwt_token" not in st.session_state:
        st.warning("You must log in first!")
        st.stop()
    response= api_requests.execute_secure_data_jwt_admin(st.session_state['jwt_token'])
    st.subheader(f"Welcome, {response.json()['Username']}. Choose an action below!")
    if st.button("🔍 View Inventory"):
        st.switch_page("pages/view_items.py")
    if st.button("➕ Add Item"):
        st.switch_page("pages/add_item.py")
    if st.button("✏️ Update Item"):
        st.switch_page("pages/update_item.py")
    if st.button("🗑️Delete Item"):
        st.switch_page("pages/delete_item.py")
   
    
    if st.button("Logout"):
        st.session_state.clear()
        st.success("Logged out successfully!")
        st.switch_page("main.py")

if __name__ == "__main__":
    main()
