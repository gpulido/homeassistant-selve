DOMAIN = "selve"

GATEWAYS_KEY = "gateways"

from homeassistant.components.cover import CoverDeviceClass, CoverEntityFeature

SERVICE_SET_POS1 = 'selve_set_pos1'
SERVICE_SET_POS2 = 'selve_set_pos2'

#TODO: map the rigth types

SELVE_CLASSTYPES = {
    0:None,
    1:CoverDeviceClass.SHUTTER,
    2:CoverDeviceClass.BLIND,
    3:CoverDeviceClass.SHUTTER,
    4:'cover',
    5:'cover',
    6:'cover',
    7:'cover',
    8:'cover',
    9:'cover',
    10:'cover',
    11:'cover',
}

SELVE_SUPPORTED_FEATURES = (
    CoverEntityFeature.OPEN 
    | CoverEntityFeature.CLOSE 
    | CoverEntityFeature.STOP 
    | CoverEntityFeature.SET_POSITION 
    | CoverEntityFeature.OPEN_TILT 
    | CoverEntityFeature.CLOSE_TILT 
    | CoverEntityFeature.SET_TILT_POSITION
)
