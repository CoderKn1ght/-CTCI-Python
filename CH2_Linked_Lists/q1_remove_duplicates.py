from CH2_Linked_Lists.Node import Node
# Possible Solution without extra buffer -> O(n^2) -> Brute Force
n1 = Node(7)
n2 = Node(7)
n3 = Node(2)
n4 = Node(7)

n1.next = n2
n2.next = n3
n3.next = n4


def remove_duplicates_using_set(head):
    unique_set = set()
    current = head

    unique_set.add(current.val)

    while current.next:
        if current.next.val in unique_set:
            current.next = current.next.next
        else:
            unique_set.add(current.next.val)
            current = current.next
    return head


remove_duplicates_using_set(n1).iterate_and_print()
