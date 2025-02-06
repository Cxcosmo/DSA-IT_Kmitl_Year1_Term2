class DataNode :
    def __init__(self, data = None) :
        self.data = data
        self.next = None

class SinglyLinkedList :
    def __init__(self) :
        self.count = 0
        self.head = None

    def insert_last(self, data) :
        new_data = DataNode(data)
        if self.head is None :
            self.head = new_data
        else :
            data = self.head
            while data.next :
                data = data.next
            data.next = new_data
        self.count += 1

    def insert_front(self, data) :
        new_data =  DataNode(data)
        if self.head is None :
            self.head = new_data
        else :
            new_data.next = self.head
            self.head = new_data
        self.count += 1


    def insert_before(self, node, data) :
        point = self.head
        new_data = DataNode(data)
        if point is None :
            print("Cannot insert, " + node + " does not exist.")
            return
        if point.data == node :
            new_data.next = self.head
            self.head = new_data
            self.count += 1
            return
        while point :
            if point.next == None :
                print("Cannot insert, " + node + " does not exist.")
                return
            elif point.next.data == node :
                new_data.next = point.next
                point.next = new_data
                self.count += 1
                return
            point = point.next

    def delete(self, data) :
        point = self.head
        if point is None :
            print("Cannot delete, " + data + " does not exist.")
            return
        if point.data == data :
            self.head = point.next
            self.count -= 1
            return
        while point :
            if point.next == None :
                print("Cannot delete, " + data + " does not exist.")
                return
            elif point.next.data == data :
                point.next = point.next.next
                self.count -= 1
                return
            point = point.next

    def traverse(self) :
        point = self.head
        data_output = ""
        if point is None :
            print("This is an empty list.")
            return 
        while point :
            data_output += point.data + " -> "
            point = point.next
        print(data_output.strip(" -> "))

def main():
    my_list = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            my_list.insert_front(data)
        elif condition == "L":
            my_list.insert_last(data)
        elif condition == "B":
            my_list.insert_before(*data.split(", "))
        elif condition == "D":
            my_list.delete(data)
        else:
            print("Invalid Condition!")
    my_list.traverse()
main()
