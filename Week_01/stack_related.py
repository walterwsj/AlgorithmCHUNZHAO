def is_valid_parentheses(str_list):
    dic = {"{": "}", "(": ")", "[": "]"}
    stack = ["?"]
    for c in str_list:
        if c in dic:
            stack.append(c)
        elif dic[stack.pop()] != c:
            return False
    return len(stack) == 1