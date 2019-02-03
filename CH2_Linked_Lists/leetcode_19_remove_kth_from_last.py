from CH2_Linked_Lists.Node import Node

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

def remove_kth_from_last(head, k):
    leading = head
    trailing = head
    count = 0

    while count < k:
        leading = leading.next
        count += 1
    if not leading:
        head = head.next
        return head
    while leading:
        prev = trailing
        trailing = trailing.next
        leading = leading.next
    prev.next = prev.next.next
    return head

remove_kth_from_last(n1,5).iterate_and_print()