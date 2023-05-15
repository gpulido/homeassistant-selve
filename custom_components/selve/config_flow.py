import logging
from typing import Any, Dict, Optional

from homeassistant import config_entries, core
from homeassistant.const import CONF_PORT
import homeassistant.helpers.config_validation as cv
import voluptuous as vol

from .const import (
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)

SELVE_SCHEMA = vol.Schema(
    {        
        vol.Required(CONF_PORT, default=7000): cv.string,                        
    }
)

class SelveConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Selve Custom config flow."""

    data: Optional[Dict[str, Any]]

    async def async_step_user(self, user_input: Optional[Dict[str, Any]] = None):
        """Invoked when a user initiates a flow via the user interface."""
        errors: Dict[str, str] = {}
        if user_input is not None:
            from selve import Gateway
            port = user_input[CONF_PORT]                        
            try:
                gat = Gateway(port, False)                
            except:
                errors["base"] = "connection"
            if not errors:
                self.data = user_input

                return self.async_create_entry(title="Selve", data=self.data)

        return self.async_show_form(
            step_id="user", data_schema=SELVE_SCHEMA, errors=errors
        )
