def power_set_dynamic_programming(elements):
    print(elements)

    super_set = []
    for i in range(len(elements)+1):
        if i == 0:
            super_set.append([])
            continue
        temp_set = []
        for list in super_set:
            temp_set.append(list)
        super_set.append([elements[i-1]])
        for list in temp_set:
            if list:
                temp_list = []
                for element in list:
                    temp_list.append(element + elements[i-1])
                super_set.append(temp_list)
    print(super_set)
    size = 0
    for list in super_set:
        size += len(list)

    print(size+1)

elements = ['a','b','c','d']
power_set_dynamic_programming(elements)