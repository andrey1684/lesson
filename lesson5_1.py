import keyword
import string
var = ["_", "__", "___", "x", "get_value", "get value", "get!value", "some_super_puper_value",
        "Get_value", "get_Value", "getValue", "3m", "m3", "assert", "assert_exception"]
true_list =[]
false_list = []
n = string.ascii_uppercase + string.punctuation.replace("_", "")
for varic in var:
    if len(varic) > 0:
        if varic[0].isnumeric() == False:
            if varic.islower:
                if varic.count(" ") == 0:
                    if not varic in keyword.kwlist:
                        index = varic.find("_")
                        if index != -1:
                            second = varic.find("_", index + 1)
                            if second - index != 1:
                                true_list.append(varic)
                                # print(f"True {varic}")
                            else:
                                # print(f"False, '__' in {varic}")
                                false_list.append(varic)
                        else:
                            # print(f"True '{varic}'")
                            true_list.append(varic)
                    else:
                        # print(f"False, keyword in '{varic}'")
                        false_list.append(varic)
                else:
                    # print(f"False, ' ' in {varic}")
                    false_list.append(varic)
            else:
                # print(f"False, {varic} is not lower")
                false_list.append(varic)
        else:
            # print(f"False, first symbol in {varic} is numeric")
            false_list.append(varic)
    else:
        # print(f"False, var = 0")
        false_list.append(varic)
# print(f"true_list {true_list}")
# print(f"false list {false_list}")
nn = 0 #number element in true_list
for i in true_list:
    if i in true_list:
        for j in i:
            if j in n:
                # print(f"False {i}")
                false_list.append(i)
                nn += 1
                i = i[nn]
print(f"False elements in var: {false_list}")
for b in false_list:
    if b in true_list:
        true_list.remove(b)
print(f"True elements in var: {true_list}")
