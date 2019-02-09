from CH5_Bit_Manipulation.basic_bit_functions import get_nth_bit
number = 0b11110111011001000000

# not solved

print(bin(number))

start_index = 0
current_index = 0
zero_index = 0
longest = 0

flag = False

while number != 0:
    nth_bit = get_nth_bit(number,0)
    if nth_bit == 0:
        if flag == False:
            flag = True
            zero_index = current_index
        else:
            print("possible: ",current_index - start_index)
            longest = max(longest,(current_index - start_index))
            print("longest: ",longest)
            flag = True
            start_index = zero_index + 1
            print("new start index: ",start_index)
            zero_index = current_index
    current_index += 1

    number = number >> 1
