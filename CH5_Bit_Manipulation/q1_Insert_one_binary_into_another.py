from CH5_Bit_Manipulation.basic_bit_functions import clear_nth_bit
n = 0b1110000000000
m = 0b100011
i = 2
j = 6

m = m << i

while i < j:
    clear_nth_bit(n,i)
    i += 1

m = m | n
print(bin(m))