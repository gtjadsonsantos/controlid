from .const import (
    DOMAIN
)

from .doors import (
    open_remote_door,
    access,
    lock,
    unlock
)

def setup(hass, config):

    hass.services.register(DOMAIN, "open_remote_door", open_remote_door)
    hass.services.register(DOMAIN, "access", access)
    hass.services.register(DOMAIN, "lock", lock)
    hass.services.register(DOMAIN, "unlock", unlock)

    return True
