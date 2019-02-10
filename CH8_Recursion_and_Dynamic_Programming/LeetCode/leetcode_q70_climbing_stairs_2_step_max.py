def number_of_possible_ways_to_climb(n):
    if n < 3:
        return n

    last = 2
    second_last = 1
    answer = 0

    for i in range(3,n+1):
        answer = last + second_last
        second_last = last
        last = answer

    return answer

number_of_stairs = 4

print(number_of_possible_ways_to_climb(number_of_stairs))

