class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student_id1 = int(input("Enter the ID for Student 1: "))
student_name1 = input("Enter the name for Student 1: ")
student1 = Student(student_id1, student_name1)

student_id2 = int(input("Enter the ID for Student 2: "))
student_name2 = input("Enter the name for Student 2: ")
student2 = Student(student_id2, student_name2)

print(f"Student 1: ID={student1.student_id}, Name={student1.student_name}")
print(f"Student 2: ID={student2.student_id}, Name={student2.student_name}")
