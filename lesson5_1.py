import keyword
import string
key = keyword.kwlist
pun = ['!', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '^', '`', '{', '|', '}', '~']
var = input(str("please enter the variable:"))
while var:
    if var[0].isnumeric():
        print(False)
        break
    if var in key:
        print(False)
        break
    if var.istitle():
        print(False)
        break
    if var.isupper():
        print(False)
        break
    for i in var:
        if pun.count(i) == True:
            print(False)
            break
    for i in var:
        if var.count("_") > 1 or var.count(" ") > 0 and i.istitle():
            print(False)
            break
        if pun.count(i) == 0 and var.count("_") <= 1:
            print(True)
            break
    break