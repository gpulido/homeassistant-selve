DOMAIN = "selve"

GATEWAYS_KEY = "gateways"

from homeassistant.components.cover import (
    #ATTR_POSITION,
    #ATTR_TILT_POSITION,       
    SUPPORT_OPEN, 
    SUPPORT_CLOSE, 
    SUPPORT_STOP,
    SUPPORT_OPEN_TILT, 
    SUPPORT_CLOSE_TILT, 
    #SUPPORT_STOP_TILT, 
    SUPPORT_SET_POSITION, 
    SUPPORT_SET_TILT_POSITION,
    DEVICE_CLASS_WINDOW, 
    DEVICE_CLASS_BLIND, 
    DEVICE_CLASS_AWNING, 
    DEVICE_CLASS_SHUTTER  
)


SERVICE_SET_POS1 = 'selve_set_pos1'
SERVICE_SET_POS2 = 'selve_set_pos2'

#TODO: map the rigth types

SELVE_CLASSTYPES = {
    0:None,
    1:DEVICE_CLASS_SHUTTER,
    2:DEVICE_CLASS_BLIND,
    3:DEVICE_CLASS_SHUTTER,
    4:'cover',
    5:'cover',
    6:'cover',
    7:'cover',
    8:'cover',
    9:'cover',
    10:'cover',
    11:'cover',
}

SELVE_SUPPORTED_FEATURES = SUPPORT_OPEN | SUPPORT_CLOSE | SUPPORT_STOP | SUPPORT_SET_POSITION | SUPPORT_OPEN_TILT | SUPPORT_CLOSE_TILT | SUPPORT_SET_TILT_POSITION