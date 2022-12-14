#!/usr/bin/env python
"""
@author:       ALIF FUSOBAR
@nockname:     Xcod3bughunt3r
@license:      MIT FUCK LICENSE
@contact:      master@itsecurity.id
"""


from scapy.fields import *
from scapy.packet import *
from scapy.layers.inet import UDP

class HSRP(Packet):
    name = "HSRP"
    fields_desc = [
        ByteField("version", 0),
        ByteEnumField("opcode", 0, { 0:"Hello", 1:"Coup", 2:"Resign", 3:"Advertise"}),
        ByteEnumField("state", 16, { 0:"Initial", 1:"Learn", 2:"Listen", 4:"Speak", 8:"Standby", 16:"Active"}),
        ByteField("hellotime", 3),
        ByteField("holdtime", 10),
        ByteField("priority", 120),
        ByteField("group", 1),
        ByteField("reserved", 0),
        StrFixedLenField("auth","cisco",8),
        IPField("virtualIP","192.168.1.1") ]
        


        
        
bind_layers( UDP,           HSRP,          dport=1985, sport=1985)
