import string
first = input("first_symbol")
second =input("second_symbol")
elements = first, "-", second
elements = list(elements)
abc = string.ascii_letters
# print("".join(elements))
answer = []
first = abc.find(first)
second = abc.find(second)
# print(first)
# print(second)
x = int(second) - int(first)
if x < 0:
    print("not correct range")
answer = abc[first: int(second) + 1]
print(answer)


# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA