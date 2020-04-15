# Author: Allen
# Date: 2020-4-15 22:47:55
"""
实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都
删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
注意每个输入文件有多组输入，即多个字符串用回车隔开
"""


def remove_least_chars(string):
    counter = {}
    
    for c in string:
        if c not in counter:
            counter[c] = 1
        else:
            counter[c] += 1
    minimum = min(counter.values())
    
    return ''.join([c for c in string if counter[c] != minimum])


while 1:
    try:
        string = input()
        if not string:
            break
        print(remove_least_chars(string))
    except:
        break
