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

def is_parentheses_matching(expression) :
    check = ArrayStack()
    result = False
    error = True
    for i in expression :
        if i == "(" :
            check.push(i)
        elif i == ")" :
            error = check.pop()
    if check.is_empty() and error :
        result = True
    return result

def main(x) :
    result = is_parentheses_matching(x)
    if result :
        print(f"Parentheses in {x} are matched")
    else :
        print(f"Parentheses in {x} are unmatched")
    print(result)
main(input())
