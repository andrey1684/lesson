import keyword
import string
punqtuation = ['!', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '^', '`', '{', '|', '}', '~']

vvod = input("Please enter text for hashtag: ")
hash = []
h = list(vvod)
y = 0
for i in h:
    if not i in punqtuation:
       hash.insert(y, i)
       y += 1
       # print(hash)
    if i in punqtuation:
        continue
# print(hash)
while True:
    if len(hash) > 140:
        hash.pop()
    else:
         hash.insert(0, "#")
         # print(hash)
         break
hashtag = "".join(hash)
hashtag = hashtag.title()
hashtag = hashtag.replace(" ", "")
print(hashtag)
