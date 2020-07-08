"""
题目描述
有A、B、C、D、E、F 6个城市，假如某人驾车，A到B需要12个小时，C到D需要3个小时，B到C需要10个小时，D到E需要4个小时，C到F需要6个小时，F到A需要16个小时，E到F需要2个小时，B到F需要7个小时，C到E需要5个小时，求任意给定的两地之间的最佳驾驶路线。

输入描述:
ABCDEF中任意两个字母，以空格隔开

输出描述:
第一行输出最短时间

第二行输出最佳路线

示例1
输入
C E

输出
5
C E

备注:
按顺序输出代表城市的字母，并以空格隔开
"""

class DijkstraPath():
    def __init__(self, node, node_ls):
        self.node_map = [[0 for _ in range(len(node))] for _ in range(len(node))]
        for x, y, val in node_list:
            self.node_map[node.index(x)][node.index(y)] = val
            self.node_map[node.index(y)][node.index(x)] = val
        self.node_len = len(node)
        self.used_node_list = []
        self.collected_node_dict = {}
    
    def solve(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node
        self._init_dijkstra()
        return self._format_path()
    
    def _init_dijkstra(self):
        self.used_node_list.append(self.from_node)
        # 假设起始节点为-1, 则从from_node到起始节点距离为0
        self.collected_node_dict[self.from_node] = [0, -1]
        for node_index, dic in enumerate(self.node_map[self.from_node]):
            # 如果可到达
            if dic:
                self.collected_node_dict[node_index] = [dic, self.from_node]
        self._foreach_dijkstra()
    
    # 迭代
    def _foreach_dijkstra(self):
        if len(self.used_node_list) == self.node_len - 1:
            return
        for key in list(self.collected_node_dict.keys()):
            val = self.collected_node_dict[key]
            if key not in self.used_node_list and key != to_node:
                self.used_node_list.append(key)
            else:
                continue
            for node_index, dic in enumerate(self.node_map[key]):
                # 更新成较小距离的点
                if dic and node_index in self.collected_node_dict and self.collected_node_dict[node_index][0] > dic + val[0]:
                    self.collected_node_dict[node_index][0] = dic + val[0]
                    self.collected_node_dict[node_index][1] = key
                elif dic and node_index not in self.collected_node_dict:
                    self.collected_node_dict[node_index] = [dic + val[0], key]
        self._foreach_dijkstra()
    
    def _format_path(self):
        node_list = []
        temp_node = self.to_node
        node_list.append((temp_node, self.collected_node_dict[temp_node][0]))
        # 从终点往回查找
        while self.collected_node_dict[temp_node][1] != -1:
            temp_node = self.collected_node_dict[temp_node][1]
            node_list.append((temp_node, self.collected_node_dict[temp_node][0]))
        node_list.reverse()
        return node_list


if __name__ == '__main__':
    node = ['A', 'B', 'C', 'D', 'E', 'F']
    node_list = [('A', 'B', 12), ('C', 'D', 3), ('B', 'C', 10),
                 ('D', 'E', 4), ('C', 'F', 6), ('F', 'A', 16),
                 ('E', 'F', 2), ('B', 'F', 7), ('C', 'E', 5)]
    inp = input().split(' ')
    from_node = node.index(inp[0])
    to_node = node.index(inp[1])
    dijkstraPath = DijkstraPath(node, node_list)
    path = dijkstraPath.solve(from_node, to_node)
    
    if len(path) == 1:
        path *= 2
    
    print(path[-1][-1])
    print(' '.join([node[p] for p, _ in path]))
