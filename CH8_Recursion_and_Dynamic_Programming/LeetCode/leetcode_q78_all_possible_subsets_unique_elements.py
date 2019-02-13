def sub_sets_iterative(nums):
    power_set = [[]]
    for num in nums:
        temp_set = [set for set in power_set]
        for temp_list in temp_set:
            current_list = [element for element in temp_list]
            current_list.append(num)
            power_set.append(current_list)
    return power_set

def sub_set_sums_recursive(nums):
    super_set = [[]]
    i = 0
    return sub_Set_sums_recursive_util(super_set, nums, i)

def sub_Set_sums_recursive_util(super_set, nums, i):

    if i == len(nums):
        return super_set

    temp_set = [set for set in super_set]
    for set in temp_set:
        current_list = [element for element in set]
        current_list.append(nums[i])
        super_set.append(current_list)

    return sub_Set_sums_recursive_util(super_set, nums, i+1)


nums = [1,2,3]
print(sub_set_sums_recursive(nums))
