from kamene.all import *
import logging
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)


def qytang_ping(ip):
    ping_pkt = IP(dst=ip)/ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return 1
    else:
        return 0

import paramiko


def qytang_ssh(ip, username, password, port=22, cmd='sh ip int b'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x


if __name__ == '__main__':
    print(qytang_ssh('192.168.2.11', 'cisco', 'cisco', ))




if __name__ == '__main__':
    result = qytang_ping('10.1.1.12')
    print(result)

from ping import ping
from ssh import ssh
import re
import pprint


def qytang_get_if(*ips, username='root', password='P@ssw0rd'):
    device_if_dict = {}
    for ip in ips:
        if qytang_ping(ip):
           if_ip_dict = {}
           result = ssh(ip, username, password)
           result_if = re.findall('(\w+|\w+/\d+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+', result)
           for i in range(len(result_if)):
               if_ip_dict.update({result_if[i][0]: result_if[i][1]})
           device_if_dict.update({ip: if_ip_dict})
        else:
            device_if_dict.update({ip: {}})
    return device_if_dict


if __name__ == '__main__':
    pprint.pprint(qytang_get_if('192.168.247.161', '192.168.247.162', username='cisco', password='cisco'), indent=4)
