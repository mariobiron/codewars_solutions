# Your task is to return the list with elements from tree sorted by levels, which means the root element goes first,
# then root children (from left to right) are second and third, and so on.
#
# Return empty list if root is None.

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def go_through_tree(node,level,pos,da_list):
    if node.value != None:
        da_list.append([level,pos,node.value])
    if node.left != None:
        go_through_tree(node.left,level+1,(pos+1)*10,da_list)
    if node.right != None:
        go_through_tree(node.right,level+1,(pos+1)*10,da_list)

def tree_by_levels(node):
    return_array = []
    working_array = []
    lvl = 0
    final_list = []
    if node != None:
        go_through_tree(node, lvl, 0, working_array)
        final_list = sorted(working_array, key=lambda x: (x[0], x[1]))
        for x,y,z in final_list:
            return_array.append(z)
    return return_array


print(tree_by_levels(None)) #, []
print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1))) #, [1, 2, 3, 4, 5, 6]
print(tree_by_levels(Node(Node(None, Node(None, None, None), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1))) #, [1, 2, 3, 4, 5, 6]

# from collections import deque
#
#
# def tree_by_levels(node):
#     if not node:
#         return []
#     res, queue = [], deque([node,])
#     while queue:
#         n = queue.popleft()
#         res.append(n.value)
#         if n.left is not None:
#             queue.append(n.left)
#         if n.right is not None:
#             queue.append(n.right)
#     return res

# def tree_by_levels(node):
#     p, q = [], [node]
#     while q:
#         v = q.pop(0)
#         if v is not None:
#             p.append(v.value)
#             q += [v.left,v.right]
#     return p if not node is None else []

# def tree_by_levels(tree):
#     queue = [tree]
#     values = []
#
#     while queue:
#         node = queue.pop(0)
#         if node:
#             queue += [node.left, node.right]
#             values.append(node.value)
#
#     return values