def search(nums,target):

    if len(nums) < 1:
        return -1

    start = 0
    end = len(nums) - 1

    pivot_index = find_pivot(start, end, nums)

    if nums[pivot_index] == target:
        return pivot_index

    if nums[pivot_index] < target <= nums[end]:
        return binary_search(nums,pivot_index+1,end,target)
    return binary_search(nums,start,pivot_index-1,target)


def binary_search(nums,start,end,target):

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            start = mid + 1
            continue
        end = mid - 1

    return -1


def find_pivot(start, end, nums):

    while start <= end:
        if start == end:
            return start

        mid = (start+end)//2

        if nums[mid-1] > nums[mid] and nums[mid+1] > nums[mid]:
            return mid

        if nums[end] < nums[mid]:
            start = mid + 1
            continue
        end = mid



nums = [10,14,3,4,5,8]
target = 2
print(search(nums,target))