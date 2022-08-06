#!/usr/bin/env python
"""
@author:       ALIF FUSOBAR
@nockname:     Xcod3bughunt3r
@license:      MIT FUCK LICENSE
@contact:      master@itsecurity.id
"""


from scapy.fields import *
from scapy.packet import *
from scapy.layers.inet import IP

class GPRS(Packet):
    name = "GPRSdummy"
    fields_desc = [
        StrStopField("dummy","","\x65\x00\x00",1)
        ]


bind_layers( GPRS,          IP,            )
