def pow(x):
    return x ** 2
def some_gen(begin, end, func):
    n = 1
    while n <= end:
        x = begin
        begin = pow(x)
        n += 1
        yield x
        # print(x)

from inspect import isgenerator

gen = some_gen(2, 4, pow)

assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print("ok")


#####################################################

def pow(x):
    return x ** 2
def some_gen(begin, end, func):
    n = 1
    for n in range(1, end):
        if n == 1:
            begin = begin
            n += 1
            yield begin
        if n > 1:
            x = begin
            begin = pow(x)
            n += 1
            yield begin

from inspect import isgenerator

gen = some_gen(2, 4, pow)

assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print("ok")
