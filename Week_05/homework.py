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
