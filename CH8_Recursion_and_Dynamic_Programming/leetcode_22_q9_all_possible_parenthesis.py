def generate_parenthesis(number):
    print("here")

    possible_combinations = []

    for i in range(number):
        if i == 0:
            possible_combinations.append("()")
            continue
        if i == 1:
            new_strings = []
            for string in possible_combinations:
                temp_string = string + "()"
                new_strings.append(temp_string)
                temp_string = string.join("()")
                new_strings.append(temp_string)
            possible_combinations = new_strings
            continue
        if i == 2:
            hash_set = set()
            new_strings = []
            # print("possible_combinations:", possible_combinations)
            for string in possible_combinations:
                temp_string = string.join("()")
                # print("joined", temp_string)
                new_strings.append(temp_string)
                for i in range(0,len(string),2):
                    temp_list = list(string)
                    temp_string = ''.join(temp_list[:i] + ['(',')'] + temp_list[i:])
                    if temp_string not in hash_set:
                        hash_set.add(temp_string)
                        new_strings.append(temp_string)
                        # print("appended: ",temp_string)
            possible_combinations = new_strings
        if i == 3:
            hash_set = set()
            new_strings = []
            print("possible_combinations:", possible_combinations)
            for string in possible_combinations:
                temp_string = string.join("()")
                print("joined", temp_string)
                new_strings.append(temp_string)
                for i in range(0, len(string), 2):
                    temp_list = list(string)
                    temp_string = ''.join(temp_list[:i] + ['(', ')'] + temp_list[i:])
                    if temp_string not in hash_set:
                        hash_set.add(temp_string)
                        new_strings.append(temp_string)
                        print("appended: ", temp_string)
            possible_combinations = new_strings

    print(len(possible_combinations))
    print(possible_combinations)

number = 4
generate_parenthesis(number)