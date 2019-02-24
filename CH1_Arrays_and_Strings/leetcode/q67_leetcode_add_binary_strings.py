

from collections import deque
def add_binary(a, b):
    result = deque()
    prev_carry  = 0


    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0:
        sum = 0
        next_carry = 0
        flag = False

        if i >= 0:
            if a[i] == '1':
                sum = 1
            else:
                sum = 0

        print("first:",sum,prev_carry)

        if j >= 0:
            if b[j] == '1':
                if sum == 1:
                    flag = True
                    sum = 0
                    next_carry = 1
                else:
                    sum = 1
            else:
                if sum == 1:
                    sum = 1
                else:
                    sum = 0

        print("second:", sum, prev_carry)

        if sum:
            if prev_carry:
                sum = 0
                next_carry = 1
        else:
            if prev_carry:
                sum = 1
                next_carry = 0
            if flag:
                next_carry = 1

        prev_carry = next_carry

        print("third:", sum, next_carry)
        print("---------------")

        result.appendleft(str(sum))
        i -= 1
        j -= 1

    if prev_carry:
        result.appendleft('1')

    return ''.join(result)

a = "1111"
b = "1111"
print(add_binary(a,b))
