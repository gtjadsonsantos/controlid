from requests import post
import json

from .const import (
    DOMAIN
)


def setup(hass, config):
    def auth(ip: str, login: str, password: str):
        response = post("http://"+ip+"/login.fcgi",
                        data={"login": login, "password": password}).json()
        return response["session"]

    def open_remote_door(call):
        ip = call.data.get("ip", "")
        username = call.data.get("username", "")
        password = call.data.get("password", "")
        actions = call.data.get("actions", [])

        headers = {
        "Content-Type": "application/json",
        }

        payload = {
            'actions': actions
        }  
        
        post("http://"+ip+"/execute_actions.fcgi?session="+auth(ip, username, password), data=json.dumps(payload), headers=headers)


    hass.services.register(DOMAIN, "open_remote_door", open_remote_door)

    return True
