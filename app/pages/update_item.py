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

st.title("View and Update Item Details")
item_id = st.text_input("Enter Item ID", "")
if item_id:
    response = api_requests.execute_view_item(st.session_state["jwt_token"],item_id)
    if response.status_code == 200:
        item_data = response.json()
        st.subheader("Item Details")
        st.write(f"**Name**: {item_data['item_name']}")
        st.write(f"**Price**: ${item_data['item_price']:.2f}")
        st.write(f"**Description**: {item_data['item_description']}")
        with st.form(key="update_item_form"):
            updated_name = st.text_input("Item Name", item_data['item_name'])
            updated_price = st.number_input("Price ($)", min_value=0.0, value=item_data['item_price'], format="%.2f")
            updated_description = st.text_area("Item Description", item_data['item_description'])
            submit_button = st.form_submit_button(label="Update Item")
        if submit_button:
            updated_item = {
                "item_name": updated_name,
                "item_price": updated_price,
                "item_description": updated_description
            }
            update_response = api_requests.execute_update_item(st.session_state["jwt_token"],item_id,updated_item)
            if update_response.status_code == 204:
                st.success("Item updated successfully!")
            else:
                st.error(f"Failed to update item: {update_response.status_code}")
    else:
        st.error("Item not found or invalid ID!")
        
if st.button("Logout"):
    st.session_state.clear()
    st.success("Logged out successfully!")
    st.switch_page("main.py")
