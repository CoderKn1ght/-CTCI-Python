def fibonacci_using_simple_recursion(num):
    if num < 2:
        return num
    return fibonacci_using_simple_recursion(num-1) + fibonacci_using_simple_recursion(num-2)

# Just uses two variables
# O(1) space and O(N) time
def fibonacci_using_simple_iteration(num):
    if num < 2:
        return num

    second_last = 0
    last = 1
    answer = 0
    for i in range(0,num-1):
        answer = second_last + last
        second_last = last
        last = answer
    return answer

def fibonacci_using_dynamic_programming_one_d_array(num):
    if num < 2:
        return num

    array = [0] * (num + 1)
    array[1] = 1

    for i in range(2,num+1):
        array[i] = array[i-1] + array[i-2]

    return array[num]

num = 10
print(fibonacci_using_dynamic_programming_one_d_array(num))