"""
Support for Selve cover - shutters etc.
"""
from custom_components.selve import SelveDevice
import logging

from homeassistant.components.cover import CoverEntity

from .const import DOMAIN, GATEWAYS_KEY, SELVE_CLASSTYPES, SELVE_SUPPORTED_FEATURES


from typing import Callable, Optional
from homeassistant.helpers.typing import (
    ConfigType,
    DiscoveryInfoType,
    HomeAssistantType,
)


_LOGGER = logging.getLogger(__name__)

def setup_platform(
    hass: HomeAssistantType,
    config: ConfigType,
    add_entities: Callable,
    discovery_info: Optional[DiscoveryInfoType] = None,
) -> None:
    """Set up Selve covers."""    
    devices = [ SelveCover(device,SELVE_CLASSTYPES.get(device.device_type.value)) for device in hass.data[DOMAIN]['devices']['cover']]    
    add_entities(devices)


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Perform the setup for Selve devices."""
    entities = []
    gateway = hass.data[DOMAIN][GATEWAYS_KEY][config_entry.entry_id]
    gateway.discover()
    for device in list(gateway.devices.values()): #TODO filter by type cover
        device_type = SELVE_CLASSTYPES.get(device.device_type.value)
        if device_type is None:
            _LOGGER.warning('Unsupported type %s for Selve device %s',
                            device.device_type, device.name)
            continue
        entities.append( SelveCover(device, device_type))
            
    async_add_entities(entities)



class SelveCover(SelveDevice, CoverEntity):
    """Representation a Selve Cover."""

    def __init__(self, selve_device, device_type):
        super().__init__(selve_device)
        self._device_type = device_type

    def update(self):
        """Update method."""
        self.selve_device.discover_properties()
    
    @property
    def supported_features(self):
        """Flag supported features."""
        return SELVE_SUPPORTED_FEATURES

    @property
    def current_cover_position(self):
        """
        Return current position of cover.
        0 is closed, 100 is fully open.
        """
        return 50
    
    @property
    def current_cover_tilt_position(self):
        """
        Return current position of cover.
        0 is closed, 100 is fully open.
        """
        return 50
 
    @property
    def is_closed(self):
        """Return if the cover is closed."""
        # if self.current_cover_position is not None:
        #     return self.current_cover_position == 0
        return None

    @property
    def device_class(self):
        """Return the class of the device.""" 
        return self._device_type
    

    def open_cover(self, **kwargs):
        """Open the cover."""
        self.selve_device.moveUp() 

    def open_cover_tilt(self, **kwargs):
        """Open the cover."""
        # Using tilt for intermediate positions
        self.selve_device.moveIntermediatePosition1()        

    def close_cover(self, **kwargs):
        """Close the cover."""
        self.selve_device.moveDown()  

    def close_cover_tilt(self, **kwargs):
        """Open the cover."""
        # Using tilt for intermediate positions
        self.selve_device.moveIntermediatePosition2()        

    def stop_cover(self, **kwargs):
        """Stop the cover."""
        self.selve_device.stop()
    
    def stop_cover_tilt(self, **kwargs):
        """Stop the cover."""
        self.selve_device.stop()
    
        
