#! /usr/bin/env python3
# coding: utf-8
# github: https://github.com/fengpenghui
# 码云: https://gitee.com/fengpenghui0923


import paramiko
import time

def qytang_multicmd(ip, username, password, cmd_list, enable='', wait_time=2, verbose=True):
    ssh = paramiko.SSHClient()    # 创建SSH Client
    ssh.load_system_host_keys()   # 加载系统SSH密钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # 添加新的SSH密钥
    ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)   # SSH连接
    chan = ssh.invoke_shell()  # 激活交互式shell
    time.sleep(1)   # 等待网络设备回应
    x = chan.recv(2048).decode()   # 获取路由器返回的信息,2048为缓存大小
    if enable and '>' in x: #判断enable和>是否在回显x中
        chan.send('enable'.encode())   # 发送命令
        chan.send(b'\n') # 回车
        chan.send(enable.encode())  # 发送命令
        chan.send(b'\n')  # 回车
        time.sleep(wait_time)
    elif not enable and '>' in x:  #没有传enable密码，>在x中
        print('需要配置enable密码！')
        return
    for cmd in cmd_list:
        chan.send(cmd.encode())
        chan.send(b'\n')
        time.sleep(wait_time)
        x = chan.recv(40960).decode()  # 获取路由器返回的信息
        if verbose:
            print(x)
    chan.close()
    ssh.close()

if __name__ == '__main__':
    qytang_multicmd ('192.168.2.11',
                     'cisco',
                     'cisco',
                     ['terminal length 0',#显示完整show内容
                     # 'show version',
                      'show ip int br',
                      'config ter',
                      'int e0/1',
                      'ip add 192.168.1.2 255.255.255.0',
                      'do show ip int br'],
                    enable= 'cisco',
                    wait_time=1,
                    verbose= True  #False静默执行
                     )