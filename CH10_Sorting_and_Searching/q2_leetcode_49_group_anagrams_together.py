from collections import OrderedDict
def group_anagrams(strs):

    dict = {}
    for string in strs:
        string_sorted = ''.join(sorted(string))
        if string_sorted in dict:
            dict[string_sorted].append(string)
            continue
        dict[string_sorted] = [string]

    answer_list = []
    for key in dict:
        answer_list.append(dict[key])

    print(answer_list)


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
group_anagrams(strs)