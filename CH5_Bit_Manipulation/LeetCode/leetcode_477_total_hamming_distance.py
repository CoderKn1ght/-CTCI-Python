# Times out on leetcode

def get_all_combinations(nums):
    total_hamming_distance = 0

    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            result = nums[i] ^ nums[j]
            current_hamming_distance = 0
            while result != 0:
                if result & 1 == 1:
                    current_hamming_distance += 1
                result = result >> 1
            total_hamming_distance += current_hamming_distance
            j += 1
        i +=1

    return total_hamming_distance
nums = [482445,7558884]

print(get_all_combinations(nums))