
import logging
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)
from kamene.all import *

def qytang_ping(ip):
    ping_pkt = IP(dst=ip)/ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return ip, True

if __name__ == '__main__':
    print(qytang_ping('10.1.1.1'))
