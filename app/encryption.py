from cryptography.fernet import Fernet
import os

def get_cipher():
    key = os.getenv("ENCRYPTION_KEY").encode()
    return Fernet(key)

def encrypt_token(token: str) -> str:
    return get_cipher().encrypt(token.encode()).decode()

def decrypt_token(encrypted_token: str) -> str:
    return get_cipher().decrypt(encrypted_token.encode()).decode()
