# Come up with one pass solution (two pointer) where we also verify string are in same order(dict methdo does not care about order i.e move operation)
# i.e if order is not same operation will be considered as move operations

from collections import Counter

def is_one_away_using_dict(s1, s2):

    if len(s2) > len(s1):
        s1, s2 = s2, s1

    dict = {}

    for c in s1:
        if c not in dict:
            dict[c] = 1
            continue
        dict[c] += 1

    one_different = False

    for c in s2:
        if c not in dict:
            if one_different:
                return False
            one_different = True
            continue
        dict[c] -= 1


    difference = 0
    for key in dict:
        difference += dict[key]
        if difference > 1:
            return False

    return True

print(is_one_away_using_dict('cas','cage'))
