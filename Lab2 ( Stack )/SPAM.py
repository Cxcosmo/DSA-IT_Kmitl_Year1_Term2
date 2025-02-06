class stack :
    def __init__(self) :
        self.size = 0
        self.data = []
    def push(self, Data) :
        self.data.append(Data)
        self.size += 1
    def pop(self) :
        if self.data :
            self.size -= 1
            return self.data.pop(self.size)
        else :
            print("Underflow: Cannot pop data from an empty list")
            return None
    def is_empty(self) :
        if not self.data :
            return True
        return False
    def get_stack_top(self) :
        if self.data :
            return self.data[self.size - 1]
        else :
            print("Underflow: Cannot pop data from an empty list")
            return None
    def get_size(self) :
        return self.size
    def print_stack(self) :
        return print(self.data)

def main(spam) :
    check = stack()
    result = True
    for i in spam :
        if i == "(" :
            check.push(1)
        elif i == "{" :
            check.push(2)
        elif i == "[" :
            check.push(3)
        elif i in (")", "}", "]") and not check.get_size() :
            result = False
        elif i == ")" and check.get_stack_top() == 1 :
            check.pop()
        elif i == "}" and check.get_stack_top() == 2 :
            check.pop()
        elif i == "]" and check.get_stack_top() == 3 :
            check.pop()
    if check.get_size() :
        result = False
    return result

str_input = input()
print(main(str_input))
