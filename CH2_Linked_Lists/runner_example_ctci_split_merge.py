from CH2_Linked_Lists.Node import Node

n1 = Node('a1')
n2 = Node('a2')
n3 = Node('a3')
n4 = Node('a4')

n5 = Node('b1')
n6 = Node('b2')
n7 = Node('b3')
n8 = Node('b4')

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8

def solution(head):
    leading = head
    trailing = head
    current = head

    while leading:
        leading = leading.next
        if leading:
            leading = leading.next
            trailing = trailing.next

    while trailing:
        temp_current = current.next
        current.next = trailing
        temp_trailing = trailing
        trailing = trailing.next
        current  = temp_current
        if temp_trailing.next:
            temp_trailing.next = current

    return head

solution(n1).iterate_and_print()