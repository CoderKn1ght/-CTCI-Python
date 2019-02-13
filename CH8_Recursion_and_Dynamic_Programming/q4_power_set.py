def power_set_dynamic_programming(elements):
    print(elements)

    super_set = [[]]
    for element in elements:
        temp_set = [set for set in super_set]
        for list in temp_set:
            current_list = [current_list for current_list in list]
            current_list.append(element)
            super_set.append(current_list)
    return super_set

elements = ['a','b','c']
print(power_set_dynamic_programming(elements))