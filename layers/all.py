#!/usr/bin/env python
"""
@author:       ALIF FUSOBAR
@nockname:     Xcod3bughunt3r
@license:      MIT FUCK LICENSE
@contact:      master@itsecurity.id
"""


from scapy.config import conf
from scapy.error import log_loading
import logging
log = logging.getLogger("scapy.loading")

def _import_star(m):
    mod = __import__(m, globals(), locals())
    for k,v in mod.__dict__.iteritems():
        globals()[k] = v

for _l in conf.load_layers:
    log_loading.debug("Loading layer %s" % _l)
    try:
        _import_star(_l)
    except Exception,e:
	log.warning("can't import layer %s: %s" % (_l,e))




