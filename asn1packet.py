#!/usr/bin/env python
"""
@author:       ALIF FUSOBAR
@nockname:     Xcod3bughunt3r
@license:      MIT FUCK LICENSE
@contact:      master@itsecurity.id
"""


from packet import *

class ASN1_Packet(Packet):
    ASN1_root = None
    ASN1_codec = None    
    def init_fields(self):
        flist = self.ASN1_root.get_fields_list()
        self.do_init_fields(flist)
        self.fields_desc = flist    
    def self_build(self):
        return self.ASN1_root.build(self)    
    def do_dissect(self, x):
        return self.ASN1_root.dissect(self, x)
        

