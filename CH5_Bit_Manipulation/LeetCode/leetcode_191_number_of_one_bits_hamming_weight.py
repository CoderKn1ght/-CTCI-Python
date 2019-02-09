def get_hamming_weight(number):
    hamming_distance = 0
    while number != 0:
        if number & 1 == 1:
            hamming_distance += 1
        number = number >> 1

    return hamming_distance

number = 11
print(get_hamming_weight(number))