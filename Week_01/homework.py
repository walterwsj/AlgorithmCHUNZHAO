import copy
from typing import List

"""
给定一个排序数组，你需要在"原地"删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
"""


def remove_duplicates(nums: List[int]) -> int:
    if nums is None or len(nums) == 0:
        return 0
    former, latter, len_nums = 0, 1, len(nums)
    while latter < len_nums:
        if nums[former] != nums[latter]:
            former += 1
            nums[former] = nums[latter]
        else:
            latter += 1
    return former + 1


# test_nums = [1, 1, 2, 3]


"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
"""


def rotate_tmp_list(nums: List[int], k: int) -> list:
    slave_list = copy.deepcopy(nums)
    len_nums = len(nums)
    for i in range(len_nums):
        nums[(i + k) % len_nums] = slave_list[i]
    return nums


def rotate_tmp_list_2(nums: List[int], k: int) -> list:
    len_num = len(nums)
    k %= len_num
    slave = nums[:len_num - k]
    for i in range(len_num - k):
        del nums[0]
    nums.extend(slave)
    return nums


def rotate_reverse(nums: List[int], k: int) -> list:
    len_nums = len(nums)
    reverse(nums, 0, len_nums - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len_nums - 1)
    return nums


def reverse(nums, former, latter):
    while former < latter:
        nums[former], nums[latter] = nums[latter], nums[former]
        former += 1
        latter -= 1
    return nums


def rotate_regular(nums: List[int], k: int) -> list:
    len_nums = len(nums)
    if k % len_nums == 0:
        return nums
    while k:
        tmp = nums[-1]
        for i in range(len_nums - 1, -1, -1):
            nums[i] = nums[i - 1]
        nums[0] = tmp
        k -= 1
    return nums


# test_nums = [1, 2, 3, 4, 5, 6, 7]


"""
给你两个有序整数数组nums1 和 nums2，请你将 nums2 合并到nums1中，使 nums1 成为一个有序数组。
初始化nums1 和 nums2 的元素数量分别为m 和 n 。你可以假设nums1有足够的空间（空间大小等于m + n）来保存 nums2 中的元素。
"""


def merge(nums1: List[int], m: int, nums2: List[int], n: int):
    i, j, k = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        else:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1


def merge_optimize(nums1: List[int], m: int, nums2: List[int], n: int):
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        while i >= 0 and nums2[j] < nums1[i]:
            nums1[i], nums1[k] = nums1[k], nums1[i]
            i -= 1
            k -= 1
        nums1[k], nums2[j] = nums2[j], nums1[k]
        k -= 1
        j -= 1
    return nums1


# num1 = [1, 2, 3, 0, 0, 0]
# m = 3
# num2 = [2, 5, 6]
# n = 3


"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
"""


def two_sum(nums: List[int], target: int):
    res, len_nums = [], len(nums)
    for i in range(len_nums - 1):
        for j in range(i + 1, len_nums):
            if nums[i] + nums[j] == target:
                res.append([i, j])
    return res


def two_sum_optimize(nums: List[int], target: int):
    res = {}
    for index, value in enumerate(nums):
        rest_part = target - value
        if rest_part in res:
            return [res[rest_part], index]
        else:
            res[value] = index
    return res


"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
"""


def move_zeroes(nums: List[int]):
    j, len_nums = 0, len(nums)
    for i in range(len_nums):
        if nums[i] != 0:
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums


def move_zeroes_optimize(nums: List[int]):
    index, len_nums = 0, len(nums)
    for i in range(len_nums):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1
    while index < len_nums:
        nums[index] = 0
        index += 1
    return nums


"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位，数组中每个元素只存储单个数字。
你可以假设除了整数0之外，这个整数不会以零开头。
"""


def plus_one(digits: List[int]):
    len_main, len_slave = len(digits), len(digits)
    index = 0
    result = 0
    while len_main > 0:
        result += digits[index] * 10 ** (len_main - 1)
        index += 1
        len_main -= 1
    len_tmp_result = len(str(result + 1))
    if len_tmp_result == len_slave:
        return [int(i) for i in str(result + 1)]
    else:
        count = len_slave - len_tmp_result
        new_result = [0] * count
        new_result += [int(i) for i in str(result + 1)]
        return new_result


def plus_one_opi(digits: List[int]):
    len_digits, count = len(digits), -1
    for i in range(len_digits):
        if digits[i] != 0:
            break
        count += 1
    res = int("".join([str(i) for i in digits])) + 1
    return [0] * count + [int(x) for x in list(str(res))]


def plus_one_opi_1(digits: List[int]):
    len_digits, digits = len(digits), [0] + digits
    for i in range(len_digits)[::-1]:
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            break
    if digits[0] == 0:
        return digits[1:]
    else:
        return digits


"""
有效的字母异位词
"""


def is_anagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    len_t, count = len(s), [0] * 26
    for i in range(len_t):
        count[ord(s[i]) - ord("a")] += 1
        count[ord(t[i]) - ord("a")] -= 1
    for i in count:
        if i != 0:
            return False
    return True

