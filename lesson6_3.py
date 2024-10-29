digit = [999, 1000, 423, 33, 25, 1]
n = 0
for i in digit:
    i = digit[n]
    if i > 9:
        while i > 9:
            a = i // 100
            b = i % 100 // 10
            c = i % 100 % 10
            if a != 0:
                digit1 = a * b * c
                if digit1 > 9:
                    i = digit1
                else:
                    print(digit1)
                    break
            else:
                if b != 0:
                    digit1 = b * c
                    if digit1 > 9:
                        i = digit1
                    else:
                        print(digit1)
                        break
    else:
        print(i)
    n += 1

#
# digit = int(input("please enter digit"))
# while digit > 9:
#     a = digit // 100
#     b = digit % 100 // 10
#     c = digit % 100 % 10
#     if a != 0:
#         digit1 = a * b * c
#         if digit1 > 9:
#             digit = digit1
#         else:
#             print(digit1)
#             break
#     else:
#         if b != 0:
#             digit1 = b * c
#             if digit1 > 9:
#                 digit = digit1
#             else:
#                 print(digit1)
#                 break
# else:
#     print(digit)
