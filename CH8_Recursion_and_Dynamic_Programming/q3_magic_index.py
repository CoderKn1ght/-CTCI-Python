def binary_search_solution_using_iteration(nums):
    start = 0
    end = len(nums) - 1

    while start < end:
        mid = int((start + end) / 2)

        if nums[mid] < mid:
            start = mid + 1
            continue
        elif nums[mid] > end:
            end = mid - 1
            continue
        return mid

def binary_search_using_recursion(nums):
    start = 0
    end = len(nums) - 1
    return binary_search_using_recursion_util(nums, start, end)

def binary_search_using_recursion_util(nums, start, end):

    if start  > end:
        return "Not found"
    mid = int((start + end) / 2)

    if nums[mid] < mid:
        return binary_search_using_recursion_util(nums, mid+1, end)
    elif nums[mid] > mid:
        return binary_search_using_recursion_util(nums, mid, mid-1)
    return mid

def binary_search_using_recursion_with_redundant_values(nums):
    start = 0
    end = len(nums) - 1
    return binary_search_using_recursion_with_redundant_values_util(nums, start, end)

def binary_search_using_recursion_with_redundant_values_util(nums, start, end):

    if start > end:
        return "Not found", False

    mid = int((start + end) / 2)

    if nums[mid] == mid:
        return mid, True

    result, found = binary_search_using_recursion_with_redundant_values_util(nums, start, end-1)
    if found:
        return result, found
    result, found = binary_search_using_recursion_with_redundant_values_util(nums, mid+1 , end)
    if found:
        return result, found

    return "not found", False


nums = [-10,-5,-12,-2,-2,3,4,8,9,12,13]
print(binary_search_using_recursion_with_redundant_values(nums))