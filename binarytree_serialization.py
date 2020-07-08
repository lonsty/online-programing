"""
题目描述
二叉树序列化可以基于先序/中序/后序/按层等遍历方式进行。

现输入二叉树层次遍历序列，请输出其前序遍历序列。

如有二叉树如下：
0
/ \
1   2
/     \
3       4
\     /
5   6
其层次遍历序列为：0, 1, 2, 3, #, #, 4, #, 5, 6, #
其先序遍历序列为：0, 1, 3, #, 5, #, #, #, 2, #, 4, 6, #, #, #
（其中空用"#"代替）

输入描述:
第一行输入数字N为层次遍历结点个数
接下来以层次遍历顺序输入N行节点的值（空用"#"代替）

输出描述:
先序遍历结果（空打印为"#"）
"""

def bfsorder_to_tree(serialised, null='N'):
    container = [null]
    leaves = [[container, 0]]

    for value in serialised:
        children, child_idx = leaves.pop(0)
        if value != null:
            node = children[child_idx] = {
                "value": value,
                "children": [null, null]
            }
            
            leaves.append([node["children"], 0])
            leaves.append([node["children"], 1])
        if len(leaves) == 0:
            break 

    return container[0] # 返回根节点


def preorder_traversal(root):
    if root == '#':
        preorder_serialised.append('#')

    if isinstance(root, dict):
        preorder_serialised.append(root.get('value'))
        preorder_traversal(root.get('children')[0])
        preorder_traversal(root.get('children')[1])


if __name__ == '__main__':
    n = int(input().strip())
    bfsorder_serialised = [input().strip() for _ in range(n)]
    
    tree = bfsorder_to_tree(bfsorder_serialised, null='#')
    preorder_serialised = []
    preorder_traversal(tree)

    print('\n'.join(preorder_serialised))
