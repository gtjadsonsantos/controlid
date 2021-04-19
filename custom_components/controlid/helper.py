from requests import post

def auth(ip: str, login: str, password: str) -> str:
    
    payload = {"login": login, "password": password }
    
    url = f"http://{ip}/login.fcgi"

    response = post(url,data=payload, timeout=10).json()

    return response["session"]