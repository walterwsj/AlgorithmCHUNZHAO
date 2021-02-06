from collections import Counter
from typing import List

"""
多数元素
"""


def majority_element(test_nums: List[int]) -> int:
    count = Counter(test_nums)
    result = 0
    for k in dict(count):
        if count[k] > len(test_nums) // 2:
            result = k
    return result


def majority_element_moore(nums: List[int]) -> int:
    temp_num = nums[0]
    times = 1
    for i in range(1, len(nums)):
        if times == 0:
            temp_num = nums[i]
            times = 1
        elif nums[i] == temp_num:
            times += 1
        else:
            times -= 1
    return temp_num


"""
幂运算
"""


def my_pow(x, n):
    def sub_pows(N):
        if N == 0:
            return 1.0
        sub_pow = sub_pows(N // 2)
        return sub_pow * sub_pow if N % 2 == 0 else sub_pow * sub_pow * x

    return sub_pows(n) if n >= 0 else 1.0 / sub_pows(-n)


"""
返回不含重复元素的数组的所有子集
"""


def sub_sets_python(nums):
    res = [[]]
    for i in nums:
        res = res + [[i] + num for num in res]
    return res


def sub_sets_feedback(nums):
    res = []
    n = len(nums)

    def helper(index, temp_res):
        res.append(temp_res)
        for i in range(index, n):
            helper(i + 1, temp_res + [nums[i]])

    helper(0, [])
    return res


def sub_sets(nums):
    subsets = [[]]
    for num in nums:
        new_sets = []
        for subset in subsets:
            new_sub = subset + [num]
            new_sets.append(new_sub)
        subsets.extend(new_sets)
    return subsets


"""
17. 电话号码的字母组合
"""


def letter_combinations(digits: str) -> List[str]:
    if not digits:
        return []
    d = [" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    res = [""]
    for i in digits:
        letters = d[ord(i) - 48]
        size = len(res)
        for x in range(size):
            tmp = res.pop(0)
            for j in letters:
                res.append(tmp + j)
    return res


"""
柠檬酸找零
"""


def lemonade_change(bills):
    five, ten = 0, 0
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        else:
            if five > 0 and ten > 0:
                five -= 1
                ten -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True


def lemonade_change_list(bills):
    a = [0] * 5
    for bill in bills:
        a[bill / 5] += 1
        a[bill / 10] -= 1
        a[bill / 20] -= 1
        if a[1] < 0 or a[1] + 2 * a[2] < 0:
            return False
    return True


"""
122. 买卖股票的最佳时机 II
"""


def max_profit(prices: List[int]) -> int:
    if len(prices) < 2:
        return False
    final_profit = 0
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i - 1]
        if diff > 0:
            final_profit += diff
    return final_profit


"""
455. 分发饼干
"""


def find_content_children(children: List[int], cookies: List[int]):
    children.sort()
    cookies.sort()
    res, index = 0, len(cookies) - 1
    for i in range(len(children) - 1, -1, -1):
        if index >= 0 and cookies[index] >= children[i]:
            res += 1
            index -= 1
    return res


nums = [3, 2, 3]
print(majority_element(nums))
