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
