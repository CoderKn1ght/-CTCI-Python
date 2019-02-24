def intersection(nums1,num2):
    unique = set()

    for num in nums1:
        unique.add(num)

    result  = []
    for num in nums2:
        if num in unique:
            result.append(num)
            unique.remove(num)

    return result

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(intersection(nums1,nums2))