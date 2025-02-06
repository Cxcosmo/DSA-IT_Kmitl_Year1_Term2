import json
class Max_Min_Avg :
    def __init__(self, list_num) :
        self.list_num = json.loads(list_num)

    def x(self) :
        x_num = self.list_num[0]
        for i in self.list_num :
            if i > x_num :
                x_num = i
        return x_num
    
    def n(self) :
        n_num = self.list_num[0]
        for i in self.list_num :
            if i < n_num :
                n_num = i
        return n_num

    def check(self) :
        avg_num = round(sum(self.list_num) / len(self.list_num), 2)
        return (self.x(), self.n(), avg_num)

num_check = Max_Min_Avg(input())
print(num_check.check())
