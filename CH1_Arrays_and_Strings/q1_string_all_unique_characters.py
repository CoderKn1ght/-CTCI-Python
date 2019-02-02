import time
# Solution 1
# Assumptions made: input uses a ASCII (128) character set
# Uses a boolean list. At most needs to go over 128 characters.


def check_all_unique_boolean_list(string_to_be_tested):
    if len(string_to_be_tested) > 128:
        return False
    character_set_check = [False] * 128
    for char in string_to_be_tested:
        ascii_value = ord(char)
        if character_set_check[ascii_value]:
            return False
        character_set_check[ascii_value] = True
    return True


# Solution 2
# Uses Dictionary
def check_all_unique_dictionary(string_to_be_tested):
    character_set = {}
    for char in string_to_be_tested:
        if char not in character_set:
            character_set[char] = None
        else:
            return False
    return True


start_time = time.perf_counter()
print(check_all_unique_boolean_list('aucxizlxk'))
end_time = time.perf_counter()
time_taken = (end_time-start_time)
print('Boolean : ' + "%.10f" % time_taken + " seconds")

start_time = time.perf_counter()
print(check_all_unique_dictionary('aucxizlxk'))
end_time = time.perf_counter()
time_taken = (end_time-start_time)
print('Dictionary : ' + "%.10f" % time_taken + " seconds")

# Output Obtained
# False
# Boolean : 0.0000197465 seconds
# False
# Dictionary : 0.0000063471 seconds
