#Input : 100
#Output : 292

#Input : 1000
#Output : 3893

#Input : 10000
#Output : 48894

def Calculator(n) :
    if n == 1 :
        result = 1
    else :
        result = 0
        len_n = len(str(n))
        if len_n == 2 :
            result += 18
        elif len_n >= 3 :
            result += int(str(len_n - 1) + ("8" * (len_n - 1)))
        r = ""
        for i in range(int("1" + ("0" * (len_n - 1))), n + 1) :
            r += f"{i}+"
        result += len(r)
    print(result)
Calculator(int(input()))