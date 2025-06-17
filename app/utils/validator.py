import requests

user_service_url = "http://127.0.0.1:5000/users"

def validate_user(user_id):
    try:
        response = requests.get(f"{user_service_url}/{user_id}")
        if response.status_code != 200:
            return False
        return True
    except Exception:
        return False