import heapq, time
def merge_sorted(nums1,m,nums2,n):

    if len(nums2) == 0:
        return nums1
    nums1_index = nums2_index = 0
    zeros_start_index = len(nums1) - len(nums2)

    for index in range(len(nums1)):
        if nums2_index == len(nums2):
            return nums1
        if zeros_start_index == index:
            nums1[index] = nums2[nums2_index]
            nums2_index += 1
            zeros_start_index += 1
            continue
        if nums1[index] > nums2[nums2_index]:
            temp = zeros_start_index
            zeros_start_index += 1
            while temp > index:
                nums1[temp] = nums1[temp-1]
                temp -= 1
            nums1[index] = nums2[nums2_index]
            nums2_index += 1
            nums1_index += 1

    return nums1

def merge_sorted_from_behind(nums1, m , nums2, n):
    n = n-1
    m = m-1
    while m >= 0 and n >= 0:
        if nums1[m] > nums2[n]:
            nums1[n+m+1] = nums1[m]
            m -= 1
        else:
            nums1[n+m+1] = nums2[n]
            n -= 1
    if n >= 0:
        nums1[:n+1] = nums2[:n+1]
    return nums1

def using_heap(nums1, m, nums2, n):
    j = 0
    for i in range(m,m+n):
        nums1[i] = nums2[j]
        j += 1

    print(nums1)

    heapq.heapify(nums1)
    nums1 = heapq.nsmallest(len(nums1),nums1)

    return nums1

nums1 = [0]
nums2 = [-2]

print(merge_sorted_from_behind(nums1,0,nums2,1))
