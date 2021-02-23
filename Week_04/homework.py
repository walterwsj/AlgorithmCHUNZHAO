from typing import List

from collections import Counter

"""
64. 最小路径和
"""


def min_path_sum(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, columns = len(grid), len(grid[0])
    dp = [[0] * columns for _ in range(rows)]
    dp[0][0] = grid[0][0]
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, columns):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, rows):
        for j in range(1, columns):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[rows - 1][columns - 1]


"""
91. 解码方法
"""


def num_decode(s):
    """
    :type s: str
    :rtype: int
    """
    if not s or s[0] == '0':  # 基本情况，直接返回 0
        return 0
    dp = [None] * len(s)  # 构建 dp 数组
    dp[0] = 1  # 只有一个数时肯定为 1
    if len(s) > 1:  # 为 dp[1] 填充值
        if s[1] == '0':  # s[i] 为 ‘0’ 时
            if int(s[0:2]) <= 26:  # 截取前两数，判断是否小于或等于 26
                dp[1] = 1  # 因为 s[i] 为 ‘0’ 所以 dp[1] 只有 1 种可能
            else:
                return 0  # 比如 60 , 此时该序列无法翻译
        else:  # s[i] 不为 ‘0’ 时
            if int(s[0:2]) <= 26:
                dp[1] = 2  # 比如 16，有两种翻译结果
            else:
                dp[1] = 1  # 比如 27，只有一种结果
    else:  # 只有一个数
        return 1

    for i in range(2, len(s)):  # 从 2 开始
        if s[i] == '0':  # s[i] 为 ‘0’ 时
            if s[i - 1] == '0':  # 前一个为 ‘0’
                return 0  # 无解
            else:  # 前一个不为 ‘0’
                if int(s[i - 1:i + 1]) <= 26:  # s[i-1] 和 s[i] 组成的数 <= 26
                    dp[i] = dp[i - 2]
                else:
                    return 0
        else:  # s[i] 不为 ‘0’
            if s[i - 1] == '0':  # 前一个为 ‘0’
                dp[i] = dp[i - 1]
            else:  # 前一个不为 ‘0’
                if int(s[i - 1:i + 1]) <= 26:  # s[i-1] 和 s[i] 组成的数 <= 26
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:  # s[i-1] 和 s[i] 组成的数 > 26
                    dp[i] = dp[i - 1]

    return dp[len(s) - 1]


"""
最大正方形
"""


def maximal_square(matrix: List[List[str]]) -> int:
    res = 0
    m = len(matrix)
    if m == 0:
        return 0
    n = len(matrix[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 if matrix[i - 1][j - 1] == "1" else 0
            res = max(res, dp[i][j])
    return res ** 2


"""
最大调度
"""


def least_interval(tasks: List[str], n: int) -> int:
    ct = Counter(tasks)
    num_bucket = ct.most_common(1)[0][1]
    last_bucket_size = list(ct.values()).count(num_bucket)
    res = (num_bucket - 1) * (n + 1) + last_bucket_size
    return max(res, len(tasks))


"""
回文子串
"""


def count_substring(s: str) -> int:
    # dp[i][j] 代表 子串[i, j] 是否是一个 回文串
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    count = 0
    # 枚举所有可能 因为代表子串 所以 i <= j
    for j in range(n):
        for i in range(0, j + 1):
            # 子串长度
            length = j - i + 1
            # 只有一个字符 直接就是一个回文串
            if length == 1:
                dp[i][j] = True
                count += 1
            # 两个字符 只有相等才是回文串
            if length == 2 and s[i] == s[j]:
                dp[i][j] = True
                count += 1
            # 超过两个字符 首位相同 且除去首尾的子串是回文串 才是回文串
            if length > 2 and s[i] == s[j] and dp[i + 1][j - 1] is True:
                dp[i][j] = True
                count += 1
    return count


"""
最长括号
"""


def longest_valid_parentheses(s: str) -> int:
    if not s:
        return 0
    res = 0
    stack = [-1]
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                res = max(res, i - stack[-1])
    return res


"""
62. 不同路径
"""


def unique_path(m, n):
    dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


m = 3
n = 7
print(unique_path(m,n))