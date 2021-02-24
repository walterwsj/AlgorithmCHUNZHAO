import collections
from typing import List

from collections import Counter

from urllib3.connectionpool import xrange

"""
爬楼梯
"""

dic = {}


def climb_stairs(n: int) -> int:
    if n < 3:
        return n
    else:
        x, y = 0, 0
        if dic.get(n - 1) is not None and dic.get(n - 2) is not None:
            x = dic.get(n - 1)
            y = dic.get(n - 2)
        else:
            x = climb_stairs(n - 1)
            y = climb_stairs(n - 2)
            dic[n - 1] = x
            dic[n - 2] = y
        return x + y


def climb_stairs_1(n: int) -> int:
    if n < 3:
        return n
    x, y = 1, 2
    for i in range(3, n + 1):
        x, y = y, x + y
    return y


"""
位 1 的个数
"""


def hamming_weight(n: int) -> int:
    res = 0
    while n:
        res += n & 1
        n >>= 1
    return res


def hamming_weight_py(n: int) -> int:
    return bin(n).count("1")


"""
2次幂
"""


def is_power_of_two(n: int) -> bool:
    if n == 0:
        return False
    return n & (n - 1) == 0


"""
颠倒二进制位
"""


def reverse_bits_py(n: int) -> int:
    return int('0b' + bin(n)[2:][::-1] + '0' * (32 - len(bin(n)[2:])), 2)


def reverse_bits(n: int) -> int:
    ans, power = 0, 31
    while n:
        ans += (n & 1) >> power
        n >>= 1
        power -= 1
    return ans


"""
生成括号
"""


def generate_parentheses(n):
    if n <= 0:
        return []
    res = []

    def _generate(left, right, s):
        if left > n or right > left:
            return
        if len(s) == n * 2:
            res.append(s)
            return
        if left < n:
            _generate(left + 1, right, s + "(")
        if left > right:
            _generate(left, right + 1, s + ")")

    _generate(0, 0, "")
    return res


"""
数独是否有效
"""


def is_valid_sudoku(self, board: List[List[str]]) -> bool:
    rows, cols, boxes = [{} for i in range(9)], [{} for i in range(9)], [{} for i in range(9)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                num = int(num)
                box_index = (i // 3) * 3 + j // 3

                rows[i][num] = rows[i].get(num, 0) + 1
                cols[j][num] = cols[j].get(num, 0) + 1
                boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                if rows[i][num] > 1 or cols[j][num] > 1 or boxes[box_index][num] > 1:
                    return False
    return True


"""
字典树
"""


class Trie:
    def __int__(self):
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def starts_with(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return True


"""
单词搜索
"""

end_of_word = "#"
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.result = None

    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []
        if not words:
            return []
        self.result = set()
        root = collections.defaultdict()

        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node[end_of_word] = end_of_word

        self.m, self.n = len(board), len(board[0])
        for i in xrange(self.m):
            for j in xrange(self.n):
                if board[i][j] in root:
                    self._dfs(board, i, j, "", root)

        return list(self.result)

    def _dfs(self, board, i, j, current_word, current_dict):
        current_word += board[i][j]
        current_dict = current_dict[board[i][j]]
        if end_of_word in current_dict:
            self.result.add(current_word)
        tmp, board[i][j] = board[i][j], '@'
        for k in xrange(4):
            x, y = i + dx[k], j + dy[k]
            if 0 <= x < self.m and 0 <= y < self.n and board[x][y] != '@' and board[x][y] in current_dict:
                self._dfs(board, x, y, current_word, current_dict)
        board[i][j] = tmp


"""
省份数量
"""


class UnionFind:
    def __init__(self):
        self.father = {}
        self.num_of_sets = 0

    def find(self, x):
        root = x
        while self.father[root] is not None:
            root = self.father[root]

        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father

        return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.num_of_sets -= 1

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.num_of_sets += 1


def find_circle_num(M: List[List[int]]) -> int:
    uf = UnionFind()
    for i in range(len(M)):
        uf.add(i)
        for j in range(i):
            if M[i][j]:
                uf.merge(i, j)

    return uf.num_of_sets


"""
并查集模板
"""


class UnionFindSet:
    def __init__(self):
        self.num_of_sets = 0
        self.father = {}

    def find(self, x):
        root = x
        while self.father[root] is not None:
            root = self.father[root]

        while x != root:
            original_father = self.father[x]
            self.father[x] = None
            x = original_father

        return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.num_of_sets -= 1

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.num_of_sets += 1


"""
island
"""


class UnionFindIsLand:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, x):
        root = x
        while self.parent[root] is not None:
            root = self.parent[root]

        while x != root:
            original_parent = self.parent[x]
            self.parent[x] = None
            x = original_parent
        return root

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.count -= 1

    def getCount(self):
        return self.count


def num_is_lands(grid: List[List[str]]) -> int:
    nr = len(grid)
    if nr == 0:
        return 0
    nc = len(grid[0])

    uf = UnionFindIsLand(grid)
    num_islands = 0
    for r in range(nr):
        for c in range(nc):
            if grid[r][c] == "0":
                num_islands += 1
            else:
                for x, y in [(r + 1, c), (r, c + 1)]:
                    if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                        uf.union(r * nc + c, x * nc + y)
    return uf.getCount() - num_islands


test = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
print(num_is_lands(test))
