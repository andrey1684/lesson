user_choise = "yes"
while user_choise:
    first_digit = int(input("please enter first digit:"))
    x = first_digit;
    mathematical_operation = input("operation:")
    z = mathematical_operation;
    second_digit = int(input("please enter second digit:"))
    y = second_digit;
    if z == ("+"):
        solution = x + y;
    elif z == ("-"):
        solution = x - y;
    elif z == ("*"):
        solution = x * y;
    elif z == ("/") and y != 0:
        solution = x / y;
    elif y == 0:
        solution = ("fail, division by zero")
    print(solution)
    user_choise = input("do you want continue: yes or no")
    if user_choise == "yes":
        continue
    if user_choise == "no":
        break
