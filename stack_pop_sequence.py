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
