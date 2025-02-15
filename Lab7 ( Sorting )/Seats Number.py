# Insertion Sort
#Input : ["I639", "O82", "N877", "S123", "S187", "P525", "R94", "Z967", "R797", "K363"]
#Input : 9 ( index ที่ sort ตัวสุดท้าย )
#Output : ['I639', 'O82', 'N877', 'S123', 'S187', 'P525', 'R94', 'Z967', 'R797', 'K363']
#Output : ['I639', 'N877', 'O82', 'S123', 'S187', 'P525', 'R94', 'Z967', 'R797', 'K363']
#Output : ['I639', 'N877', 'O82', 'S123', 'S187', 'P525', 'R94', 'Z967', 'R797', 'K363']
#Output : ['I639', 'N877', 'O82', 'S123', 'S187', 'P525', 'R94', 'Z967', 'R797', 'K363']
#Output : ['I639', 'N877', 'O82', 'P525', 'S123', 'S187', 'R94', 'Z967', 'R797', 'K363']
#Output : ['I639', 'N877', 'O82', 'P525', 'R94', 'S123', 'S187', 'Z967', 'R797', 'K363']
#Output : ['I639', 'N877', 'O82', 'P525', 'R94', 'S123', 'S187', 'Z967', 'R797', 'K363']
#Output : ['I639', 'N877', 'O82', 'P525', 'R94', 'R797', 'S123', 'S187', 'Z967', 'K363']
#Output : ['I639', 'K363', 'N877', 'O82', 'P525', 'R94', 'R797', 'S123', 'S187', 'Z967']
#Output : Comparison times: 25

# Selection Sorting
#Input : ["A1", "A2", "B3", "B2", "B1", "D1", "C1"]
#Input : 6
#Output : ['A1', 'A2', 'B3', 'B2', 'B1', 'D1', 'C1']
#Output : ['A1', 'A2', 'B3', 'B2', 'B1', 'D1', 'C1']
#Output : ['A1', 'A2', 'B1', 'B2', 'B3', 'D1', 'C1']
#Output : ['A1', 'A2', 'B1', 'B2', 'B3', 'D1', 'C1']
#Output : ['A1', 'A2', 'B1', 'B2', 'B3', 'D1', 'C1']
#Output : ['A1', 'A2', 'B1', 'B2', 'B3', 'C1', 'D1']
#Output : Comparison times: 21

# Bubble Sorting
#Input : ["C1", "D1", "B2", "B2", "B3", "A2", "A1"]
#Input : 6
#Output : ['A1', 'C1', 'D1', 'B2', 'B2', 'B3', 'A2']
#Output : ['A1', 'A2', 'C1', 'D1', 'B2', 'B2', 'B3']
#Output : ['A1', 'A2', 'B2', 'C1', 'D1', 'B2', 'B3']
#Output : ['A1', 'A2', 'B2', 'B2', 'C1', 'D1', 'B3']
#Output : ['A1', 'A2', 'B2', 'B2', 'B3', 'C1', 'D1']
#Output : ['A1', 'A2', 'B2', 'B2', 'B3', 'C1', 'D1']
#Output : Comparison times: 21

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
            self.print_join()
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
            self.print_join()
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
            self.print_join()
        print(f"Comparison times: {self.compar_time}")

    def print_join(self) :
        new_data_list = []
        for i in self.data_list :
            new_data_list.append(i[0] + str(i[1]))
        print(new_data_list)

def Seats_Number() :
    import json
    new_list = []
    for i in json.loads(input()) :
        x = []
        x.append(i[0])
        x.append(int(i[1:]))
        new_list.append(x)
    data_list = Sorting(new_list, int(input()))
    # data_list.insertionSort()
    # data_list.selectionSort()
    data_list.bubbleSort()
Seats_Number()
