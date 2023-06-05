[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)
# homeassistant-selve
Home Assistant Custom component to manage Selve devices through the usb-rtf gateway.

Underline ut uses the [python-selve library](https://github.com/gpulido/python-selve) so refer to it for the Selve devices limitations.


## Installing
The component comply with [HACS](https://github.com/hacs/integration), although it is not published on it, it can be installed as a [custom repository](https://hacs.xyz/docs/faq/custom_repositories)

After being installed through hacs, it can be added as an integration in Home Assistant.

Plug a gateway on the same pc where Home assistant is running, check for the usb interface (for example /dev/ttyUSB0) and use it as configuration when requested in the workflow integration.

