import re

cleaned = list()
def delete_html_tags(file, results_file = "cleaned.txt"):
    with open("draft.html", "r", encoding = "utf-8") as file:
        for line in file:
            text = re.findall(r">[\SА-Яа-я\s+]+<", line)
            if len(text) > 0:
                print(text)
                text = str(text)
                with open("cleaned.txt", 'a') as txt_file:
                    txt_file.write(text)


delete_html_tags("draft.html", results_file="cleaned.txt")
