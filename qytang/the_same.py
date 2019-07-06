#! /usr/bin/env python3
# coding: utf-8
# github: https://github.com/fengpenghui
# 码云: https://gitee.com/fengpenghui0923

list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

print("方案一：")
for x in list1:
     if x in list2:
             print(x,'in List1 and List2')
     else:
         print(x,'only in List1')
print('='*30)

print("方案二：")
def findsame(list1,list2):
    for x in list1:
        if x in list2:
            print(x,'in List1 and List2')
        else:
            print(x,'only in List1')

findsame(list1,list2)

if __name__ == '__main__':
    pass
