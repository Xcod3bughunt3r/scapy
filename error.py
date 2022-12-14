#!/usr/bin/env python
"""
@author:       ALIF FUSOBAR
@nockname:     Xcod3bughunt3r
@license:      MIT FUCK LICENSE
@contact:      master@itsecurity.id
"""


#############################
##### Logging subsystem #####
#############################

class Scapy_Exception(Exception):
    pass

import logging,traceback,time

class ScapyFreqFilter(logging.Filter):
    def __init__(self):
        logging.Filter.__init__(self)
        self.warning_table = {}
    def filter(self, record):        
        from config import conf
        wt = conf.warning_threshold
        if wt > 0:
            stk = traceback.extract_stack()
            caller=None
            for f,l,n,c in stk:
                if n == 'warning':
                    break
                caller = l
            tm,nb = self.warning_table.get(caller, (0,0))
            ltm = time.time()
            if ltm-tm > wt:
                tm = ltm
                nb = 0
            else:
                if nb < 2:
                    nb += 1
                    if nb == 2:
                        record.msg = "more "+record.msg
                else:
                    return 0
            self.warning_table[caller] = (tm,nb)
        return 1    

log_scapy = logging.getLogger("scapy")
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
log_scapy.addHandler(console_handler)
log_runtime = logging.getLogger("scapy.runtime")          # logs at runtime
log_runtime.addFilter(ScapyFreqFilter())
log_interactive = logging.getLogger("scapy.interactive")  # logs in interactive functions
log_loading = logging.getLogger("scapy.loading")          # logs when loading scapy


def warning(x):
    log_runtime.warning(x)

