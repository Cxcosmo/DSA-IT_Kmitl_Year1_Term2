class Laew_Tae_App :
    def __init__(self) :
        self.menu_list = ["Pizza", "Fried Chicken", "Hamburger", "Steak"]
        self.count_random = 1

    def random_foods(self) :
        self.count_random += 1

    def list_foods(self) :
        return sorted(self.menu_list)

print(Laew_Tae_App().list_foods())
