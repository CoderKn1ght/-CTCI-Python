# Solution 1


def is_one_away(s1, s2):
    found_change = False
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if found_change:
                    return False
                found_change = True
        return True
    elif len(s1) > len(s2):
        return helper(s1, s2)
    else:
        return helper(s2, s1)


def helper(s1, s2):
    if len(s1) - len(s2) > 1:
        return False
    dict = {}
    for c in s1:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    for c in s2:
        if c in dict:
            if dict[c] == 0:
                return False
            dict[c] -= 1
        else:
            return False

    for value in dict.values():
        flag = False
        if value != 0 and value != 1:
            return False
        elif value == 1:
            if flag:
                return False
            flag = True
    return True


print(is_one_away('cake', 'eka'))
