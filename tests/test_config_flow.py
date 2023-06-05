"""Tests for the config flow."""
from unittest import mock

import pytest

from custom_components.selve import config_flow
from custom_components.selve.const import DOMAIN

@pytest.mark.asyncio
async def test_flow_user_init(hass):
    """Test the initialization of the form in the first step of the config flow."""
    result = await hass.config_entries.flow.async_init(
        config_flow.DOMAIN, context={"source": "user"}
    )
    expected = {
        "data_schema": config_flow.SELVE_SCHEMA,
        "description_placeholders": None,
        "errors": {},
        "flow_id": mock.ANY,
        "handler": "selve",
        "step_id": "user",
        "type": "form",
    }
    assert expected == result
