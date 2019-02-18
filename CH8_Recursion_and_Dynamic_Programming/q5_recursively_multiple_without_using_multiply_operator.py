# Try bit manipulations solution
# Try dynamic programming approach

def iterative_solution_using_addition(num1, num2):
    result = 0

    for i in range(num2):
        result += num1

    return result

def recursive_simple_solution_using_addition(num1, num2):
    sum = 0
    count = 1
    negative = False

    if num1 < 0:
        negative = True
        num1 = -1 * num1

    if num2 < 0:
        num2 = -1 * num2

        if negative == True:
            negative = False
        else:
            negative = True

    if negative == True:
        return -1 * recursive_simple_solution_util(num1, num2, sum, count)
    return recursive_simple_solution_util(num1, num2, sum, count)

def recursive_simple_solution_util(num1, num2, sum, count):
    if count == num2:
        return sum

    sum += num2
    count += 1

    return recursive_simple_solution_util(num1, num2, sum, count)

def dynamic_programming_solution(num1, num2):
    print("reached")

num1 = -5
num2 = -6
print(dynamic_programming_solution(num1, num2))
