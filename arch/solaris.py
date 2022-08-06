#!/usr/bin/env python
"""
@author:       ALIF FUSOBAR
@nockname:     Xcod3bughunt3r
@license:      MIT FUCK LICENSE
@contact:      master@itsecurity.id
"""


# IPPROTO_GRE is missing on Solaris
import socket
socket.IPPROTO_GRE = 47

LOOPBACK_NAME="lo0"

from unix import *
