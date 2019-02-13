def solve_tower_of_hanoi(number_of_disks):
    stack_1 = [number_of_disks-i for i in range(0,number_of_disks)]
    stack_2 = []
    stack_3 = []

    stack_2.append(stack_1.pop())
    stack_3.append(stack_1.pop())
    stack_3.append(stack_2.pop())
    stack_2

    print(stack_1)
    print(stack_2)
    print(stack_3)

number_of_disks = 3
solve_tower_of_hanoi(number_of_disks)