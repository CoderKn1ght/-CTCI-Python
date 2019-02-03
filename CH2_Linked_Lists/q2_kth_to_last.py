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


def kth_to_last(head, k):
    leading = head
    trailing = head
    count = 0
    while leading and count < k:
        leading = leading.next
        count += 1
    while leading:
        trailing = trailing.next
        leading = leading.next
    return trailing.val


print(kth_to_last(n1, 2))
