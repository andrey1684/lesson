# variation_1
# numbers = [0, 12, 4, 6, 0, 21, 43, 7, 0, 0, 0, 25, 1, 2, 3]
# for i in numbers:
#     if i == 0:
#         numbers.remove(i)
#         numbers.append(i)
# print(numbers)


#variation_2
import random
numbers = [] #створення пустого списку
for x in range(50):
    n = round(random.random() * 5)
    numbers.append(n) # постановка випадкових чисел від 0 до 5 у список numbers
# numbers = [0, 12, 4, 6, 0, 21, 43, 7, 0, 0, 0, 25, 1, 2, 3] #у випадку відомого списку
print(numbers)
count_0 = 0
for zero in numbers:
    if zero == 0:
        count_0 = count_0 + 1
print(count_0) #пошук так виведення кількості необхідних значень, у данному випадку "0"

nums = []
zeros = [] #створення нових пустих списків
for i in numbers:
    if i == 0:
        numbers.remove(i)
        numbers.insert(0, 1)
        zeros.insert(0, 0) # видалення з початкового списку та постановка у нових список пошукового значення, та заміна його на значеення 1, для збереження індексу наступного значення
    if i != 0:
        numbers.remove(i)
        numbers.insert(0, 1)
        nums.append(i)
print(nums)
print(zeros)
new_numbers = nums + zeros
print(new_numbers)


