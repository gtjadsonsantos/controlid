
from requests import post
from homeassistant.core import ServiceCall
import json

from .helper import auth



def open_remote_door(call:ServiceCall):
    ip = call.data.get("ip", "")
    username = call.data.get("username", "")
    password = call.data.get("password", "")
    actions = call.data.get("actions", [])

    headers = {"Content-Type": "application/json"}

    payload = {'actions': actions}

    post("http://"+ip+"/execute_actions.fcgi?session="+auth(ip,username, password), data=json.dumps(payload), headers=headers)


def access(call:ServiceCall):
    ip = call.data.get("ip", "")
    username = call.data.get("username", "")
    password = call.data.get("password", "")
    actions = call.data.get("actions", [])

    headers = {"Content-Type": "application/json"}

    payload = {'actions': actions}

    post("http://"+ip+"/execute_actions.fcgi?session="+auth(ip,username, password), data=json.dumps(payload), headers=headers)


def unlock(call: ServiceCall):
    ip = call.data.get("ip", "")
    username = call.data.get("username", "")
    password = call.data.get("password", "")
    actions = call.data.get("actions", [])

    headers = {"Content-Type": "application/json"}

    payload = {'actions': actions}

    post("http://"+ip+"/execute_actions.fcgi?session="+auth(ip,username, password), data=json.dumps(payload), headers=headers)
    


def lock(call: ServiceCall):
    ip = call.data.get("ip", "")
    username = call.data.get("username", "")
    password = call.data.get("password", "")
    actions = call.data.get("actions", [])

    headers = {"Content-Type": "application/json"}

    payload = {'actions': actions}

    post("http://"+ip+"/execute_actions.fcgi?session="+auth(ip,username, password), data=json.dumps(payload), headers=headers)