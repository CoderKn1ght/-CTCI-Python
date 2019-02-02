import time
# Solution 1
# Assumptions made: input uses a ASCII (128) character set
# Uses a boolean list. At most needs to go over 128 characters.

def is_unique_characters_boolean(string_to_be_tested):
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
def is_unique_characters_dictionary(string_to_be_tested):
    character_set = {}
    for char in string_to_be_tested:
        if char not in character_set:
            character_set[char] = None
        else:
            return False
    return True


# Solution 3
# Uses Bit Manipulation

def is_unique_characters_bit(string_to_be_tested):
    checker = 0
    for char in string_to_be_tested:
        ascii_value = ord(char) - ord('a')
        if (checker & (1 << ascii_value)) > 0:
            return False
        checker = checker | (1 << ascii_value)
    return True


start_time = time.perf_counter()
print(is_unique_characters_boolean('aucxizlk'))
end_time = time.perf_counter()
time_taken = (end_time-start_time)
print('Boolean : ' + "%.10f" % time_taken + " seconds")

start_time = time.perf_counter()
print(is_unique_characters_dictionary('aucxizlk'))
end_time = time.perf_counter()
time_taken = (end_time-start_time)
print('Dictionary : ' + "%.10f" % time_taken + " seconds")

start_time = time.perf_counter()
print(is_unique_characters_bit('asdfgh'))
end_time = time.perf_counter()
time_taken = (end_time-start_time)
print('Bit : ' + "%.10f" % time_taken + " seconds")

# Output Obtained
# True
# Boolean : 0.0000204518 seconds
# True
# Dictionary : 0.0000063471 seconds
# True
# Bit : 0.0000084628 seconds
