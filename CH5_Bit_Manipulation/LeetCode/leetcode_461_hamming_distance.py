def get_hamming_distance(x,y):
    hamming_distance = 0

    while x or y != 0:
        first_bit_of_x = x & 1
        first_bit_of_y = y & 1

        if first_bit_of_x != first_bit_of_y:
            hamming_distance += 1
        if x != 0:
            x = x >> 1
        if y != 0:
            y = y >> 1

    return hamming_distance

x = 1
y = 4
print(get_hamming_distance(x, y))