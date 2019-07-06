#! /usr/bin/env python3
# coding: utf-8
# github: https://github.com/fengpenghui
# 码云: https://gitee.com/fengpenghui0923


import re

str1 = 'Port-channel1.189       192.168.189.254     YES   CONFIG    up'

result = re.match('\s*(.*\w\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w*)\s+(\w*)\s+(\w*)\s+(\w*)\s*',str1).groups()

print('-'*100)
print('接口：%-30s'%(result[0]))
print('IP地址：%-30s'%(result[1]))
print('状态：%-30s'%(result[-1]))
