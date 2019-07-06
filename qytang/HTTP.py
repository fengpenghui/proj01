#! /usr/bin/env python3
# coding: utf-8
# github: https://github.com/fengpenghui
# 码云: https://gitee.com/fengpenghui0923

import os,re,time

while 1:
    time.sleep(1)
    result = os.popen("netstat -tunlp").read()
    i = re.findall('0.0.0.0:80', result)
    if i == ['0.0.0.0:80']:
        print('HTTP(TCP/80)服务已经被打开')
        break
    else:
        print('等待一秒重新开始监控:')

