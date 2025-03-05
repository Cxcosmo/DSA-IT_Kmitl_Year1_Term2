#Input : ["San Francisco", "San Jose", "Sacramento", "Fresno", "Bakersfield", "Reno"]
#Input : 3
#Input : {"Name": "A", "Cities": ["San Francisco", "San Jose", "Sacramento", "Fresno", "Bakersfield"]}
#Input : {"Name": "B", "Cities": ["San Francisco", "San Jose", "Sacramento", "Reno"]}
#Input : {"Name": "C", "Cities": ["San Jose", "Fresno", "Bakersfield"]}
#Output : ['A', 'B']

#Input : ["San Francisco", "San Jose", "Los Angeles", "Sacramento", "San Diego", "Las Vegas", "Reno", "Phoenix"]
#Input : 7
#Input : {"Name": "Nakngam Vibe", "Cities": ["Reno"]}
#Input : {"Name": "Kaewpongpok Tunes", "Cities": ["Las Vegas", "Phoenix"]}
#Input : {"Name": "Wongsomsri Radio", "Cities": ["Reno", "Phoenix", "Las Vegas"]}
#Input : {"Name": "Mincharoen FM", "Cities": ["Los Angeles", "Sacramento"]}
#Input : {"Name": "Purimongkol Station", "Cities": ["San Francisco"]}
#Input : {"Name": "Mongkolsuktavi Tunes", "Cities": ["Reno", "San Jose", "Las Vegas"]}
#Input : {"Name": "Wongchan AM", "Cities": ["San Jose", "Reno"]}
#Output : ['Mincharoen FM', 'Mongkolsuktavi Tunes', 'Purimongkol Station', 'Wongsomsri Radio']

def setCovering(cities, radio, radio_list = []) :
    radio_select = None
    count = 0
    check = False
    for x in cities :
        for y in radio :
            if x in y["Cities"] :
                check = True
                break
    if not cities or not radio or not check :
        return sorted(radio_list)
    for i in radio :
        count_check = 0
        for j in cities :
            if j in i["Cities"] :
                count_check += 1
        if count < count_check :
            radio_select = i
            count = count_check
    if radio_select :
        radio_list.append(radio_select["Name"])
    for i in radio_select["Cities"] :
        if i in cities :
            cities.remove(i)
    radio.remove(radio_select)
    return setCovering(cities, radio, radio_list)

def main() :
    import json
    cities = json.loads(input())
    radio = []
    for _ in range(int(input())) :
        radio.append(json.loads(input()))
    print(setCovering(cities, radio))

main()
