#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01
# blog: https://houm01.com

import re
import random


number = random.randint(0,84)

with open('CCIE-RS1') as f:
    text = f.read()
    result = re.findall('(\d、[\s\S]*?)markmark', text)[number]
    result2 = re.match('(.*)\n', result).groups()[0]
    result3 = result.replace(result2, '')
    result4 = result3.split('\n')
    result5 = random.shuffle(result4)

    print(result2)
    for x in result4:
        print(x)


