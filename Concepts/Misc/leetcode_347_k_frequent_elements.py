from collections import Counter
import heapq

def solve(nums, k):
    counter = Counter(nums)
    print(counter)
    print(heapq.nlargest(k, counter.keys(), key=counter.get))

nums = [1,5,5,4,4,4,9]
k = 2

solve(nums, k)