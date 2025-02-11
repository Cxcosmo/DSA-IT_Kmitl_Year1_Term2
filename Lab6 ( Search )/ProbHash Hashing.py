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

class ProbHash :
    def __init__(self, size: int) :
        self.__hash_table = [None] * size
        self.__size = size

    def hash(self, key:int) :
        return key % self.__size

    def rehash(self, key:int, index_slicing = 0 , count = 1) :
        index_data = self.hash(key) + index_slicing
        if count == self.__size :
            return None
        if index_data == self.__size :
            index_data = 0
            index_slicing = 0 - self.hash(key)
        if not self.__hash_table[index_data] :
            return self.rehash(key, index_slicing + 1 , count + 1)
        if self.__hash_table[index_data].get_std_id() == key :
            return index_data
        else :
            return self.rehash(key, index_slicing + 1 , count + 1)


    def insert_data(self, std:Student, index_slicing = 0) :
        index_hash = self.hash(std.get_std_id()) + index_slicing
        if not None in self.__hash_table :
            print(f"The list is full. {std.get_std_id()} could not be inserted.")
            return
        if index_hash == self.__size :
            index_hash = 0
            index_slicing = 0 - self.hash(std.get_std_id())
            check = self.insert_data(std, index_slicing)
            if not check :
                return False
        if not self.__hash_table[index_hash] :
            self.__hash_table[index_hash] = std
            print(f"Insert {std.get_std_id()} at index {index_hash}")
            return False
        else :
            index_slicing += 1
            check = self.insert_data(std, index_slicing)
            if not check :
                return False

    def search_data(self, std_id) :
        index_data = self.rehash(std_id)
        if index_data != None :
            print(f"Found {std_id} at index {index_data}")
            return self.__hash_table[index_data]
        print(f"{std_id} does not exist.")
        return None

def main():
    import json
    size = int(input())
    hash_table = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hash_table.insert_data(std)
        elif condition == "S":
            print("------")
            student = hash_table.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()