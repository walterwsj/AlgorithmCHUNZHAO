import collections
from typing import List

"""
反转字符串里的单词
"""


def reverse_str(test_str):
    return " ".join([i[::-1] for i in test_str.strip().split(' ') if i])


def reverse_str_deque(s: str) -> str:
    left, right = 0, len(s) - 1
    while left <= right and s[left] == ' ':
        left += 1
    while left <= right and s[right] == ' ':
        right -= 1
    tmp, result = collections.deque(), []
    while left <= right:
        if s[left] != ' ':
            tmp.appendleft(s[left])
        else:
            result.append("".join(tmp))
            tmp = collections.deque()
        left += 1
    result.append("".join(tmp))
    return ' '.join(result)
