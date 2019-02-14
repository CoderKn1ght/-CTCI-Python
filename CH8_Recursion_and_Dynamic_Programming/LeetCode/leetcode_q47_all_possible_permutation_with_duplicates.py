# Think about faster algorithm
# do it using recursion

def permutations_without_duplicates(nums):
    previous_list = [[]]

    for i in range(len(nums)):
        current_list = []
        current_set = set()
        for list in previous_list:
            for insert_index in range(len(list) + 1):
                temp_list = list[:insert_index] + [nums[i]] + list[insert_index:]
                string_for_hash_check_from_list = ''.join([str(i) for i in temp_list])
                if string_for_hash_check_from_list not in current_set:
                    current_set.add(string_for_hash_check_from_list)
                    current_list.append(temp_list)

        previous_list = current_list

    print(len(previous_list))
    return previous_list

nums = [2,2,4]
print(permutations_without_duplicates(nums))