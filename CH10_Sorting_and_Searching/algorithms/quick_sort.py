def quick_Sort(start,end,nums):

    if start < end:
        pivot_index = partition(start,end,nums)

        quick_Sort(start, pivot_index-1,nums)
        quick_Sort(pivot_index+1,end,nums)

    return nums

def partition(start,end,nums):
    pivot = nums[end]
    pivot_index_to_return = start

    for i in range(start,end):
        if nums[i] <= pivot:
            nums[i], nums[pivot_index_to_return] = nums[pivot_index_to_return],nums[i]
            pivot_index_to_return += 1
    nums[pivot_index_to_return], nums[end] = nums[end], nums[pivot_index_to_return]
    return pivot_index_to_return

nums = [5,1,4,2,8,2,3,4,7,8,4,5,6,23,1,1,5,7,8,9,2,4,5,6,34,45,562,34,56,64,423,24,13212,3123,211,4,12,234,35,56,45,575434,2,323,12]
print(quick_Sort(0,len(nums)-1,nums))