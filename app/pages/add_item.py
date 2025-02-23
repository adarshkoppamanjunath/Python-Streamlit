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
        
st.title("Add Inventory Item")
with st.form(key="add_item_form"):
    item_name = st.text_input("Item Name", "")
    item_description = st.text_area("Item Description", "")
    item_price = st.number_input("Price ($)", min_value=0.0, format="%.2f")
    submit_button = st.form_submit_button(label="Add Item")
    
if submit_button:
    new_item = {
        "item_name": item_name,
        "item_price": item_price,
        "item_description": item_description
    }
    response = api_requests.execute_add_new_item(st.session_state["jwt_token"],new_item)
    if response.status_code == 201:
        st.success("Item added successfully!")
        st.json(response.json())

if st.button("Logout"):
    st.session_state.clear()
    st.success("Logged out successfully!")
    st.switch_page("main.py")

