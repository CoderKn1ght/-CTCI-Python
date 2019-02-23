# try to optimize

def lcs_without_Repeating(s):

    # time_complexity O(n^2)

    unique = [False for i in range(128)]

    leading = 0
    trailing = 0
    length = 0
    temp_length = 0
    while leading < len(s):
        if not unique[ord(s[leading])]:
            unique[ord(s[leading])] = True
            leading += 1
            temp_length += 1
            length = max(length, temp_length)
            continue
        while s[trailing] != s[leading]:
            unique[ord(s[trailing])] =  False
            trailing += 1
            temp_length -= 1
        trailing += 1
        leading += 1

    return length



s = "abcbcbbsqwea"
print(lcs_without_Repeating(s))