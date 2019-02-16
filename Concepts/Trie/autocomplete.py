class Trie(object):
    def __init__(self):
        self.childrens = {}
        self.end_of_word = False

def insert_words(list, root):

    current_trie_node = root

    for word in list:
        for letter in word:
            if letter not in current_trie_node.childrens:
                temp_trie_node = Trie()
                current_trie_node.childrens[letter] = temp_trie_node
                current_trie_node = temp_trie_node
            else:
                current_trie_node = current_trie_node.childrens[letter]
        current_trie_node.end_of_word = True
        current_trie_node = root

def get_all_words(root):

    current_string_as_list = []
    current_string = ""
    all_words = []

    return get_all_words_util(root, current_string, all_words)

def get_all_words_util(current_node, current_string, all_words):

    if current_node.end_of_word:
        all_words.append(current_string)
    #     Here because, all words is not primitive data type, therefore it's not required to return
    #  all words everytime in recursion call
    #  Just return it once when function finishes execution
    #  all values will be added to original list

    for children in current_node.childrens:
        # simplly appending will append in original list and that will not work in recursion
        # how python handles lists assignment and string is different
        # with strings we do not need to create new variable
        # current_string.append(children)
        # current_string = current_string[:]

        current_string += children
        get_all_words_util(current_node.childrens[children], current_string, all_words)
        current_string = current_string[:-1]

    return all_words

def is_word_present(current, word):

    for char in word:
        if char not in current.childrens:
            return False
        current = current.childrens[char]
    if current.end_of_word == True:
        return True
    return False

def complete_autocomplete(current, prefix):

    for char in prefix:
        if char not in current.childrens:
            return False
        current = current.childrens[char]

    autocomplete_list = []
    print(complete_autocomplete_util(current, autocomplete_list, prefix))

def complete_autocomplete_util(current, autocomplete_list, prefix):

    if current.end_of_word:
        autocomplete_list.append(prefix)

    for children in current.childrens:
        prefix = prefix + children
        complete_autocomplete_util(current.childrens[children], autocomplete_list, prefix)
        prefix = prefix[:-1]

    return autocomplete_list



list = ["gaxer","ceer","heer","catabolism","catabolite","cat","cato"]
root = Trie()
insert_words(list, root)
# print(get_all_words(root))
# word = "abcg"
# print(is_word_present(root, word))
prefix ="cat"
complete_autocomplete(root, prefix)


