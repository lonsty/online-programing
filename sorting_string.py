# Author: Allen
# Date: 2020-4-16 22:06:53
"""
编写一个程序，将输入字符串中的字符按如下规则排序。
规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
如，输入： Type 输出： epTy
规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
如，输入： BabA 输出： aABb
规则 3 ：非英文字母的其它字符保持原来的位置。
如，输入： By?e 输出： Be?y
"""


def sort_string(string):
    chars = [c for c in string if 'a' <= c.lower() <= 'z']
    reversed_chars = list(reversed(sorted(chars, key=lambda x: x.lower())))
    sorted_ = [reversed_chars.pop() if 'a' <= c.lower() <= 'z' else c for c in string]
    return ''.join(sorted_)


while 1:
    try:
        string = input()
        if not string:
            break
        print(sort_string(string))
    except:
        break
