from CH5_Bit_Manipulation.basic_bit_functions import get_nth_bit, set_nth_bit

# Solutions online are more complex and maybe faster

def get_largest_number(number):
    number_of_ones = get_number_of_ones(number)
    number = 0

    while number_of_ones != 0:
        number = set_nth_bit(number,31-number_of_ones)
        number_of_ones -= 1

    return number

def get_smallest(number):
    number_of_ones = get_number_of_ones(number)
    number = 0

    while number_of_ones != 0:
        number = set_nth_bit(number,number_of_ones-1)
        number_of_ones -= 1

    print(bin(number))
    return number

def get_number_of_ones(number):
    number_of_ones = 0
    while number != 0:
        bit_value = get_nth_bit(number, 0)
        if bit_value == 1:
            number_of_ones += 1
        number = number >> 1

    return number_of_ones

number = 2_147_43_644
print(number)
print(get_largest_number(number))
print(get_smallest(number))

