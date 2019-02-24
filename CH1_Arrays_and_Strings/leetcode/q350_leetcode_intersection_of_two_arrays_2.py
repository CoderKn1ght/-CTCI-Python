from collections import Counter
def intersection_2(nums1,num2):
    c = Counter(nums1)

    result = []

    for num in nums2:
        if num in c:
            result.append(num)
            if c[num] == 1:
                del c[num]
                continue
            c[num] -= 1

    print(result)

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(intersection_2(nums1,nums2))