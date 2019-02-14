def permutations_without_duplicates(nums):

    previous_list = [[]]

    for i in range(len(nums)):
        current_list = []
        for list in previous_list:
            for insert_index in range(len(list)+1):
                temp_list = list[:insert_index] + [nums[i]] + list[insert_index:]
                # temp_list.insert(insert_index,nums[i])
                current_list.append(temp_list)

        previous_list = current_list

    print(len(previous_list))
    return previous_list

nums = [1,2,3,4]
print(permutations_without_duplicates(nums))