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

def infixToPostfix(expression) :
    result = ""
    stack_expression = ArrayStack()
    for i in expression :
        if i.isalpha() :
            result += i
        elif not i.isspace() :
            if i == "(" :
                stack_expression.push(i)
            elif i == ")" :
                for _ in range(stack_expression.get_size()) :
                    x = stack_expression.pop()
                    if x != "(" :
                        result += x
            elif stack_expression.is_empty() :
                stack_expression.push(i)
            elif stack_expression.get_stack_top() in ("*", "/") :
                for _ in range(stack_expression.get_size()) :
                    result += stack_expression.pop()
                stack_expression.push(i)
            elif ( i == "+" and stack_expression.get_stack_top() == "-") or (i == "-" and stack_expression.get_stack_top() == "+") :
                for _ in range(stack_expression.get_size()) :
                    result += stack_expression.pop()
                stack_expression.push(i)
            else :
                stack_expression.push(i)

    for _ in range(stack_expression.get_size()) :
        result += stack_expression.pop()
    print(result)
infixToPostfix(input())
