from typing import List

"""
反转字符串里的单词
"""


def reverse_str(test_str):
    return " ".join([i[::-1] for i in test_str.strip().split(' ') if i])
