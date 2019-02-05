set_of_stack = []

threshold = 3

def push(val):
    if len(set_of_stack) == 0:
        set_of_stack.append([])

    current_stack = set_of_stack[len(set_of_stack)-1]
    if len(current_stack) == threshold:
        set_of_stack.append([])
        current_stack = set_of_stack[len(set_of_stack)-1]

    current_stack.append(val)

def pop():
    if len(set_of_stack) == 0:
        return "stack empty"
    last_stack = set_of_stack[len(set_of_stack)-1]
    temp = last_stack.pop()
    if len(last_stack) == 0:
        del set_of_stack[len(set_of_stack)-1]
    return temp

def pop_at_index(index):
    current_stack = set_of_stack[index]
    current_stack.pop()

def pop_at_index_and_insert_last(index):
    current_stack = set_of_stack[index]
    current_stack.pop()
    current_stack.append(pop())


# try shifting everythin one back
# def pop_at_index_and_shift_back(index):
#     current_stack = set_of_stack[index]
#     current_stack.pop()
#     for i in range (index, len(set_of_stack)):
#         if len(set_of_stack[i]) < 3:
#             # test = set_of_stack[i+1].pop()
#         break
#
#
#         # temp = set_of_stack[]

push(5)
push(3)
push(15)
push(7)
push(5)
push(3)
push(15)
push(7)
print(set_of_stack)
print("--------------------------")
pop_at_index_and_shift_back(0)
print(set_of_stack)
