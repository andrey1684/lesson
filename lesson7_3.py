import string
def second_index(text, some_str):
    index_first = text.find(some_str)
    if text.count(some_str) >= 2:
        index_second = text.find(some_str, index_first + 1)
        return index_second

# print(second_index("hi", "h"))
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
