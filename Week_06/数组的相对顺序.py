import collections
from typing import List

"""
数组的相对顺序
"""


def relative_sort_array_tuple(arr_1, arr_2):
    rank = {x: i for i, x in enumerate(arr_2)}
    arr_1.sort(key=lambda x: (0, rank[x]) if x in rank else (1, x))
    return arr1


def relative_sort_array(arr_1, arr_2):
    max_value = max(arr_1)
    frequency = [0] * (max_value + 1)
    for item in arr_1:
        frequency[item] += 1
    result = []
    for item in arr_2:
        result.extend([item] * frequency[item])
        frequency[item] = 0
    for index in range(max_value + 1):
        if frequency[index] > 0:
            result.extend([index] * frequency[index])
    return result


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
print(relative_sort_array(arr1, arr2))
