
from homeassistant.const import TEMP_CELSIUS
from homeassistant.core import HomeAssistant
from requests import post
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.helpers.typing import ConfigType
from homeassistant.components.sensor import SensorEntity
import logging
from typing import  Callable
from datetime import timedelta


import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from .helper import auth

from .const import (
    CONFIG_USERNAME,
    CONFIG_PASSWORD,
    CONFIG_DOORID,
    CONFIG_IP,
    CONFIG_NAME
)

SCAN_INTERVAL = timedelta(seconds=15)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONFIG_NAME): cv.string,
        vol.Required(CONFIG_IP): cv.string,
        vol.Required(CONFIG_USERNAME):cv.string,
        vol.Required(CONFIG_DOORID): cv.string,
        vol.Required(CONFIG_PASSWORD): cv.string
    }
)

def setup_platform(hass:HomeAssistant,config:ConfigType, async_add_entities: Callable,discovery_info=None):

    name = config.get(CONFIG_NAME)
    ip = config.get(CONFIG_IP)
    username = config.get(CONFIG_USERNAME)
    password = config.get(CONFIG_PASSWORD)
    doorid = config.get(CONFIG_DOORID)

    async_add_entities([ControlidSensor(
        name=name,
        ip=ip,
        username=username,
        password=password,
        doorid=doorid
    )]) 


class ControlidSensor(SensorEntity):

    def __init__(self,name:str,ip:str,username:str,password:str,doorid:str):
        self._state = None
        self._name:str = name
        self._ip:str = ip
        self._username:str = username
        self._password:str = password
        self._doorid:str = doorid

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    async def async_update(self):
        session = await auth(self.ip,self.username,self.password)
        response = await post("http://{ip}/doors_state.fcgi?session={session}".format(ip=self._ip,session=session)).json() 

        for door in response["doors"]:
            if (door["id"] == int(self.doorid)):
                self._state = door["open"]
        
        
