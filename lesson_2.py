time = int(input("Enter a four-digit number:"))
first_digit = time // 1000;
second_digit = time % 1000 // 100;
third_digit = time % 1000 % 100 // 10;
fourth_digit = time % 1000 % 100 % 10;
print(first_digit)
print(second_digit)
print(third_digit)
print(fourth_digit)


pin_code = int(input("Please enter your pin code:"))
x = pin_code;
first_digit_of_the_code = x // 1000;
n1 = first_digit_of_the_code;
second_digit_of_the_code = x % 1000 // 100;
n2 = second_digit_of_the_code;
third_digit_of_the_code = x % 1000 % 100 // 10;
n3 = third_digit_of_the_code;
fourth_digit_of_the_code = x % 1000 % 100 % 10;
n4 = fourth_digit_of_the_code;
print(x)
print(n1)
print(n2)
print(n3)
print(n4)