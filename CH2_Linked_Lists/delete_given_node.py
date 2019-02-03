from CH2_Linked_Lists.Node import Node

n1 = Node(4)
n2 = Node(5)
n3 = Node(6)
n4 = Node(7)

n1.next = n2
n2.next = n3
n3.next = n4

# n1.iterate_and_print()

def delete_nth_node(n):
    print(n)


def delete_node_with_given_value_if_present(head, value):
    if head.val == value:
        head = head.next
    else:
        temp_node = head
        next_node = temp_node.next
        while next_node:
            if next_node.val == value:
                temp_node.next = next_node.next
                break
            next_node = next_node.next
            temp_node = temp_node.next
        else:
            print("Element Not Found")
    return head


head = delete_node_with_given_value_if_present(n1, 4)
head.iterate_and_print()