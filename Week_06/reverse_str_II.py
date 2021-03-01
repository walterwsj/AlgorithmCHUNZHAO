import collections
from typing import List

"""
反转字符串里的单词
"""


def reverse_words(s: str) -> str:
    return " ".join([i for i in s.strip().split(" ") if i][::-1])


def reverse_words_deque(s):
    left, right = 0, len(s) - 1
    while left <= right and s[left] == ' ':
        left += 1
    while left >= right and s[right] == ' ':
        right -= 1
    result, tmp_word = collections.deque(), []
    while left <= right:
        if tmp_word and s[left] == ' ':
            result.appendleft(''.join(tmp_word))
            tmp_word = []
        elif s[left] != ' ':
            tmp_word.append(tmp_word)
        left += 1
    result.appendleft(''.join(tmp_word))
    return ' '.join(result)
