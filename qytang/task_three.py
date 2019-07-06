#! /usr/bin/env python3
# coding: utf-8
# github: https://github.com/fengpenghui
# 码云: https://gitee.com/fengpenghui0923


import re

str1 = '166    54a2.74f7.0326    DYNAMIC     Gi1/0/11'

result = re.match('(\d{1,3})\s+([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\s+(\w+)\s+(\w.*\d)',str1).groups()

print('-'*50)
print('%-10s : %s' % ('VLAN ID', result[0]))
print('%-10s : %s' % ('MAC', result[1]))
print('%-10s : %s' % ('Type', result[2]))
print('%-10s : %s' % ('Interface', result[3]))