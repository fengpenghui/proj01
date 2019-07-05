
from qytang_ssh import qytang_ssh
import re

def ssh_get_route(ip,username,password):
    Gateway =  re.findall('0.0.0.0\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+0.0.0.0\s+UG',qytang_ssh(ip,username,password,cmd='route -n'))
    return Gateway[0]

if __name__ == '__main__':
    print(qytang_ssh('10.1.1.12','root','P@ssw0rd'))
    print(qytang_ssh('10.1.1.12','root','P@ssw0rd',cmd='pwd'))
    print('网关为：')
    print(ssh_get_route('10.1.1.12','root','P@ssw0rd'))