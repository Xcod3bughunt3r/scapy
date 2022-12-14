#!/usr/bin/env python
"""
@author:       ALIF FUSOBAR
@nockname:     Xcod3bughunt3r
@license:      MIT FUCK LICENSE
@contact:      master@itsecurity.id
"""


import getopt

def usage():
    print >>sys.stderr,"""Usage: check_asdis -i <pcap_file> [-o <wrong_packets.pcap>]
    -v   increase verbosity
    -d   hexdiff packets that differ
    -z   compress output pcap
    -a   open pcap file in append mode"""

def main(argv):
    PCAP_IN = None
    PCAP_OUT = None
    COMPRESS=False
    APPEND=False
    DIFF=False
    VERBOSE=0
    try:
        opts=getopt.getopt(argv, "hi:o:azdv")
        for opt, parm in opts[0]:
            if opt == "-h":
                usage()
                raise SystemExit
            elif opt == "-i":
                PCAP_IN = parm
            elif opt == "-o":
                PCAP_OUT = parm
            elif opt == "-v":
                VERBOSE += 1
            elif opt == "-d":
                DIFF = True
            elif opt == "-a":
                APPEND = True
            elif opt == "-z":
                COMPRESS = True
                
                
        if PCAP_IN is None:
            raise getopt.GetoptError("Missing pcap file (-i)")
    
    except getopt.GetoptError,e:
        print >>sys.stderr,"ERROR: %s" % e
        raise SystemExit
    
    

    from scapy.config import conf
    from scapy.utils import RawPcapReader,RawPcapWriter,hexdiff
    from scapy.layers import all


    pcap = RawPcapReader(PCAP_IN)
    pcap_out = None
    if PCAP_OUT:
        pcap_out = RawPcapWriter(PCAP_OUT, append=APPEND, gz=COMPRESS, linktype=pcap.linktype)
        pcap_out._write_header(None)

    LLcls = conf.l2types.get(pcap.linktype)
    if LLcls is None:
        print >>sys.stderr," Unknown link type [%i]. Can't test anything!" % pcap.linktype
        raise SystemExit
    
    
    i=-1
    differ=0
    failed=0
    for p1,meta in pcap:
        i += 1
        try:
            p2d = LLcls(p1)
            p2 = str(p2d)
        except KeyboardInterrupt:
            raise
        except Exception,e:
            print "Dissection error on packet %i" % i
            failed += 1
        else:
            if p1 == p2:
                if VERBOSE >= 2:
                    print "Packet %i ok" % i
                continue
            else:
                print "Packet %i differs" % i
                differ += 1
                if VERBOSE >= 1:
                    print repr(p2d)
                if DIFF:
                    hexdiff(p1,p2)
        if pcap_out is not None:
            pcap_out.write(p1)
    i+=1
    correct = i-differ-failed
    print "%i total packets. %i ok, %i differed, %i failed. %.2f%% correct." % (i, correct, differ,
                                                                                failed, i and 100.0*(correct)/i)
    
        
if __name__ == "__main__":
    import sys
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print >>sys.stderr,"Interrupted by user."
