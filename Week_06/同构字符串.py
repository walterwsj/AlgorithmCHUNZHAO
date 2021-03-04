def is_isomorphic(str_1, str_2):
    return all(str_1.index(str_1[i]) == str_2.index(str_2[i]) for i in range(len(str_1)))
