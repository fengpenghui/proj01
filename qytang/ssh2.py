#! /usr/bin/env python3
# coding: utf-8
# github: https://github.com/fengpenghui
# 码云: https://gitee.com/fengpenghui0923
import paramiko


def qytang_ssh(ip,user,passwd,port=22,cmd='ls'):
    ssh = paramiko.SSHClient()  # 初始化参数
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy) # 公钥不存在时，自动添加
    ssh.connect(hostname=ip,username=user,password=passwd,timeout=5,compress=True)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x


if __name__ == '__main__':
    print(qytang_ssh('10.1.1.2','houmm','packet'))
    print(qytang_ssh('10.1.1.2','houmm','packet',cmd='pwd'))