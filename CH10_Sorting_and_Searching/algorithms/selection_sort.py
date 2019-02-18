def selection_sort(nums):

    for i in range(len(nums)-1):
        smallest_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[smallest_index]:
                smallest_index = j
        nums[i], nums[smallest_index] = nums[smallest_index], nums[i]
    return nums



nums = [5,1,4,2,8]
print(selection_sort(nums))