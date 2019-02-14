# do it using recursion
# do it geeks for geeks way (dfs kinda thing)


def permutations_without_duplicates(string):

    previous_list = []

    for i in range(len(string)):
        if i == 0:
            previous_list = [string[i]]
            continue
        current_list = []
        for single_string in previous_list:
            for insert_index in range(len(single_string)+1):
                temp_string = [i for i in single_string]
                temp_string.insert(insert_index,string[i])
                current_list.append(''.join(temp_string))
        previous_list = current_list

    print(len(previous_list))
    return previous_list

nums = "abc"
print(permutations_without_duplicates(nums))