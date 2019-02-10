import time
from CH5_Bit_Manipulation.basic_bit_functions import get_nth_bit, update_nth_bit
from collections import deque

def reverse_binary_representation_one_by_one(number):
    answer = 0
    bit_number = 0

    while bit_number < 32:
        value_to_set = get_nth_bit(number, bit_number)
        answer = update_nth_bit(answer, (31 - bit_number), value_to_set)
        bit_number += 1

    return answer

number = 0b11111111111111111111111111111101

start_time = time.perf_counter()
print(reverse_binary_representation_one_by_one(number))
end_time = time.perf_counter()
time_taken = (end_time-start_time)
print('One by One : ' + "%.10f" % time_taken + " seconds")

def reverse_binary_representation_using_stack(number):
    answer = 0
    queue = deque()

    for i in range(32):
        if number & 1 == 1:
            queue.appendleft(1)
        else:
            queue.appendleft(0)
        number = number >> 1

    for i in range(32):
        answer <<= 1
        if queue.pop() == 1:
            answer |= 1

    return answer

start_time = time.perf_counter()
print(reverse_binary_representation_using_stack(number))
end_time = time.perf_counter()
time_taken = (end_time-start_time)
print('One by One : ' + "%.10f" % time_taken + " seconds")
