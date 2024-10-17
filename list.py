list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_1.insert(0, list_1[-1])
list_1.pop()
print(list_1)

fruits = ["apple", "pear", "banana", "orange", "watermelon"]
fruits.insert(0, fruits[len(fruits) -1])
fruits.pop(len(fruits) -1)
print(fruits)

my_list = [3, 6, 12, 22, 29, 7, 14, 41]
my_list.insert(0, my_list[len(my_list) - 1])
my_list.pop(-1)
print(my_list)

one_digit_list = [777]
one_digit_list.insert(0, one_digit_list[-1])
one_digit_list.pop()
print(one_digit_list)