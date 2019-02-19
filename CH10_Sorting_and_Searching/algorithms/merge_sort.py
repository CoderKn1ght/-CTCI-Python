def merge_sort(nums):
    if len(nums) > 1:
        mid = int(len(nums)/2)
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)

        return merge_sort_util(left,right,nums)

def merge_sort_util(left,right,nums):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

    return nums

nums = [5,1,4,2,8,2,3,4,7,8,4,5,6,23,1,1,5,7,8,9,2,4,5,6,34,45,562,34,56,64,423,24,13212,3123,211,4,12,234,35,56,45,575434,2,323,12]

start = 0
end = len(nums)
print(merge_sort(nums))
