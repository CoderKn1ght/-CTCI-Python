def permutations_with_duplicates(string):

    previous_list = []

    for i in range(len(string)):
        if i == 0:
            previous_list = [string[i]]
            continue
        current_set = set()
        for single_string in previous_list:
            for insert_index in range(len(single_string)+1):
                temp_string = [i for i in single_string]
                temp_string.insert(insert_index,string[i])
                current_set.add(''.join(temp_string))

        previous_list = [string for string in current_set]

    print(len(previous_list))
    return previous_list

nums = "abb"
print(permutations_with_duplicates(nums))