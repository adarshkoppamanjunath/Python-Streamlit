import requests
from requests.auth import HTTPBasicAuth
import json

url = "http://fastapi-service:8000/"

def execute_token_login(username="testuser",password="secret"):
    payload = 'username=%s&password=%s'%(username,password)
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url+"login", headers=headers, data=payload)
    return response
    
def execute_secure_data_jwt_admin(access_token):
    payload={}
    headers = {
    'Authorization': 'Bearer %s'%(access_token)
    }
    response = requests.request("GET", url+"secure-data-jwt-admin", headers=headers, data=payload)
    return response

def execute_add_new_item(access_token,payload):
    payload = json.dumps(payload)
    headers = {
    'Authorization': 'Bearer %s'%(access_token),
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url+"add-new-item", headers=headers, data=payload)
    return response

def execute_view_all_items(access_token):
    payload={}
    headers = {
    'Authorization': 'Bearer %s'%(access_token)
    }
    response = requests.request("GET", url+"get-all-items", headers=headers, data=payload)
    return response

def execute_view_item(access_token,item_id):
    payload={}
    headers = {
    'Authorization': 'Bearer %s'%(access_token)
    }
    response = requests.request("GET", url+"item/"+item_id, headers=headers, data=payload)
    return response

def execute_update_item(access_token,item_id,payload):
    headers = {
    'Authorization': 'Bearer %s'%(access_token),
    'Content-Type': 'application/json'
    }
    payload = json.dumps(payload)
    response = requests.request("PUT", url+"update-item/"+item_id, headers=headers, data=payload)
    return response

def execute_delete_item(access_token,item_id):
    headers = {
    'Authorization': 'Bearer %s'%(access_token),
    'Content-Type': 'application/json'
    }
    response = requests.request("DELETE", url+"delete-item/"+item_id, headers=headers)
    return response