#Sort x+Y จากน้อย -> มาก ถ้าเท่า y มากมาก่อน
#Input : 2 ( จน.ชุดข้อมูล )
#Input : 2 ( จน.ข้อมูล )
#Input : 10 0 ( x, Y )
#Input : 2 8
#Input : 3
#Input : -5 20
#Input : 1 1
#Input : 10 3
#-------------
#Output : 2 8
#Output : 10 0
#Output : 1 1
#Output : 10 3
#Output : -5 20

def pointSorting() :
    for _ in range(int(input())) :
        point_list = []
        for _ in range(int(input())) :
            point_list.append(input().split(" "))
        while point_list :
            min_point = point_list[0]
            for i in point_list :
                if int(i[0]) + int(i[1]) < int(min_point[0]) + int(min_point[1]) :
                    min_point = i
                elif int(i[0]) + int(i[1]) == int(min_point[0]) + int(min_point[1]) and int(i[1]) > int(min_point[1]) :
                    min_point = i
            print(" ".join(min_point))
            point_list.remove(min_point)
pointSorting()
