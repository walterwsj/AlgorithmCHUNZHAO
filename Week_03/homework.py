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


"""
874. 模拟行走机器人
"""


def robot_sim(commands_list: List[int], obstacles_list: List[List[int]]) -> int:
    if not commands_list:
        return 0
    direct_x = [0, 1, 0, -1]  # up;left;down;right
    direct_y = [1, 0, -1, 0]
    current_x, current_y, current_direct, ans = 0, 0, 0, 0
    com_len, obs_len = len(commands), len(obstacles)
    obstacle_set = {(obstacles[i][0], obstacles[i][1]) for i in range(obs_len)}

    for i in range(com_len):
        if commands_list[i] == -1:  # 向右转90度
            current_direct = (current_direct + 1) % 4
        elif commands_list[i] == -2:  # 向左转90度
            current_direct = (current_direct + 3) % 4
        else:  # 1 <= x <= 9: 向前移动x个单位长度
            for j in range(commands_list[i]):
                # 试图走出一步，并判断是否遇到了障碍物
                nx = current_x + direct_x[current_direct]
                ny = current_y + direct_y[current_direct]
                # 当前坐标不是障碍物，计算并存储的最大欧式距离的平方做比较
                if (nx, ny) not in obstacle_set:
                    current_x = nx
                    current_y = ny
                    ans = max(ans, current_x * current_x + current_y * current_y)
                else:
                    # 是障碍点，被挡住了，停留，智能等待下一个指令，那可以跳出当前指令了。
                    break
    return ans


commands = [4, -1, 4, -2, 4]
obstacles = [[2, 4]]
print(robot_sim(commands, obstacles))
