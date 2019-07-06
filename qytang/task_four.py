#! /usr/bin/env python3
# coding: utf-8
# github: https://github.com/fengpenghui
# 码云: https://gitee.com/fengpenghui0923


import re

str1 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09,bytes 27575949, flags UIO'

result = re.match('(\w*)\s+(\w*)\s+((\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,3}))\s+(\w*)\s+((\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})),\s*(\w*)\s+(\d{1,3}):(\d{1,3}):(\d{1,3}),\s*(\w*)\s*(\d{1,8}),\s*(\w*)\s*(\w*)',str1).groups()

print('-'*50)
print('%-12s : %s' % ('protocol', result[0]))
print('%-12s : %s' % ('server', result[2]))
print('%-12s : %s' % ('localserver', result[6]))
print('%-12s : %-2s小时 %-2s分钟 %-2s秒' % ('idle', result[10],result[11],result[12]))
print('%-12s : %s' % ('bytes', result[14]))
print('%-12s : %s' % ('flags', result[16]))


