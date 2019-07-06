#! /usr/bin/env python3
# coding: utf-8
# github: https://github.com/fengpenghui
# 码云: https://gitee.com/fengpenghui0923


# import logging
#
# logging.getLogger('kamene.runtime').setLevel(logging.ERROR)
# from kamene.all import *
#
# def qytang_ping(ip):
#     ping_pkt = IP(dst=ip,ttl=1) / ICMP()
#     ping_result = sr1(ping_pkt, timeout=2, verbose=False)
#     if ping_result:
#         return ip, 1
#     else:
#         return ip, 0
#
#
# if __name__ == '__main__':
#     result = qytang_ping('10.1.1.1')
#     if result[1]:
#         print(result[0], '通!')
#     else:
#         print(result[0], '不通!')


import paramiko


def qytang_ssh(ip,username,passwd,port=22,cmd='ls'):
    ssh = paramiko.SSHClient()  # 初始化参数
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy) # 公钥不存在时，自动添加
    ssh.connect(hostname=ip,username=user,password=passwd,timeout=5,compress=True)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x


if __name__ == '__main__':
    print(qytang_ssh('10.1.1.12','root','P@ssw0rd'))
    print(qytang_ssh('10.1.1.12','root','P@ssw0rd',cmd='pwd'))