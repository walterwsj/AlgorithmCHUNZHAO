def get_longest_str(string_test):
    res = ''
    for i in range(len(string_test)):
        s1 = find(string_test, i, i)
        s2 = find(string_test, i, i + 1)
        res = s1 if len(s1) > len(res) else res
        res = s2 if len(s2) > len(res) else res
    return res


def find(string_part, i, j):
    while i >= 0 and j < len(string_part) and string_part[i] == string_part[j]:
        i -= 1
        j += 1
    return string_part[i + 1:j]
