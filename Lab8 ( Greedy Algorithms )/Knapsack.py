#Input : 3
#Input : { "name": "Stereo", "price": 3000, "weight": 3 }
#Input : { "name": "Laptop", "price": 2000, "weight": 2 }
#Input : { "name": "Guitar", "price": 1500, "weight": 1.5 }
#Input : 3.5
#Output : Knapsack Size: 3.5 kg
#Output : ===============================
#Output : Stereo -> 3 kg -> 3000 THB
#Output : Total: 3000 THB

#Input : 6
#Input : { "name": "Sweater", "price": 30, "weight": 0.7 }
#Input : { "name": "Jeans", "price": 40, "weight": 0.8 }
#Input : { "name": "T-Shirt", "price": 15, "weight": 0.3 }
#Input : { "name": "Sneakers", "price": 50, "weight": 1 }
#Input : { "name": "Hat", "price": 20, "weight": 0.2 }
#Input : { "name": "Sunglasses", "price": 25, "weight": 0.1 }
#Input : 3.5
#Output : Knapsack Size: 3.5 kg
#Output : ===============================
#Output : Sunglasses -> 0.1 kg -> 25 THB
#Output : Hat -> 0.2 kg -> 20 THB
#Output : Jeans -> 0.8 kg -> 40 THB
#Output : T-Shirt -> 0.3 kg -> 15 THB
#Output : Sneakers -> 1 kg -> 50 THB
#Output : Sweater -> 0.7 kg -> 30 THB
#Output : Total: 180 THB

class Item :
    def __init__(self, name : str, price : int, weight : float):
        self.__name = name
        self.__price = price
        self.__weight = weight
    def get_name(self) :
        return self.__name
    def get_price(self) :
        return self.__price
    def get_weight(self) :
        return self.__weight
    def get_cost(self) :
        return self.__price / self.__weight

def knapsack(items, knapsack_capacity) :
    print(f"Knapsack Size: {knapsack_capacity} kg")
    print("===============================")
    def recursive(items, knapsack_capacity, total = 0) :
        check = True
        for i in items :
            if knapsack_capacity - i.get_weight() < 0 :
                check = False
            else :
                check = True
                break
        if not items or not check:
            return total
        item : Item = None
        for i in items :
            if not item :
                item = items[0]
            elif knapsack_capacity - i.get_weight() >= 0 and item.get_cost() < i.get_cost() :
                item = i
            elif knapsack_capacity - i.get_weight() >= 0 and item.get_cost() == i.get_cost() and items.index(item) > items.index(i) :
                item = i
        print(f"{item.get_name()} -> {item.get_weight()} kg -> {item.get_price()} THB")
        total += item.get_price()
        knapsack_capacity -= item.get_weight()
        items.remove(item)
        return recursive(items, knapsack_capacity, total)
    
    print(f"Total: {recursive(items, knapsack_capacity)} THB")

def main():
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)
main()
