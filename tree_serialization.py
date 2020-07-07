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
