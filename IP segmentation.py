"""
题目描述
一个数字段由首尾两个数字标识，表示一个自然数集合，
比如数字段[beg, end)表示从beg到end之间的所有自然数，
包含beg，但不包含end。

有若干个数字段，这些数字段之间可能有重叠，
怎么把这些数字段合并去重，用最少个数的数字段来表示。

合并前后，整个集合包含的数字不发生变化。


输入描述:
第一行为数字N，表示接下来有N个数字段(N<=100000)
第二行开始一共有N行，每行两个数字，分别表示一个数字段的beg和end
(beg和end为无符号32位整数)
输出描述:
合并去重后形成的数字段集合，按升序排列。
"""
# ------------------------------ 方法一：超时 ---------------------------
from itertools import groupby
from operator import itemgetter

n = int(input())  # 数字段个数
seq = set()  # 自然数序列

for i in range(n):
    seq.update(range(*map(int, input().split())))

seq = sorted(seq)

# 连续自然数分段
# segs = [list(map(itemgetter(1), g)) for k, g in groupby(enumerate(seq), lambda x: x[0] - x[1])]

spl = [0] + [i for i in range(1, len(seq)) if seq[i] - seq[i-1] > 1] + [None]
segs = [seq[b:e] for (b, e) in [(spl[i-1], spl[i]) for i in range(1, len(spl))]]
for seg in segs:
    print(seg[0], seg[-1] + 1)

# ------------------------------- 方法一 --------------------------------
n = int(input().strip())
array = []

for i in range(n):
    array.append(list(map(int, input().split())))

array.sort(key=lambda x: (x[0], -x[1]))
result = [array[0]]

for i in range(1, len(array)):
    a, b = result[-1]
    start, end = array[i]
    if start == b:
        result[-1] = [a, end]
    elif start > b:
        result.append([start, end])
    else:
        result[-1] = [a, max(b, end)]

for line in result:
    print(line[0], line[1])
