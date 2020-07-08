"""
题目描述
设计实现一个LRU（Least Recently Used）缓存器

LRU有如下两个方法：
int get(int key) - 从缓存中取值，返回key对应的value（值总是一个正数）， 如不存在返回 -1。
void set(int key, int value) - 往缓存中存键值对。 当缓存达到容量限制时，令“最近最少使用” 的键值对失效。

根据输入内容操作该LRU缓存器，输出LRU缓存器每个get的结果。

例如：
缓存器容量为3；
set(1, 2)
set(2, 3)
set(3, 4)
get(1) 返回 2
get(4) 返回 -1
set(4, 5)
get(2) 返回 -1

输入描述:
第一行输入两个数N L（N>0, L>0），N为缓存器容量，L为接下来输入的行数

接下来输入L行：

(1) 对应get操作，输入格式为"g %d"；

(2) 对应set操作，输入格式为"s %d %d"，前一个数为key，后一个为value。

输出描述:
输出每次get操作的返回值，一次一行。
"""

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.dict = OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dict:
            return -1
        v = self.dict.pop(key) 
        self.dict[key] = v   # set key as the newest one
        return v

    def set(self, key, value):
        if key in self.dict:    
            self.dict.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1  
            else:  # self.dic is full
                self.dict.popitem(last=False) 
        self.dict[key] = value

n, lines = map(int, input().strip().split())
lru_cache = LRUCache(n)

for _ in range(lines):
    args = input().strip().split()[1:]
    if len(args) > 1:
        lru_cache.set(*args)
    else:
        print(lru_cache.get(args[0]))
