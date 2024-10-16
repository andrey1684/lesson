first_digit = int(input("please enter first digit:"))
x = first_digit
user_select = input("please enter operation")
match user_select:
    case "+":
        second_digit = int(input("please enter second digit:"))
        y = second_digit
        print(x + y)
    case "-":
        y = int(input("please enter second digit"))
        print(x - y)
    case "*":
        y = int(input("please enter second digit"))
        print(x * y)
    case "/":
        y = int(input("please enter second digit"))
        if y != 0:
            print(x / y)
        if y == 0:
            print("fail, division by zero")
