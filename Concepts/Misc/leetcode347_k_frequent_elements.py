from collections import Counter

def solve(nums, k):
    cnt = Counter()

    for num in nums:
        cnt[num] += 1

    cnt = cnt.most_common()

    to_return = []
    for keys in cnt:
        if k == 0:
            break
        to_return.append(keys[0])
        k -= 1

    print(to_return)


nums = [1, 2, 2]
k = 2

solve(nums, k)