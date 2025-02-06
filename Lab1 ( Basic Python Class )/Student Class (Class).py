class student :
    def __init__(self, name, sex, age, student_id, gpa):
        self.name = name
        self.sex = sex
        self.age = age
        self.student_id = student_id
        self.gpa = gpa

    def need_student(self) :
        if self.sex == "Male" :
            sex_check = "Mr"
        else :
            sex_check = "Miss"
        return sex_check

student_list = []
for _ in range(3) :
    student_list.append(student(input(), input(), int(input()), input(), float(input())))
need_id = input()
student_check = False

for i in student_list :
    if i.student_id == need_id :
        student_check = True
        index_student = student_list.index(i)

if not student_check :
    print("Student not found")
else :
    student = student_list[index_student]
    print(f"{student.need_student()} {student.name} ({student.age}) ID: {need_id} GPA {student.gpa:.2f}")
