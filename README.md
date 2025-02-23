# Inventory Management Streamlit App

## Overview

This is a Streamlit-based application for **inventory management** with features such as:

- **Add Item**: Add new items to the inventory.
- **View and Update Item**: View item details and update them.
- **Delete Item**: Delete items from the inventory by entering the item number.
- **Token Authentication**: The app supports **JWT token authentication** to secure access to CRUD operations.

## Features

### 1. **Add Item**
- Allows users to add items to the inventory by filling out a form with the following fields:
  - Item Name
  - Price
  - Stock Quantity
  - Description
- Upon successful submission, the item is added to the inventory.

### 2. **View and Update Item**
- Displays details of an existing item based on its ID.
- Users can update the following fields:
  - Item Name
  - Price
  - Stock Quantity
  - Description
- Changes are saved via an API call and the updated details are displayed.

### 3. **Delete Item**
- Users can delete an item by entering its **Item Number**.
- Upon deletion, a success message is shown, or an error message is displayed if the item is not found or deletion fails.

### 4. **Token Authentication**
- The app uses **JWT tokens** for user authentication.
- If the token is expired, the user is automatically redirected to the **login page**.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/inventory-management-streamlit.git
cd inventory-management-streamlit
