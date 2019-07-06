#! /usr/bin/env python3
# coding: utf-8
# github: https://github.com/fengpenghui
# 码云: https://gitee.com/fengpenghui0923


import paramiko
import re

def qytang_multicmd(ip, username, password, cmd_list, enable='', wait_time=2, verbose=True):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.2.11', port=22, username='cisco', password='cisco', timeout=5, compress=True)
    chan = ssh.invoke_shell()
    time.sleep(1)
    chan.recv(2048).decode()
    chan.send('config ter'.encode())  # 发送命令
    chan.send(b'\n')  # 回车
    x = chan.recv(2048).decode()  # 获取路由器返回的信息
    print(x)  # 打印返回信息
    chan.send('router ospf 1'.encode())
    chan.send(b'\n')
    x = chan.recv(2048).decode()
    print(x)

if __name__ == '__main__':
    cmd_list = ('show version','hostname Test')
    print(qytang_multicmd('192.168.2.11', username='cisco', password='cisco'))