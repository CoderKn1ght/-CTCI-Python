from CH2_Linked_Lists.Node import Node

n1 = Node(4)
n3 = Node(6)
n4 = Node(7)
n5 = Node(7)

n1.next = n3
n3.next = n4
n4.next = n5

n1.iterate_and_print()