import collections
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
给定一个 N 叉树，返回其节点值的后序遍历。
"""


def postorder(root: 'Node') -> List[int]:
    if root is None:
        return []
    stack, res = [root], []
    while stack:
        tmp = stack.pop()
        stack.append(tmp.children)
        res.append(tmp.val)
    return res[::-1]


def postorder_recurse(root: 'Node') -> List[int]:
    if not root:
        return []
    res = []
    for node in root.children:
        res.extend(postorder_recurse(node))
    res.append(root.val)
    return res


root = Node(1, [Node(3, [Node(5, []), Node(6, [])]), Node(2, []), Node(4, [])])
##################################################################################

"""
给定一个 N 叉树，返回其节点值的前序遍历。
"""


def pre_order(root: 'Node') -> List[int]:
    if not root:
        return []
    queue, res = [root], []
    while queue:
        tmp_node = queue.pop(0)
        if tmp_node:
            res.append(tmp_node.val)
            for node in tmp_node.children[::-1]:
                res.insert(0, node)
    return res


def pre_order_recurse(root: 'Node') -> List[int]:
    if not root:
        return []
    res = []
    res.append(root.val)
    for child in root.children:
        res.extend(pre_order_recurse(child))
    return res


"""
给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。
"""


def level_order(root):
    if not root:
        return []
    queue, res = [(root, 0)], [[]]
    while queue:
        tmp, level = queue.pop(0)
        if len(res) <= level:
            res.append([])
        res[level].append(tmp.val)
        for node in root.children:
            queue.append((node, level + 1))
    return res


"""
给定一个二叉树的根节点 root ，返回它的 中序 遍历。
"""


def inorder_traversal(root: TreeNode) -> List[int]:
    stack, res = [root], []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        if stack:
            tmp = stack.pop()
            res.append(tmp.val)
            root = tmp.right
    return res


def inorder_traversal_recurse(root: TreeNode) -> List[int]:
    def in_order(root):
        if not root:
            return None
        in_order(root.left)
        res.append(root.val)
        in_order(root.right)

    res = []
    in_order(root)
    return res


"""
给定一个二叉树的根节点 root ，返回它的前序遍历。
"""


def preorder_traversal(root: TreeNode) -> List[int]:
    stack, res = [root], []
    while stack or root:
        while root:
            res.append(root.val)
            root = root.left
            stack.append(root)
        if stack:
            tmp = stack.pop()
            root = tmp.right
    return res


def preorder_traversal_recurse(root: TreeNode) -> List[int]:
    def pre_order(root):
        if not root:
            return None
        res.append(root.val)
        pre_order(root.left)
        pre_order(root.right)

    res = []
    return res


"""
给定一个二叉树的根节点 root ，返回它的后序遍历。
"""


def postorder_traversal(root: TreeNode) -> List[int]:
    master, slave, res = [root], [], []
    while master:
        tmp = master.pop()
        res.append(tmp.val)
        if tmp.left:
            master.append(tmp.left)
        if tmp.right:
            master.append(tmp.right)
    while slave:
        res.append(slave.pop().val)
    return res


"""
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数
"""


def nth_ugly_number(n: int) -> int:
    res, a, b, c = [1] * n, 0, 0, 0
    for i in range(1, n):
        a2, b3, c5 = res[a] * 2, res[b] * 3, res[c] * 5
        res[i] = min(a2, b3, c5)
        if res[i] == a2: a += 1
        if res[i] == b3: b += 1
        if res[i] == c5: c += 1
    return res[-1]


"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
"""


def top_k_frequent(nums, k):
    from collections import Counter
    dic = Counter(nums)
    tmp = [(v, dic[v]) for v in dic]
    tmp.sort(key=lambda tmp: tmp[1], reverse=True)
    res = [tmp[i][0] for i in range(k)]
    return res


def top_k_frequent_heap(nums, k):
    def adjust_down(num_list, root, k):
        val = num_list[root]
        while root << 1 < k:
            child = root << 1
            if child | 1 < k and num_list[child | 1][1] < num_list[child | 1]:
                child |= 1
            if num_list[child][1] < val[1]:
                num_list[root] = num_list[child]
                root = child
            else:
                break
        num_list[root] = val

    def adjust_up(num_list, child):
        val = num_list[child]
        while child >> 1 > 0 and num_list[child >> 1][1]:
            num_list[child] = num_list[child >> 1]
            child >> 1
        num_list[child] = val

    stat = collections.Counter(nums)
    stat = list(stat.items())
    heap = [(0, 0)]

    for i in range(k):
        heap.append(stat[i])
        adjust_up(heap, len(heap) - 1)

    for i in range(k, len(stat)):
        if stat[i][1] > heap[1][1]:
            heap[1] = stat[i]
            adjust_down(heap, 1, k + 1)
    return [item[0] for item in heap[1:]]


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
