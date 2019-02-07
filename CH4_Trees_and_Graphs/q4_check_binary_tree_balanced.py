from CH4_Trees_and_Graphs.TreeNode import TreeNode

class NodeWithDepth(object):

    def __init__(self, val):
        self.val = val
        self.difference = None

head = TreeNode(NodeWithDepth(3))
head.left = TreeNode(NodeWithDepth(9))
head.right = TreeNode(NodeWithDepth(20))

head.right.left = TreeNode(NodeWithDepth(15))
head.right.right = TreeNode(NodeWithDepth(7))

def check_balanced(head):

    if not head:
        return True

    min_depth

check_balanced(head)