from CH2_Linked_Lists.Node import Node

if __name__ == '__main__':
    n1 = Node(5)
    n2 = Node(7)
    n3 = Node(3)
    n4 = Node(6)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    
    n1.iterate_and_print()
