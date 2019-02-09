from CH5_Bit_Manipulation.basic_bit_functions import get_nth_bit, update_nth_bit

number = 43261596
answer = 0

bit_number  = 0
while bit_number < 32:
    value_to_set = get_nth_bit(number,bit_number)
    answer = update_nth_bit(answer,(31-bit_number),value_to_set)
    bit_number += 1

print(answer)