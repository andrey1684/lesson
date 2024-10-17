list = [1, 2, 3, 4, 5, 6, 7, 8]
first = list[0: len(list) // 2]
second = list[len(list) // 2 :]
print(first)
print(second)
print(first, second)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first = list1[0: (len(list1) + 1) // 2]
second = list1[(len(list1) + 1) // 2:]
print(first, second)

no_element_list = []
first = no_element_list[:]
second = no_element_list [:]
print(first, second)