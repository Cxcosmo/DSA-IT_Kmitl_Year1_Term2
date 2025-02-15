# Insertion Sort
#Input : [973, 436, 732, 349, 552, 622, 258, 933, 240, 57]
#Input : 6 ( index ที่ sort ตัวสุดท้าย )
#Output : [436, 973, 732, 349, 552, 622, 258, 933, 240, 57]
#Output : [436, 732, 973, 349, 552, 622, 258, 933, 240, 57]
#Output : [349, 436, 732, 973, 552, 622, 258, 933, 240, 57]
#Output : [349, 436, 552, 732, 973, 622, 258, 933, 240, 57]
#Output : [349, 436, 552, 622, 732, 973, 258, 933, 240, 57]
#Output : [258, 349, 436, 552, 622, 732, 973, 933, 240, 57]
#Output : Comparison times: 18

# Selection Sort
#Input : [5, 4, 3, 2, 1]
#Input : 4
#Output : [1, 2, 3, 4, 5]
#Output : [1, 2, 3, 4, 5]
#Output : [1, 2, 3, 4, 5]
#Output : [1, 2, 3, 4, 5]
#Output : Comparison times: 10

# Bubble Sort
#Input : [5, 4, 3, 2, 1]
#Input : 4
#Output : [1, 5, 4, 3, 2]
#Output : [1, 2, 5, 4, 3]
#Output : [1, 2, 3, 5, 4]
#Output : [1, 2, 3, 4, 5]
#Output : [1, 2, 3, 4, 5]
#Output : Comparison times: 10

class Sorting :
    def __init__(self, data_list, last_index) :
        self.data_list = data_list
        self.last_index = last_index
        self.compar_time = 0

    def insertionSort(self) :
        """Insertion Sort"""
        for i in range(1, self.last_index + 1) :
            current = i
            walker = current - 1
            while walker >= 0 and self.data_list[current] < self.data_list[walker] :
                self.data_list[current], self.data_list[walker] = self.data_list[walker],self.data_list[current]
                walker -= 1
                current -= 1
                self.compar_time += 1
            if self.data_list[current] >= self.data_list[walker] and walker >= 0 :
                self.compar_time += 1
            print(self.data_list)
        print(f"Comparison times: {self.compar_time}")

    def selectionSort(self) :
        """Selection Sort"""
        for i in range(self.last_index) :
            current = i
            smaller = current
            walker = current + 1
            while walker <= self.last_index :
                self.compar_time += 1
                if self.data_list[walker] < self.data_list[smaller] :
                    smaller = walker
                walker += 1
            self.data_list[smaller], self.data_list[current] = self.data_list[current], self.data_list[smaller]
            print(self.data_list)
        print(f"Comparison times: {self.compar_time}")
    
    def bubbleSort(self) :
        """Bubble Sort"""
        current = 0
        sorted_check = False
        while current <= self.last_index and not sorted_check :
            walker = self.last_index
            sorted_check = True
            while walker > current :
                self.compar_time += 1
                if self.data_list[walker] < self.data_list[walker - 1] :
                    sorted_check = False
                    self.data_list[walker], self.data_list[walker - 1] = self.data_list[walker - 1], self.data_list[walker]
                walker -= 1
            current += 1
            print(self.data_list)
        print(f"Comparison times: {self.compar_time}")

def main() :
    import json
    data_list = Sorting(json.loads(input()), int(input()))
    data_list.insertionSort()
    # data_list.selectionSort()
    # data_list.bubbleSort()
main()
