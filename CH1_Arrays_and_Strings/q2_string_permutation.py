import time
# Solution 1
# Assumptions made: input uses a ASCII (128) character set
# Uses a boolean list. At most needs to go over 128 characters.


def is_string_permutation_ascii_array(s1, s2):
    if len(s1) != len(s2):
        return False
    character_set_check = [0] * 128
    for c in s1:
        ascii_value = ord(c)
        character_set_check[ascii_value] += 1
    for c in s2:
        ascii_value = ord(c)
        if character_set_check[ascii_value] == 0:
            return False
        character_set_check[ascii_value] -= 1
    return True

# Solution 2
# Uses Dictionary similar to question one dictionary solution

# Solution 3
# Uses sorting, Increased time complexity, but a possible solution without using any extra space


def is_string_permutation_sorting(s1, s2):
    s1 = list(s1)
    s2 = list(s2)

    s1.sort()
    s2.sort()

    if s1 != s2:
        return False
    return True


start_time = time.perf_counter()
print(is_string_permutation_ascii_array('abcd','abcd'))
end_time = time.perf_counter()
time_taken = (end_time-start_time)
print('ASCII Array : ' + "%.10f" % time_taken + " seconds")

start_time = time.perf_counter()
print(is_string_permutation_sorting('abcd','abcd'))
end_time = time.perf_counter()
time_taken = (end_time-start_time)
print('Sorting : ' + "%.10f" % time_taken + " seconds")

# Output Obtained
# True
# Boolean : 0.0000204518 seconds
# True
# Dictionary : 0.0000063471 seconds
# True
# Bit : 0.0000084628 seconds
