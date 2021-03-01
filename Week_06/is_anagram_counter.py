import collections

"""
异位词
"""


def is_anagram_py(word_1, word_2):
    return collections.Counter(word_1) == collections.Counter(word_2)


def is_anagram(word_1, word_2):
    len_word_1, len_word_2 = len(word_1), len(word_2)
    if len_word_1 != len_word_2:
        return False
    counts = [0] * 26
    for i in range(len_word_1):
        counts[ord(word_1[i]) - ord("a")] += 1
        counts[ord(word_2[i]) - ord("a")] -= 1
    for i in counts:
        if i != 0:
            return False
    return True
