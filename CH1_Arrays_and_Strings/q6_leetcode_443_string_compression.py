from collections import Counter
def compress_using_extra_space(s):

    con = Counter(s)
    i = 0
    for c in con.items():
        s[i] = c[0]
        i += 1

        if c[1] > 1:
            s[i] = c[1]
            i += 1

    for i in range(i,len(s)):
        del s[i]

    print(s)


# assumes sorted
def without_using_extra_space(s):

    prev_index = forward_index = insert_index = 0
    count = 1

    while prev_index < len(s):
        forward_index = prev_index + 1
        while forward_index < len(s) and s[prev_index] == s[forward_index]:
            count += 1
            forward_index += 1
        else:
            s[insert_index] = s[prev_index]
            insert_index += 1
            if count > 1:
                s[insert_index] = str(count)
                insert_index += 1
            count = 1
            prev_index = forward_index
            continue

    print(s[:insert_index])
    return insert_index

s = ["a","a","b","b","c","c","c"]
print(without_using_extra_space(s))