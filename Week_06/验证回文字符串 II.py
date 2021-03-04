def valid_palindrome(s):
    is_true = lambda x: x == x[::-1]
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return is_true(s[left + 1:right + 1]) or is_true(s[left:right])
    return True
