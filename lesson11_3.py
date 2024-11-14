def is_even(number):
    number = str(number)
    if number[-1] == "0" or number[-1] == "2" or number[-1] == "4" or number[-1] == "6" or number[-1] == "8":
        return True
    else:
        return False
#
assert is_even(150) == True
assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
