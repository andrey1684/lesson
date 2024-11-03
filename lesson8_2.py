import string
def is_palindrome(text):
    text = text.lower()
    palindrome_list = []
    for i in text:
        if not i in string.punctuation + " ":
            palindrome_list.append(i)
    # print(palindrome_list)
    if palindrome_list == palindrome_list[::-1]:
        return True
    if palindrome_list != palindrome_list[::-1]:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")