from CH4_Trees_and_Graphs.TreeNode import TreeNode
# Also this is question no 108 at LeetCode

sorted_list = [0,1,2,3,4,5,6,7,8,9,10]


def in_order(head):
    if not head:
        return
    in_order(head.left)
    print(head.val)
    in_order(head.right)

def construct_tree(start, end):
    mid_index = int((start + end) / 2)
    head = TreeNode(sorted_list[mid_index])
    if mid_index != start:
        head.left = construct_tree(start, mid_index-1)
    if mid_index != end:
        head.right = construct_tree(mid_index+1, end)

    return head

start = 0
end = len(sorted_list) - 1

in_order(construct_tree(start, end))