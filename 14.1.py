class GroupLimitError(Exception):
    pass


class Student:
    def __init__(self, gender, age, first_name, last_name, record_book):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError("У групі не може бути більше 10 студентів")
        self.group.add(student)

    def find_student(self, last_name):
        for st in self.group:
            if st.last_name == last_name:
                return st
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = '\n'.join(str(st) for st in self.group)
        return f"Number: {self.number}\n{all_students}"