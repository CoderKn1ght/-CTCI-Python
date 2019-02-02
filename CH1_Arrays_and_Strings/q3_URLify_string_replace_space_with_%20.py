import time

s = "Mr John Smith    "

# The following function also uses STRINGBUILDER concept
# First cut of trialing whitespaces using .strip function
# Then insert %20 whereever there is a white space

def using_strip_function(s):
    s = s.strip()
    s = list(s)
    for i, c in enumerate(s):
        if c == ' ':
            s[i] = '%20'
    return ''.join(s)

start_time = time.perf_counter()
print(using_strip_function(s))
end_time = time.perf_counter()
time_taken = end_time - start_time

print('string.strip() : ' + "%.10f" % time_taken + " seconds")

# The following function also uses STRINGBUILDER concept
# First convert the string into list which makes mutating string a constant time operation
# And instead of using .strip function characters are inserted
# Time complexity is increased but it is a possible solution

def manually_shifting_and_inserting(s):
    s = list(s)
    for i, c in enumerate(s):
            if c == ' ':
                length = len(s) - 1
                while length > i + 2:
                    s[length] = s[length-2]
                    length -= 1
                s[i] = '%'
                s[i + 1] = '2'
                s[i + 2] = '0'
    return ''.join(s)

start_time = time.perf_counter()
print(manually_shifting_and_inserting(s))
end_time = time.perf_counter()
time_taken = end_time - start_time

print('insert and shift right time taken : ' + "%.10f" % time_taken + " seconds")
