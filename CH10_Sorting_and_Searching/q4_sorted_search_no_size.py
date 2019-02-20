import random

def search_without_size(random_numbers):
    if random_numbers[0] == -1:
        return "empty"
    if random_numbers[1] == -1:
        return random_numbers[1]

    previous_valid_index = 1

    invalid_high_index = get_high_index(random_numbers,previous_valid_index)

def get_high_index(random_numbers, previous_valid_index):
    high_index = 1
    while True:
        previous_valid_index += high_index
        try:
            high_index = high_index * 2
            something = random_numbers[high_index]
        except:
            return previous_valid_index

random_numbers = []
for x in range(10000):
    random_numbers.append(random.randint(0,5000))
random_numbers.sort()

search_without_size(random_numbers)