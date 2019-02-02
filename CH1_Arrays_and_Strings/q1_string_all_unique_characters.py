# Solution 1
# Assumptions made: input uses a ASCII (128) character set
# Uses a boolean list. At most needs to go over 128 characters.


def check_all_unique(string_to_be_tested):
    if len(string_to_be_tested) > 128:
        return False
    character_set_check = [False] * 128
    for char in string_to_be_tested:
        ascii_value = ord(char)
        if character_set_check[ascii_value]:
            return False
        character_set_check[ascii_value] = True
    return True


print(check_all_unique('aucxizlk'))
