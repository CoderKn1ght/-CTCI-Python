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


delete_node_with_given_value_if_present(n1, 6).iterate_and_print()
returned_node = delete_nth_node(n1, 3).iterate_and_print()