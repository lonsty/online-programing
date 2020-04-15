# Author: Allen
# Date: 2020-4-15 20:29:47

"""
密码验证合格程序

密码要求:
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有相同长度超2的子串重复
"""

import re


def is_valid_password(passwd):
    if len(passwd) <= 8:
        return False
    
    kind = 0
    if re.search(r'[0-9]', passwd):
        kind += 1
    if re.search(r'[a-z]', passwd):
        kind += 1
    if re.search(r'[A-Z]', passwd):
        kind += 1
    if re.search(r'[^0-9a-zA-Z\s]', passwd):
        kind += 1
    
    if kind < 3:
        return False
    
    triples = [passwd[i: i+3] for i in range(len(passwd) - 2)]
    if len(triples) > len(set(triples)):
        return False
    
    return True


while 1:
    try:
        passwd = input()
        if not passwd:
            break
        
        if is_valid_password(passwd):
            print('OK')
        else:
            print('NG')
    except:
        break
