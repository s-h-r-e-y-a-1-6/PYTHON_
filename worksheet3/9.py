class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None

    def set_class(self, student_class):
        self.student_class = student_class

    def display_attributes(self):
        print(f"ID: {self.student_id}, Name: {self.student_name}, Class: {self.student_class}")

student_id = int(input("Enter student ID: "))
student_name = input("Enter student name: ")
student_class = input("Enter student class: ")

s = Student(student_id, student_name)
s.set_class(student_class)
s.display_attributes()