def permutations_without_duplicates(nums):

    previous_list = [[]]

    for i in range(len(nums)):
        if i == 0:
            previous_list = [[nums[i]]]
            continue
        current_list = []
        for list in previous_list:
            for insert_index in range(len(list)+1):
                temp_list = [i for i in list]
                temp_list.insert(insert_index,nums[i])
                current_list.append(temp_list)

        previous_list = current_list

    print(len(previous_list))
    return previous_list

nums = [1,2,3]
print(permutations_without_duplicates(nums))