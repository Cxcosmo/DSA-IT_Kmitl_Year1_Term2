#Input : 127
#Input : {"10": 10, "5": 10, "2": 10, "1": 10}
#Output : Amount: 127
#Output : Coin exchange result:
#Output :   10 baht = 10 coins
#Output :   5 baht = 5 coins
#Output :   2 baht = 1 coins
#Output :   1 baht = 0 coins
#Output : Number of coins: 16

#Input : 249
#Input : {"10": 10, "5": 10, "2": 10, "1": 10}
#Output : Amount: 249
#Output : Coins are not enough.

#Input : 17
#Input : {"10": 0, "5": 1, "2": 2, "1": 10}
#Output : Amount: 17
#Output : Coin exchange result:
#Output :   10 baht = 0 coins
#Output :   5 baht = 1 coins
#Output :   2 baht = 2 coins
#Output :   1 baht = 8 coins
#Output : Number of coins: 11

class CoinExchange :
    def __init__(self, amount, coins) :
        self.amount = amount
        self.coins = coins
        self.result = []
        self.count = 0
    
    def find_coin(self) :
        if not self.coins :
            return
        coin = (list(self.coins.keys()))[0]
        count_coin = self.amount // coin
        if count_coin > self.coins[coin] :
            count_coin = self.coins[coin]
        self.amount -= coin * count_coin
        self.count += count_coin
        self.result.append(f"  {coin} baht = {count_coin} coins")
        self.coins.pop(coin)
        self.find_coin()

    def exchange(self) :
        print(f"Amount: {self.amount}")
        self.find_coin()
        if self.amount > 0 :
            print("Coins are not enough.")
        else :
            print("Coin exchange result:")
            for i in self.result :
                print(i)
            print(f"Number of coins: {self.count}")

def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}

def main():
    import json
    amount = int(input())
    data = convert_key(json.loads(input()))
    coinExchange = CoinExchange(amount, data)
    coinExchange.exchange()

main()
