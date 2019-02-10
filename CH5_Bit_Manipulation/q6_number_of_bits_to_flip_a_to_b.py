def count_flip_bits_by_trversing_until_zero(num1, num2):
    count = 0

    while num1 or num2 != 0:
        if num1 & 1 == 1:
            num1_current_bit_value = 1
        else:
            num1_current_bit_value = 0

        if num2 & 1 == 1:
            num2_current_bit_value = 1
        else:
            num2_current_bit_value = 0

        if num1_current_bit_value != num2_current_bit_value:
            count += 1

        num1 = num1 >> 1
        num2 = num2 >> 1

    return count

def count_flip_bits_by_using_XOR_operation(num1, num2):
    result = num1 ^ num2
    return count_set_bits(result)

def count_set_bits(num):
    count = 0
    while num != 0:
        if num & 1 == 1:
            count += 1
        num = num >> 1
    return count

num1 = 29
print(bin(num1))
num2 = 15
print(bin(num2))

print(count_flip_bits_by_using_XOR_operation(num1, num2))