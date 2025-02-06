class ArrayStack :
    def __init__(self) :
        self.size = 0
        self.data = list()
    def push(self, input_data) :
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit() :
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1
    def pop(self) :
        if self.data :
            self.size -= 1
            return self.data.pop(self.size)
        else :
            print("Underflow: Cannot pop data from an empty list")
    def is_empty(self) :
        if not self.data :
            return True
        return False
    def get_stack_top(self) :
        if self.data :
            x = self.data.pop(self.size - 1)
            self.data.append(x)
            return x
        else :
            print("Underflow: Cannot get stack top from an empty list")
            return None
    def get_size(self) :
        return self.size
    def print_stack(self) :
        return print(self.data)

def main(m, n) :
    student_name = ArrayStack()
    student_group = ArrayStack()
    x = ArrayStack()
    for _ in range(n) :
        student_name.push(input())
    for _ in range(m) :
        student_group.push(student_name.pop())
    while student_name.data :
        for _ in range(m) :
            x.push(student_group.pop())
        for _ in range(x.size) :
            if student_name.data :
                student_group.push(f"{x.pop()}, {student_name.pop()}")
            else :
                student_group.push(x.pop())
    for _ in range(m) :
        x.push(student_group.pop())
    for i in range(m) :
        print(f"Group {i + 1}: {x.pop()}")
main(int(input()), int(input()))
