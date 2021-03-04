from typing import List

"""
反转字符串里的单词
"""


def reverse_str(test_str, k):
    result, flag = "", True
    for i in range(0, len(test_str), k):
        result += test_str[i:i + k][::-1] if flag else test_str[i:i + k]
        flag = not flag
    return result

