import streamlit as st
from api_requests import api_requests

st.markdown("""
    <style>
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
                     
st.title("Delete Item by Item Number")
item_number = st.text_input("Enter Item Number to Delete:")
if st.button("Delete Item"):
    if item_number:
        try:
            response = api_requests.execute_delete_item(st.session_state["jwt_token"],item_number)
            if response.status_code == 204:
                st.success(f"Item with ID {item_number} deleted successfully!")
            else:
                st.error(f"Failed to delete item with ID {item_number}. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter an item number.")

if st.button("Logout"):
    st.session_state.clear()
    st.success("Logged out successfully!")
    st.switch_page("main.py")
