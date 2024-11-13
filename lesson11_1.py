def prime_generator(end):
    prime_list = []
    for prime_number in range(2, end + 1):
        prime = True
        if prime_number > 1:
            for i in range(2, prime_number - 1):
                if prime_number % i == 0:
                    prime = False
            if prime:
                prime_list.append(prime_number)
                yield prime_number
                prime_number += 1
    return list(prime_list)

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print("Ok")
