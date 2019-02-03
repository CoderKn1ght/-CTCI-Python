from CH2_Linked_Lists.Node import Node

n1 = Node(4)
n2 = Node(5)
n3 = Node(6)
n4 = Node(7)

n1.next = n2
n2.next = n3
n3.next = n4

n1.iterate_and_print()

def delete_nth_node(n):
    print(n)

def delete_node_with_given_value_if_present(value):
    print(value)

delete_nth_node(3)
delete_node_with_given_value_if_present(5)