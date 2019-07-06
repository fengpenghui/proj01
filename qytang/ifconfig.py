#! /usr/bin/env python3
# coding: utf-8
# github: https://github.com/fengpenghui
# 码云: https://gitee.com/fengpenghui0923

import re

ifconfig_result = 'ens32: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500\n         inet 10.1.1.12  netmask 255.255.255.0  broadcast 10.1.1.255\n        inet6 fe80::cd81:9670:2bc7:66b9  prefixlen 64  scopeid 0x20<link>\n        ether 00:0c:29:12:87:8d  txqueuelen 1000  (Ethernet)\n        RX packets 96837  bytes 145045176 (138.3 MiB)\n        RX errors 0  dropped 0  overruns 0  frame 0\n        TX packets 72627  bytes 4655646 (4.4 MiB)\n        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0\n\n'

re_findall_result =  re.findall('([0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2})',ifconfig_result)



ip = re.findall('.*inet (.*)  netmask',ifconfig_result)

brodcast = ('')

netmask =


# print('MAC地址为:',re_findall_result[0])
