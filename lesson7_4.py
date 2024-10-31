import random
def common_elements():
    three = set()
    five = set()
    for i in range(100):
        x = random.randint(3, 100)
        # print(x)
        if x % 3 == 0:
            three.add(x)
        if x % 5 == 0:
            five.add(x)
    # print(f"multiples of three {three}")
    # print(f"multiples of five {five}")
    general_list = three.intersection(five)
    return general_list
print(f"перетин в обох множинах {common_elements()}")