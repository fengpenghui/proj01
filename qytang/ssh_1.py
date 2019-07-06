#! /usr/bin/env python3
# coding: utf-8
# github: https://github.com/fengpenghui
# 码云: https://gitee.com/fengpenghui0923

import paramiko

def qytang_ssh(ip,username,passwd,port=22,cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port=22,username=username,password=password,timeout=5,compress=True)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x


if __name__ == '__main__':
    print(qytang_ssh('10.1.1.12','root','P@ssw0rd'))
    print(qytang_ssh('10.1.1.12','root','P@ssw0rd',cmd='pwd'))