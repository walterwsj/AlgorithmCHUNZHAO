def valid_palindrome(s):
    is_palindrome = lambda x: x == x[::-1]
    str_part = lambda str_temp, x: str_temp[:x] + str_temp[x + 1:]
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_palindrome(str_part(s, left)) or is_palindrome(str_part(s, right))
        left += 1
        right -= 1
    return True
