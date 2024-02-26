n = int(input())

keys = [int(i) for i in input().split()]


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.child = 0  # total children


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)  # create left child
    else:
        root.right = insert(root.right, key)

    root.child += 1

    return root


root = None
for key in keys:
    root = insert(root, key)


def count_balance_node(root):
    if root is None or (root.left == None and root.right == None):
        return 0

    if root.left == None:
        return count_balance_node(root.right)
    elif root.right == None:
        return count_balance_node(root.left)

    is_balance = 0
    if root.left.child == root.right.child:
        is_balance = 1
    else:
        is_balance = 0

    return is_balance + count_balance_node(root.left) + count_balance_node(root.right)


print(count_balance_node(root))
