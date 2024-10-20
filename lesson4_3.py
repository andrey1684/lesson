import random
numbers = []
for i in range(random.randint(3, 10)):
    numbers.append(random.randint(1, 20))
new = [(numbers[0]), (numbers[2]), (numbers[-2])]

print(numbers)
print(new)
