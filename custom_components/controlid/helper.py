from requests.api import request


from requests import post

async def auth(ip: str, login: str, password: str) -> str:
    response = post("http://"+ip+"/login.fcgi",data={"login": login, "password": password}).json()
    return response["session"]