from datetime import datetime, timedelta
import requests
from .encryption import encrypt_token, decrypt_token

def get_fresh_token(user_token):
    if datetime.now() >= user_token["expires_at"] - timedelta(minutes=5):
        response = requests.post(
            "https://api.real-debrid.com/oauth/v2/token",
            data={
                "client_id": os.getenv("RD_CLIENT_ID"),
                "client_secret": os.getenv("RD_CLIENT_SECRET"),
                "grant_type": "refresh_token",
                "refresh_token": decrypt_token(user_token["refresh_token"])
            }
        )
        if response.ok:
            new_token = response.json()
            new_token["expires_at"] = datetime.now() + timedelta(seconds=new_token["expires_in"])
            return encrypt_token(new_token)
    return user_token["access_token"]
