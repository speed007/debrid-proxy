import os
import requests
from .encryption import encrypt_token, decrypt_token

def authenticate_rd():
    """Simple API key authentication"""
    api_key = os.getenv("RD_API_KEY")
    if not api_key:
        raise ValueError("Real-Debrid API key not configured")
    
    # Verify the API key works
    response = requests.get(
        "https://api.real-debrid.com/rest/1.0/user",
        headers={"Authorization": f"Bearer {api_key}"}
    )
    response.raise_for_status()
    return response.json()
