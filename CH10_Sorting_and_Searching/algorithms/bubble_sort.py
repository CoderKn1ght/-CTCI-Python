import time

def bubble_sort(nums):
    is_sorted = False

    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def bubble_sort_optimized(nums):

    sorted = False

    while not sorted:
        sorted = True
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                sorted = False
    return nums


nums = [5,1,4,2,8,2,3,4,7,8,4,5,6,23,1,1,5,7,8,9,2,4,5,6,34,45,562,34,56,64,423,24,13212,3123,211,4,12,234,35,56,45,575434,2,323,12]

start_time = time.perf_counter()
print(bubble_sort(nums))
end_time = time.perf_counter()
time_taken = (end_time-start_time)
print('Normal : ' + "%.10f" % time_taken + " seconds")

start_time = time.perf_counter()
print(bubble_sort_optimized(nums))
end_time = time.perf_counter()
time_taken = (end_time-start_time)
print('Optimzed : ' + "%.10f" % time_taken + " seconds")


