import json
import uuid

import streamlit as st
import requests
from requests.auth import HTTPBasicAuth

from utils import get_file_id

# Retrieve API credentials from Streamlit secrets
CLIENT_ID = st.secrets["CLIENT_ID"]
SECRET = st.secrets["SECRET"]


def get_access_token() -> str:
    """
    Request an access token from the Sberbank API.
    """
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': str(uuid.uuid4()),
    }
    payload = {"scope": "GIGACHAT_API_PERS"}

    # Make a POST request to retrieve the access token
    res = requests.post(
        url=url,
        headers=headers,
        auth=HTTPBasicAuth(CLIENT_ID, SECRET),
        data=payload,
        verify=False, # Disable SSL verification
    )

    # Extract and return the access token from the response
    access_token = res.json()["access_token"]
    return access_token


def get_image(file_id: str, access_token: str):
    """
    Retrieve an image from the GigaChat API using the file ID.
    """
    url = f"https://gigachat.devices.sberbank.ru/api/v1/files/{file_id}/content"

    payload = {}
    headers = {
        'Accept': 'application/jpg',
        'Authorization': f'Bearer {access_token}'
    }

    # Make a GET request to fetch the image
    response = requests.get(url, headers=headers, data=payload, verify=False)
    return response.content


def send_prompt(msg: str, access_token: str):
    """
    Send a text prompt to the GigaChat API and receive a response.
    """
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    payload = json.dumps({
        "model": "GigaChat-Pro",
        "messages": [
            {
                "role": "user",
                "content": msg,
            }
        ],
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    # Make a POST request to send the user prompt
    response = requests.post(url, headers=headers, data=payload, verify=False)

    # Extract and return the chatbot's response
    return response.json()["choices"][0]["message"]["content"]


def sent_prompt_and_get_response(msg: str, access_token: str):
    """
        Send a prompt to the chatbot and determine if the response is an image or text.
    """
    res = send_prompt(msg, access_token)
    data, is_image = get_file_id(res)

    # If the response is an image, fetch the image content
    if is_image:
        data = get_image(file_id=data, access_token=access_token)
    return data, is_image