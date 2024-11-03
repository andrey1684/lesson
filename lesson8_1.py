import string
def add_one (initial_list):
    n = elements_of_initial_list = len(initial_list) - 1
    coefficient = 1
    digit_initial_list = 0
    for i in initial_list:
        if elements_of_initial_list >= 0:
            i = (initial_list[n] * coefficient)
            n -= 1
            coefficient *= 10
            digit_initial_list = i + digit_initial_list
    # print(digit_initial_list)
    add_one_digit = digit_initial_list + 1
    # print(add_one_digit)

    add_one_list = []
    while add_one_digit > 0:
        add_one_list.insert(0, add_one_digit % 10)
        add_one_digit //= 10
    # print(add_one_list)
    return add_one_list



assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

###############################################

def add_one (initial_list):
    degree = len(initial_list) - 1
    index_elements = 0
    digit_of_initial_list = 0
    while degree >= 0:
        digit = initial_list[index_elements]*(10 ** degree)
        degree -= 1
        index_elements += 1
        digit_of_initial_list += digit
    add_one_digit = digit_of_initial_list + 1
    add_one_list = []
    while add_one_digit > 0:
        add_one_list.append(add_one_digit % 10)
        add_one_digit //= 10
    add_one_list.reverse()
    return add_one_list

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

