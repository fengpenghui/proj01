#! /usr/bin/env python3
# coding: utf-8
# github: https://github.com/fengpenghui
# 码云: https://gitee.com/fengpenghui0923

from qytang_ssh import qytang_ssh
import re
import hashlib
import time


def qytang_get_config(ip, username='cisco', password='cisco'):
    try:
        config_raw = qytang_ssh(ip, username, password, 22, 'sh run')
        config = ('hostname' + config_raw.split('\nhostname')[1]).split('\nend\s+')[0]
        return config

    except Exception:
        return


def qytang_check_diff(ip, username='cisco', password='cisco'):
    beforce_md5 = ''
    while True:
        m = hashlib.md5()
        m.update(qytang_get_config(ip, username, password,encode())
        current_md5 = m.hexdigest()
        print(current_md5)
        if beforce_md5 and beforce_md5 != current_md5:
            print('MD5 value changed')
            break
        else:
            beforce_md5 = current_md5
        time.sleep(5)


if __name__ == '__main__':
    # print(qytang_get_config('192.168.247.161',username='cisco', password='cisco'))
    qytang_check_diff('192.168.2.11', username='cisco', password='cisco')
