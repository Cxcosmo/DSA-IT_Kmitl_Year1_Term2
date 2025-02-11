class Student :
    def __init__(self, std_id: int, name: str, gpa: float) :
        self.__std_id = std_id
        self.__name = name
        self.__gpa = gpa

    def get_std_id(self) :
        return self.__std_id
    def get_name(self) :
        return self.__name
    def get_gpa(self) :
        return self.__gpa
    def print_details(self) :
        print(f"ID: {self.__std_id}")
        print(f"Name: {self.__name}")
        print(f"GPA: {self.__gpa:.02f}")

class BinarySearch :
    def __init__(self, data) :
        self.data = data
    def search (self, name) :
        """recursive (ขอแอ็คนิดนึง อิอิ)"""
        def search_recursive(begin, end, count = 1) :
            if begin > end :
                return None, count - 1
            mid = ( end + begin ) // 2
            if self.data[mid].get_name() > name :
                end = mid - 1
                return search_recursive(begin, end, count + 1)
            elif self.data[mid].get_name() < name :
                begin = mid + 1
                return search_recursive(begin, end, count + 1)
            else :
                return mid, count
        index_data, count = search_recursive(0, len(self.data) - 1)
        if index_data != None :
            print(f"Found {name} at index {index_data}")
            self.data[index_data].print_details()
        else :
            print(f"{name} does not exists.")
        print(f"Comparisons times: {count}")

        """While loop"""
        # begin = 0
        # end = len(self.data) - 1
        # count = 1
        # index_data = None

        # while begin <= end :
        #     mid = ( begin + end ) // 2
        #     if self.data[mid].get_name() > name :
        #         end = mid - 1
        #         count += 1
        #     elif self.data[mid].get_name() < name :
        #         begin = mid + 1
        #         count += 1
        #     else :
        #         index_data = mid
        #         begin = end + 1

        # if index_data != None :
        #     print(f"Found {name} at index {index_data}")
        #     self.data[index_data].print_details()
        # else :
        #     print(f"{name} does not exists.")
        #     count -= 1
        # print(f"Comparisons times: {count}")

def main() :
    import json
    student_list = json.loads(input())
    for i in range(0, len(student_list)) :
        student_list[i] = Student(student_list[i]["id"], student_list[i]["name"], student_list[i]["gpa"])
    student_data = BinarySearch(student_list)
    student_data.search(input())
main()
