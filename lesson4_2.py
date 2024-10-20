import random
numbers = []
even = []
for i in range(random.randint(10, 20)):
    numbers.append(random.randint(1, 100))
even = numbers[0: 20: 2]
print(numbers)
print(even)
print(sum(even))

numbers_2 = [random.randint(1, 100) for i in range(random.randint(10, 20))]
even_2 = numbers_2[0: 20:2]
print(numbers_2)
print(sum(even_2))

num = []
print(sum(num))
