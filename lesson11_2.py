def generate_cube_numbers(end):
    cubed_list = []
    cubed = 0
    for i in range(2,end):
        cubs = True
        if i ** 3 > end:
            cubs = False
        if i ** 3 <= end:
            cubed = i ** 3
            cubed_list.append(cubed)
            yield cubed

from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print("Ok")