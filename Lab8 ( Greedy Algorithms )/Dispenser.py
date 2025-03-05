def dispenser(n, m) :
    dispenser_list = []
    for x in range(m) :
        dispenser_list.append([None] * n)
    for i in range(n) :
        num = input().split()
        for j in range(m) :
            (dispenser_list[j])[i] = int(num[j])
    result = ""
    while dispenser_list != [[]] * m:
        max_check = []
        for i in range(m) :
            if len(dispenser_list[i]) :
                max_check.append(dispenser_list[i].pop(len(dispenser_list[i]) - 1))
        num = max(max_check)
        result += str(num)
        max_check[max_check.index(num)] = None
        for j in range(0,len(max_check)) :
            if max_check[j] != None :
                (dispenser_list[j]).append(max_check[j])
    print(result)
dispenser(int(input()), int(input()))
