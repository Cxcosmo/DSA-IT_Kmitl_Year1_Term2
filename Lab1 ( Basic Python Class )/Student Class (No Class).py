def Student_Class() :
    name = []
    sex = []
    age = []
    student_id = []
    gpa = []
    for _ in range(3) :
        name.append(input())
        sex.append(input())
        age.append(int(input()))
        student_id.append(input())
        gpa.append(float(input()))
    need_id = input()
    if not need_id in student_id :
        return "Student not found"
    index_id = student_id.index(need_id)
    if sex[index_id] == "Male" :
        sex_check = "Mr"
    else :
        sex_check = "Miss"
    return f"{sex_check} {name[index_id]} ({age[index_id]}) ID: {need_id} GPA {gpa[index_id]:.2f}"
print(Student_Class())
