def insertion_sort(nums):

    sorted_index = 1
    while sorted_index < len(nums):
        temp_index = sorted_index
        while temp_index > 0 and nums[temp_index] < nums[temp_index-1]:
            nums[temp_index], nums[temp_index-1] = nums[temp_index-1], nums[temp_index]
            temp_index -= 1
        sorted_index += 1
    return nums

nums = [5,1,4,2,8,2,3,4,7,8,4,5,6,23,1,1,5,7,8,9,2,4,5,6,34,45,562,34,56,64,423,24,13212,3123,211,4,12,234,35,56,45,575434,2,323,12]
print(insertion_sort(nums))
