import random


# Code assumes that if out of size -1 is returned (as mentioned in CTCI)
def search_without_size(random_numbers, target):
    if random_numbers[0] == -1:
        return "empty"
    if random_numbers[1] == -1:
        if random_numbers[0] == target:
            return random_numbers[0]
        return "not found"

    previous_valid_index = 1
    while True:
        higher_valid_index = get_high_index(random_numbers,previous_valid_index)
        if previous_valid_index == higher_valid_index:
            return "not found"
        if random_numbers[higher_valid_index] < target:
            previous_valid_index = higher_valid_index
            continue
        print("between", previous_valid_index, higher_valid_index)
        index = binary_search(random_numbers,previous_valid_index,higher_valid_index,target)
        if index == -1:
            return "not found"
        return index

def binary_search(random_numbers,previous_valid_index,higher_valid_index,target):
    while previous_valid_index <= higher_valid_index:
        mid = (previous_valid_index + higher_valid_index)//2

        if random_numbers[mid] == target:
            return mid
        if random_numbers[mid] < target:
            previous_valid_index = mid+1
            continue
        higher_valid_index = mid-1

    return -1


def get_high_index(random_numbers, previous_valid_index):
    temp_number = 1
    while True:
        try:
            temp_number *= 2
            something = random_numbers[previous_valid_index + temp_number]
            previous_valid_index += temp_number
        except:
            return previous_valid_index

random_numbers = []
for x in range(10000):
    random_numbers.append(random.randint(0,5000))
random_numbers.sort()

target = 534
answer_index = search_without_size(random_numbers,target)
if type(answer_index) == str:
    print(answer_index)
else:
    print("target: ",target)
    print("found: ",random_numbers[answer_index])
