import secrets

def custom_id():
    return secrets.token_urlsafe(8)