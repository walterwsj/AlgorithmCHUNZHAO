from typing import List

"""
反转字母
输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"
"""


def reverse_only_letters(test_string):
    letters = [char for char in test_string if char.isalpha()]
    result = []
    for char in test_string:
        if char.isalpha():
            result.append(letters.pop())
        else:
            result.append(char)
    return "".join(result)
