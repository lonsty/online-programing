"""
题目描述
已知某一个字母序列，把序列中的字母按出现顺序压入一个栈，在入栈的任意过程中，允许栈中的字母出栈，求所有可能的出栈顺序

输入描述:
字符串，如：abc

输出描述:
可能的出栈顺序，每行一种顺序

示例1
输入
abc

输出
abc
acb
bac
bca
cba
"""
class Solution:
    def __init__(self, to_push):
        # to_push为入栈字符串或序列
        self.to_push = to_push
        self.n = len(to_push)
        self.result = []

    def all_unstack(self, i, stack, popped):

        if i == self.n:
            if stack:
                top = stack.pop()
                popped.append(top)
                self.all_unstack(i, stack, popped)
                stack.append(top)  # 回溯
                popped.pop()
            else:
                self.result.append(''.join(popped))
        else:
            # 对于一个输入元素，可以入栈；可以不入，弹出栈中已有元素
            # 入栈
            stack.append(self.to_push[i])
            self.all_unstack(i + 1, stack, popped)
            stack.pop()  # 回溯

            # 出栈
            if stack:
                top = stack.pop()
                popped.append(top)
                self.all_unstack(i, stack, popped)
                popped.pop()  # 回溯
                stack.append(top)

    def print_all_sequence(self):
        for each in self.result[::-1]:
            print(each)


if __name__ == '__main__':
    to_push = input().strip()
    solution = Solution(to_push)
    solution.all_unstack(0, [], [])
    solution.print_all_sequence()
    
# =================== 方法二 ======================
# @Author: allen
# @Date: Jul 11 18:35 2020
from copy import copy
from typing import List

def print_stack_pop_seq(to_push: List[int], n,
                        stack: List[int],
                        popped: List[int]):
    if n <= 0 or (not to_push and not stack and not popped):
        return

    if len(popped) == n:
        while len(popped):
            print(popped.pop(0), end=' ')
        print()
        return

    stack_copy = copy(stack)
    popped_copy = copy(popped)

    if stack:
        popped.append(stack.pop())
        print_stack_pop_seq(copy(to_push), n, stack, popped)

    if to_push:
        stack_copy.append(to_push.pop(0))
        print_stack_pop_seq(copy(to_push), n, stack_copy, popped_copy)


if __name__ == '__main__':
    to_push = [1, 2, 3, 4]
    n = len(to_push)
    stack = []
    popped = []

    print_stack_pop_seq(to_push, n, stack, popped)
