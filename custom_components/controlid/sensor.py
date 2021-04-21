
from homeassistant.const import TEMP_CELSIUS
from homeassistant.core import HomeAssistant
from requests import post
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.helpers.typing import ConfigType
from homeassistant.components.sensor import SensorEntity
from typing import  Callable
from datetime import timedelta



import logging
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from .helper import auth

from .const import (
    CONFIG_USERNAME,
    CONFIG_PASSWORD,
    CONFIG_DOORID,
    CONFIG_IP,
    CONFIG_NAME,
    CONFIG_ICON,
    DEFAULT_ICON
)

SCAN_INTERVAL = timedelta(seconds=2)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONFIG_NAME): cv.string,
        vol.Required(CONFIG_IP): cv.string,
        vol.Required(CONFIG_USERNAME):cv.string,
        vol.Optional(CONFIG_ICON,default=DEFAULT_ICON):cv.string,
        vol.Required(CONFIG_DOORID): cv.string,
        vol.Required(CONFIG_PASSWORD): cv.string
    }
)

LOGGER = logging.getLogger(__name__)

def setup_platform(hass:HomeAssistant,config:ConfigType, async_add_entities: Callable,discovery_info=None):

    name = config.get(CONFIG_NAME)
    ip = config.get(CONFIG_IP)
    username = config.get(CONFIG_USERNAME)
    password = config.get(CONFIG_PASSWORD)
    doorid = config.get(CONFIG_DOORID)
    icon = config.get(CONFIG_ICON)

    data = ControlidData(hass=hass,name=name,ip=ip,username=username,password=password,doorid=doorid)

    async_add_entities([ControlidSensor(
        hass=hass,
        name=name,
        ip=ip,
        username=username,
        password=password,
        doorid=doorid,
        icon=icon,
        data=data
    )]) 


class ControlidSensor(SensorEntity):

    def __init__(self,hass:HomeAssistant,name:str,ip:str,username:str,password:str,doorid:str,icon:str,data):
        self._state = None
        self._name:str = name
        self._ip:str = ip
        self._username:str = username
        self._password:str = password
        self._doorid:str = doorid
        self._hass:HomeAssistant = hass
        self._data:ControlidData = data
        self._icon:str = icon

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def icon(self):
        return self._icon

    def update(self):
       self._data.update()
       self._state = self._data._state
    
class ControlidData:
   def __init__(self,hass:HomeAssistant,name:str,ip:str,username:str,password:str,doorid:str):
        self._state = None
        self._name:str = name
        self._ip:str = ip
        self._username:str = username
        self._password:str = password
        self._doorid:str = doorid
        self._hass:HomeAssistant = hass
        
   def update(self):
        session =  auth(self._ip,self._username,self._password)
        response = post("http://{ip}/doors_state.fcgi?session={session}".format(ip=self._ip,session=session)).json() 

        for door in response["doors"]:
            if (door["id"] == int(self._doorid)):
                self._state = door["open"]
