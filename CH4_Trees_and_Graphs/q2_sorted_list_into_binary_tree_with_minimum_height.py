from CH4_Trees_and_Graphs.TreeNode import TreeNode

sorted_list = [0,1,2,3,4]

def return_min_element(start, end):
    mid_index = int((start + end) / 2)
    return sorted_list[mid_index]

def return_mid_index(start, end):
    mid_index = int((start + end) / 2)
    return sorted_list[mid_index]

def construct_tree():
    start = 0
    end = len(sorted_list) - 1
    head = TreeNode(return_min_element(start, end))

construct_tree(sorted_list)