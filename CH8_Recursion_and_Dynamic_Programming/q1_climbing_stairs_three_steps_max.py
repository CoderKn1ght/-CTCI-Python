def number_of_possible_ways_to_climb(n):
    if n < 3:
        return n
    if n == 3:
        return 4

    last = 4
    second_last = 2
    third_last = 1
    answer = 0

    for i in range(4,n+1):
        answer = last + second_last + third_last
        third_last = second_last
        second_last = last
        last = answer

    return answer

number_of_stairs = 5

print(number_of_possible_ways_to_climb(number_of_stairs))
