import collections
from typing import List

"""
数组的相对顺序
"""


def relative_sort_array_tuple(arr1: List[int], arr2: List[int]) -> List[int]:
    def my_cmp(x: int) -> (int, int):
        return (0, rank[x]) if x in rank else (1, x)

    rank = {x: i for i, x in enumerate(arr2)}
    arr1.sort(key=my_cmp)
    return arr1


def relative_sort_array(arr1: List[int], arr2: List[int]) -> List[int]:
    upper = max(arr1)
    frequency = [0] * (upper + 1)
    for x in arr1:
        frequency[x] += 1
    ans = list()
    for x in arr2:
        ans.extend([x] * frequency[x])
        frequency[x] = 0
    for x in range(upper + 1):
        if frequency[x] > 0:
            ans.extend([x] * frequency[x])
    return ans


"""
异位词
"""


def is_anagram_counter(s: str, t: str) -> bool:
    return collections.Counter(s) == collections.Counter(t)


def is_anagram(s, t):
    if len(s) != len(t):
        return False
    len_t, counts = len(s), [0] * 26
    for i in range(len_t):
        counts[ord(s[i]) - ord("a")] += 1
        counts[ord(t[i]) - ord("a")] -= 1
    for i in counts:
        if i != 0:
            return False
    return True


"""
第一个不重复字符
"""


def first_unique(s):
    dic = dict()
    for c in s:
        dic[c] = dic.get(c, 0) + 1
    for i, c in enumerate(s):
        if dic[c] == 1:
            return i
    return -1


def first_unique_counter(s):
    dic = collections.Counter(s)
    for i, c in enumerate(s):
        if dic[c] == 1:
            return i
    return -1


"""
字符串反转II
"""


def reverse_str(s: str, k: int) -> str:
    res = list(s)
    n = len(s)
    time = n // (2 * k) if n % (2 * k) == 0 else n // (2 * k) + 1
    for i in range(time):
        res[i * 2 * k:i * 2 * k + k] = s[i * 2 * k:i * 2 * k + k][::-1]
    return ''.join(res)


def reverse_str_py(s, k):
    flag, res = True, ""
    for i in range(0, len(s), k):
        res += s[i:i + k][::-1] if flag else s[i:i + k]
        flag = not flag
    return res


"""
反转字符串里的单词
"""


def reverse_words_py(s: str) -> str:
    return " ".join([i for i in s.strip().split(' ') if i][::-1])


def reverse_words_deque(s):
    left, right = 0, len(s) - 1
    while left <= right and s[left] == '':
        left += 1
    while left <= right and s[right] == '':
        right -= 1
    d, word = collections.deque(), []
    while left <= right:
        if s[left] == ' ' and word:
            d.appendleft(''.join(word))
            word = []
        elif s[left] != ' ':
            word.append(s[left])
        left += 1
    d.appendleft(''.join(word))
    return ''.join(d)


"""
反转字母
"""


def reverse_only_letters(S):
    letters = [c for c in S if c.isalpha()]
    ans = []
    for c in S:
        if c.isalpha():
            ans.append(letters.pop())
        else:
            ans.append(c)
    return "".join(ans)
