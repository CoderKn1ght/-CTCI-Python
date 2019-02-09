def get_nth_bit(number, bit_number):
    if (number >> bit_number & 1) == 1:
        return 1
    return 0

def set_nth_bit(number, bit_number):
    return number | (1 << bit_number)

def clear_nth_bit(number, bit_number):
    return number & ~(1 << bit_number)

def update_nth_bit(number,bit_number,value):
    if value == 1:
        return number | (1 << bit_number)
    return number & ~(1 << bit_number)