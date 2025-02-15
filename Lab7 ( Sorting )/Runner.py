#Input : 20 ( ระยะทางรวม )
#Input : 10 ( จำนวนนักวิ่ง )
#Input : 6 2 ( ความเร็ว, จุดเริ่มวิ่ง )
#Input : 6 8
#Input : 4 3
#Input : 1 6
#Input : 8 2
#Input : 5 9
#Input : 2 6
#Input : 8 7
#Input : 4 3
#Input : 9 8
#------------
#Output : 10 ( ลำดับนักวิ่งที่เร็วสุด )


def runner() :
    distance = int(input())
    for i in range(int(input())) :
        runner = input().split()
        runner.append(i)
        if not i :
            faster_runner = runner
        time_faster = (distance - int(faster_runner[1])) / int(faster_runner[0])
        time_runner = (distance - int(runner[1])) / int(runner[0])
        if time_faster > time_runner :
            faster_runner = runner
        elif time_faster == time_runner and int(runner[0]) > int(faster_runner[0]) :
            faster_runner = runner
    print(faster_runner[2] + 1)
runner()
