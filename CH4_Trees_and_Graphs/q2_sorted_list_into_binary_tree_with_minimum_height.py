from CH4_Trees_and_Graphs.TreeNode import TreeNode

sorted_list = [1,2,3,4,5]

def construct_tree(sorted_list):
    length = len(sorted_list)
    mid_index = int(((length) + 1)/ 2)
    print(mid_index)

construct_tree(sorted_list)