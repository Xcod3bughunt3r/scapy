#!/usr/bin/env python
"""
@author:       ALIF FUSOBAR
@nockname:     Xcod3bughunt3r
@license:      MIT FUCK LICENSE
@contact:      master@itsecurity.id
"""


from scapy.packet import *
from scapy.fields import *
from scapy.layers.inet import IP

IPPROTO_VRRP=112

# RFC 3768 - Virtual Router Redundancy Protocol (VRRP)
class VRRP(Packet):
    fields_desc = [
        BitField("version" , 2, 4),
        BitField("type" , 1, 4),
        ByteField("vrid", 1),
        ByteField("priority", 100),
        FieldLenField("ipcount", None, count_of="addrlist", fmt="B"),
        ByteField("authtype", 0),
        ByteField("adv", 1),
        XShortField("chksum", None),
        FieldListField("addrlist", [], IPField("", "0.0.0.0"),
                       count_from = lambda pkt: pkt.ipcount),
        IntField("auth1", 0),
        IntField("auth2", 0) ]

    def post_build(self, p, pay):
        if self.chksum is None:
            ck = checksum(p)
            p = p[:6]+chr(ck>>8)+chr(ck&0xff)+p[8:]
        return p

bind_layers( IP,            VRRP,          proto=IPPROTO_VRRP)
