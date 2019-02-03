from CH2_Linked_Lists.Node import Node

n1 = Node(4)
n2 = Node(5)
n3 = Node(6)
n4 = Node(7)

n1.next = n2
n2.next = n3
n3.next = n4


# Assumption: By nth it means n+1 becaause starts from zero
# Assumption: n will not be greater than length-1
def delete_nth_node(head, n):
    if n == 0:
        temp = head.next
        head.next = None
        return temp
    else:
        index = 0
        current = head
        while index < n - 1:
            index += 1
            current = current.next
        current.next = current.next.next
        return head

def delete_node_with_given_value_if_present(value):
    print(value)

returned_node = delete_nth_node(n1, 3).iterate_and_print()
# delete_node_with_given_value_if_present(5)