def palindrome_2(s):
    start = 0
    end = len(s) - 1
    flag = False

    return recrusively_search(start,end,flag)

def recrusively_search(start, end, flag):
    if start > end:
        return True

    if s[start] is not s[end]:
        print(start, end)
        if flag:
            return False
        flag = True
        if s[end - 1] == s[start]:
            if recrusively_search(start, end - 1, flag):
                return True
        if s[start + 1] == s[end]:
            if recrusively_search(start + 1, end, flag):
                return True
        return False
    if not recrusively_search(start + 1, end - 1, flag):
        return False
    return True

def faster_approach(s):
    start = 0
    end = len(s) - 1

    while start < end:
        if s[start] is not s[end]:
            return search(start + 1, end, s) or search(start, end - 1, s)
        start += 1
        end -= 1

    return True


def search(start, end, s):
    if start >= end:
        return True
    if s[start] is not s[end]:
        return False

    return search(start + 1, end - 1,s)


s = "deeee"
print(faster_approach(s))
