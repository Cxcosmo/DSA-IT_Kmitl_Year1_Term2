#Input : [93, 531, 678, 143, 790, 249, 724, 332, 537, 677]
#Input : [93, 844, 143, 749, 9, 980, 93, 623, 496, 597]
#Input : [93, 216, 356, 672, 141, 93, 675, 343, 781, 534]
#Output : True

#Input : [93, 531, 678, 143, 790, 249, 724, 332, 537, 677]
#Input : [638, 844, 770, 749, 9, 980, 865, 623, 496, 597]
#Input : [116, 216, 356, 672, 141, 323, 675, 343, 781, 534]
#Output : False

import json
def isIntersect(a, b, c) :
    result = False
    for i in b :
        if i in a and i in c :
            result = True
    print(result)
isIntersect(json.loads(input()), json.loads(input()), json.loads(input()))