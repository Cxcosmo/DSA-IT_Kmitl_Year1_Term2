import json
def isIntersect(a, b, c) :
    result = False
    for i in b :
        if i in a and i in c :
            result = True
    print(result)
isIntersect(json.loads(input()), json.loads(input()), json.loads(input()))