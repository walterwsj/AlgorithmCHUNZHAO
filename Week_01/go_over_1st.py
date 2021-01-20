from typing import List

"""
删除排序数组中的重复项（Facebook、字节跳动、微软在半年内面试中考过）
旋转数组（微软、亚马逊、PayPal 在半年内面试中考过）
合并两个有序数组（Facebook 在半年内面试常考）
两数之和（亚马逊、字节跳动、谷歌、Facebook、苹果、微软在半年内面试中高频常考）
移动零（Facebook、亚马逊、苹果在半年内面试中考过）
加一（谷歌、字节跳动、Facebook 在半年内面试中考过）
"""


def remove_dup(nums):
    p, q, len_nums = 0, 1, len(nums)
    while q < len_nums:
        if nums[q] != nums[p]:
            p += 1
            nums[p] = nums[q]
        q += 1
    return nums, p + 1


# a = [1, 1, 2, 3, 3]
##################################################
def rotate_regular(nums, k):
    len_nums = len(nums)
    while k:
        tmp = nums[-1]
        for i in range(len_nums)[::-1]:
            nums[i] = nums[i - 1]
        nums[0] = tmp
        k -= 1
    return nums


def rotate_reverse(nums, k):
    len_nums = len(nums)
    reverse(nums, 0, len_nums - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len_nums - 1)
    return nums


def reverse(nums, i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return nums


def rotate_list(nums, k):
    slave, len_nums = [], len(nums)
    slave = nums[:]
    for i in range(len_nums):
        nums[(i + k) % len_nums] = slave[i]
    return nums


a = [1, 2, 3, 4, 5, 6]


##################################################
def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    return nums1


def merge_opti(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        while i >= 0 and nums1[i] > nums2[j]:
            nums1[i], nums1[k] = nums1[k], nums1[i]
            i -= 1
            k -= 1
        nums1[k], nums2[j] = nums2[j], nums1[k]
        k -= 1
        j -= 1
    return nums1


# a=[1,3,5,0,0,0]
# b=[1,2,6]
##################################################
def get_sum(nums, target):
    len_nums, res = len(nums), []
    for i in range(len_nums - 1):
        for j in range(i + 1, len_nums):
            if nums[i] + nums[j] == target:
                res.append([i, j])
    return res


def get_sum_dic(nums, target):
    dic = {}
    for index, value in enumerate(nums):
        rest_part = target - value
        if rest_part in dic:
            return [dic[rest_part], index]
        else:
            dic[value] = index


##################################################
def move_zero(nums):
    len_nums, j = len(nums), 0
    for i in range(len_nums):
        if nums[i] != 0:
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums


def move_zero_1(nums):
    index, len_nums = 0, len(nums)
    for i in range(len_nums):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1
    while index < len_nums:
        nums[index] = 0
        index += 1
    return nums


a = [1, 0, 0, 1, 0]


##########################################
def plus_one(digits: List[int]):
    count = 0
    for i in range(len(digits)):
        if digits[i] == 0:
            count += 1
        else:
            break
    num1 = int("".join([str(i) for i in digits])) + 1
    return [0] * count + [int(i) for i in list(str(num1))]


def plus_one_1(digits: List[int]):
    digits = [0] + digits
    for i in range(len(digits))[::-1]:
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            break
    if digits[0] == 0:
        return digits[1:]
    else:
        return digits
