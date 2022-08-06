#!/usr/bin/env python
"""
@author:       ALIF FUSOBAR
@nockname:     Xcod3bughunt3r
@license:      MIT FUCK LICENSE
@contact:      master@itsecurity.id
"""


try:
    import Crypto
except ImportError:
    import logging
    log_loading = logging.getLogger("scapy.loading")
    log_loading.info("Can't import python Crypto lib. Disabled certificate manipulation tools")
else:
    from scapy.crypto.cert import *
