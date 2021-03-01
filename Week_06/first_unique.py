import collections

"""
第一个不重复字符
"""


def first_unique_counter(word):
    dic = collections.Counter(word)
    for index, character in enumerate(word):
        if dic[character] == 1:
            return index
    return None


a = "aabcdeb"
print(first_unique_counter(a))
