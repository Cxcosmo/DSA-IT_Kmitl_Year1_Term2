class Is_Even :
    def __init__(self, num) :
        self.num = num
    def is_even(self) :
        if int(str(bin(self.num))[-1]) :
            return False
        return True
num_check = Is_Even(int(input()))
print(num_check.is_even())
