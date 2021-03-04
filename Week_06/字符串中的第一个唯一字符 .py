import collections

"""
第一个不重复字符
"""


def first_unique_counter(word):
    dic = collections.Counter(word)
    for index, character in enumerate(word):
        if dic[character] == 1:
            return index
    return -1


def first_unique_char(s: str) -> int:
    dic = collections.Counter(s)
    for item in dic.keys():
        if dic[item] == 0:
            return s.index(item)
    return -1


