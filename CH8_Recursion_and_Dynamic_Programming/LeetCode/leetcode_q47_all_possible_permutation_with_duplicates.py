def permutations_without_duplicates(nums):
    previous_list = []

    for i in range(len(nums)):
        if i == 0:
            previous_list = [[nums[i]]]
            continue
        current_list = []
        current_set = set()
        for list in previous_list:
            for insert_index in range(len(list) + 1):
                temp_list = [i for i in list]
                temp_list.insert(insert_index, nums[i])
                temp_list_of_for_hash_check = [str(i) for i in temp_list]
                string_for_hash_check_from_list = ''.join(temp_list_of_for_hash_check)
                if string_for_hash_check_from_list not in current_set:
                    current_set.add(string_for_hash_check_from_list)
                    current_list.append(temp_list)

        previous_list = current_list

    print(len(previous_list))
    return previous_list

nums = [2,2,2,4]
print(permutations_without_duplicates(nums))