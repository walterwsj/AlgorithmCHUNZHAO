import sys


def max_container_regular(nums):
    res, len_nums = [], len(nums)
    for i in range(len_nums - 2):
        for j in range(i + 1, len_nums - 1):
            res = max(res, min(nums[i], nums[j]) * (j - i))
    return res


def max_container_opti_2(nums):
    res, len_nums = [], len(nums)
    i, j = 0, len_nums - 1
    while i < j:
        if nums[i] < nums[j]:
            min_height = nums[i]
            i += 1
        else:
            min_height = nums[j]
            j -= 1
        res = max(res, min_height * (j - i))
        j -= 1
        i += 1
    return res


def max_area_regular(nums):
    res, len_nums = [], len(nums)
    for i in range(len_nums - 1):
        for j in range(i, len_nums):
            min_height = sys.maxsize
            for k in range(i, j + 1):
                min_height = min(min_height, nums[k])
            res = max(res, min_height * (j - i + 1))
    return res


def max_area_opti_1(nums):
    res, len_nums = [], len(nums)
    for i in range(len_nums - 1):
        min_height = sys.maxsize
        for j in range(i, len_nums):
            min_height = min(min_height, nums[j])
        res = max(res, min_height * (j - i + 1))
    return res


def max_area_opti_2(nums):
    res, len_nums, stack = 0, len(nums), [-1]
    for i in range(len_nums):
        while stack[-1] != -1 and nums[i] < nums[stack[-1]]:
            res = max(res, nums[stack.pop()] * (i - stack[-1] - 1))
    while stack[-1] != -1:
        res = max(res, nums[stack.pop()] * (stack[-1] - 1))
    return res


def get_floor(n):
    if n < 1:
        return 0
    if 1 <= n <= 2:
        return 1
    s1, s2 = 1, 1
    for i in range(3, n + 1):
        s1, s2 = s2, s1 + s2
    return s1 + 1


def three_sum(nums):
    if len(nums) < 3:
        return 0
    nums.sort()
    res, len_nums = [], len(nums)
    for i in range(len_nums):
        if nums[i] > 0:
            break
        if i > 0 and nums[i - 1] == nums[i]:
            continue
        j, k = i + 1, len_nums - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                res.append([i, j, k])
                while nums[j] == nums[j + 1]:
                    j += 1
                while nums[k] == nums[k - 1]:
                    k -= 1
                j += 1
                k -= 1
            elif nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            else:
                j += 1
    return res

