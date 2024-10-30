import string
def correct_sentence(text):
    if text[-1] != "." and text.count(".") == 0:
        result = text.capitalize() + "."
        return result
    if text[-1] != "." and text.count(".") > 0:
        result = text.title() + "."
        return result
    else:
        result = text.capitalize()
        return result


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
