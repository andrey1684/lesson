class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.gender} {self.age}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f"{self.record_book}"

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        for student in self.group.copy():
            if student.last_name == last_name:
                self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group.copy():
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = ""
        for student in self.group:
            all_students += student.__str__() + '\n'
        return f'Number:{self.number}\n{all_students}'

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student("Male", 61, "Michael", "Jordan", "NBA148")
st4 = Student("Male", 48, "Andrey", "Shevchenko", "Football010")
st5 = Student("Male", 43, "Roger", "Federer", "Tennis225")
gr = Group("Famous")
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert str(gr.find_student("Shevchenko")) == str(st4), "Test3"
assert gr.find_student("Shumacher") is None, "Test4"
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
gr.delete_student('Taylor')
# print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
