from CH4_Trees_and_Graphs.TreeNode import TreeNode

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

root.right.right.right = TreeNode(70)
root.right.right.right.right = TreeNode(90)

def get_heights(root):

    left_height = 0
    right_height = 0

    if root.left:
        left_height = 1 + get_heights(root.left)
    if root.right:
        right_height = 1 + get_heights(root.right)

    # print("balance at {} is: {}".format(root.val, left_height - right_height))
    if abs(left_height-right_height) > 1:
        print("tree imbalanced at Node with value:",root.val)
    return max(left_height, right_height)

# get_heights(root)

# -------------------------------------------------
# -------------------------------------------------
# Retuning multiple values
# This will helping in breaking out of recuresion stack is tree imbalanced condidtion is satisfied

def check_balanced_with_multiple_returns(root):

    left_height = 0
    right_height = 0

    if root.left:
        balanced, height_temp_left = check_balanced_with_multiple_returns(root.left)
        if not balanced:
            return (False, None)
        left_height = 1 + height_temp_left
    if root.right:
        balanced, height_temp_right = check_balanced_with_multiple_returns(root.right)
        if not balanced:
            return (False, None)
        right_height = 1 + height_temp_right

    print("balance at {} is: {}".format(root.val, left_height - right_height))
    if abs(left_height-right_height) > 1:
        print("here")
        return (False, None)
    return (True, max(left_height, right_height))

print(check_balanced_with_multiple_returns(root))

# -------------------------------------------------
# -------------------------------------------------
# Using objects as root nodes with their height as object attribute
# This will also helping in breaking out of recuresion stack is tree imbalanced condidtion is satisfied

class TreeNodeWithHeight:
    def __init__(self, val):
        self.val = val
        self.height = 0

head = TreeNode(TreeNodeWithHeight(3))
head.left = TreeNode(TreeNodeWithHeight(9))
head.right = TreeNode(TreeNodeWithHeight(20))

head.right.left = TreeNode(TreeNodeWithHeight(15))
head.right.right = TreeNode(TreeNodeWithHeight(7))

head.right.right.right = TreeNode(TreeNodeWithHeight(70))
head.right.right.right.right = TreeNode(TreeNodeWithHeight(80))

def check_tree_balanced(root):

    left_height = 0
    right_height = 0

    if root.left:
        if not check_tree_balanced(root.left):
            return False
        left_height = 1 + root.left.val.height
    if root.right:
        if not check_tree_balanced(root.right):
            return False
        right_height = 1 + root.right.val.height

    root.val.height = max(left_height, right_height)
    # print("height at element {} is :{}".format(root.val.val, root.val.height))
    # print("balance factor is: ",abs(left_height-right_height))

    if abs(left_height-right_height) > 1:
        # print("not balanced")
        return False

    return True

# print(check_tree_balanced(head))