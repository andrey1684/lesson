return_number = int(input("Please enter five digit number"))
N = return_number;
n1 = N // 10000;
n2 = N % 10000 // 1000;
n3 = N % 10000 % 1000 // 100;
n4 = N % 10000 % 1000 % 100 // 10;
n5 = N % 10000 % 1000 % 100 % 10;
result = n5 * 10000 + n4 * 1000 + n3 * 100 +n2 * 10 + n1;
print(result)