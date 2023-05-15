from homeassistant import config_entries, core
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.discovery import load_platform
from collections import defaultdict

import voluptuous as vol
import homeassistant.helpers.config_validation as cv
import logging
from .const import *

from homeassistant.const import CONF_PORT, Platform
from selve import Gateway

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_PORT): cv.string,
    }),
}, extra=vol.ALLOW_EXTRA)


SELVE_PLATFORMS = [
    Platform.COVER
]


async def async_setup_entry(
    hass: core.HomeAssistant, entry: config_entries.ConfigEntry
):
    """Set up the Selve components from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN].setdefault(GATEWAYS_KEY, {})

    # Connect to Selve Gateway
    selve_gateway = await hass.async_add_executor_job(
        Gateway,
        entry.data[CONF_PORT],
        False
    )

    hass.data[DOMAIN][GATEWAYS_KEY][entry.entry_id] = selve_gateway

    device_registry = dr.async_get(hass)
    device_registry.async_get_or_create(
        config_entry_id=entry.entry_id,
        identifiers={(DOMAIN, entry.unique_id)},
        manufacturer="Selve",
        name=entry.title,
    )

    await hass.config_entries.async_forward_entry_setups(entry, SELVE_PLATFORMS)

    return True


class SelveDevice(Entity):
    """Representation of a Selve device entity."""

    def __init__(self, selve_device):
        """Initialize the device."""
        self.selve_device = selve_device
        self._name = self.selve_device.name

    @property
    def unique_id(self):
        """Return the unique id base on the id returned by Selve."""
        return self.selve_device.iveoID

    @property
    def name(self):
        """Return the name of the device."""
        return self._name

    @property
    def extra_state_attributes(self):
        """Return the state attributes of the device."""
        return {'selve_device_id': self.selve_device.iveoID}
