class Student :
    def __init__(self, std_id: int, name: str, gpa: float) :
        self.__std_id = std_id
        self.__name = name
        self.__gpa = gpa

    def get_std_id(self) :
        return self.__std_id
    def get_name(self) :
        return self.__std_id
    def get_gpa(self) :
        return self.__std_id
    def print_details(self) :
        print(f"ID: {self.__std_id}")
        print(f"Name: {self.__name}")
        print(f"GPA: {self.__gpa:.02f}")

def main(text_in):
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_details()

main(input())