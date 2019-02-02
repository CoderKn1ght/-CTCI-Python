import time
# Solution 1
# Assumptions made: input uses a ASCII (128) character set
# Uses list. At most needs to go over 128 characters.


def is_palindrome_permutation(s1):
        character_set_check = [0] * 128
        found_one_odd = False
        for c in s1:
            if c == ' ':
                continue
            ascii_value = ord(c)
            character_set_check[ascii_value] += 1
        for c1 in character_set_check:
            if c1 % 2 == 0:
                continue
            else:
                if found_one_odd:
                    return False
                found_one_odd = True
        return True


start_time = time.perf_counter()
print(is_palindrome_permutation('aattcbfpapadd'))
end_time = time.perf_counter()
time_taken = (end_time-start_time)
print('array : ' + "%.10f" % time_taken + " seconds")

# Solution 2:
# Using boolean instead of Integer counts as in above ascii list


def is_palindrome_permutation_boolean(s1):
    character_set_check = [True] * 128
    count = 0
    for c in s1:
        if c == ' ':
            continue
        ascii_value = ord(c)
        if character_set_check[ascii_value]:
            count += 1
        else:
            count -= 1
        character_set_check[ascii_value] = not character_set_check[ascii_value]
    if count > 1:
        return False
    return True


start_time = time.perf_counter()
print(is_palindrome_permutation_boolean('aattcbfpapadd'))
end_time = time.perf_counter()
time_taken = (end_time-start_time)
print('Boolean : ' + "%.10f" % time_taken + " seconds")



