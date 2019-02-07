from CH4_Trees_and_Graphs.TreeNode import TreeNode

# Here height is defined as longest path from node downward to leaf node

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

def get_heights(root):

    left_height = 0
    right_height = 0

    if root.left:
        left_height = 1 + get_heights(root.left)
    if root.right:
        right_height = 1 + get_heights(root.right)

    print("at {0} the height is {1}:".format(root.val, max(left_height, right_height)))
    return max(left_height, right_height)

get_heights(root)

