class Laew_Tae_App :
    def __init__(self) :
        self.menu_list = ["Pizza", "Fried Chicken", "Hamburger", "Steak"]
        self.count_random = 1

    def add_menu(self, new_menu) :
        self.menu_list.append(new_menu)

    def random_foods(self) :
        self.count_random += 1

    def list_foods(self) :
        return sorted(self.menu_list)
    
LaewTaeApp = Laew_Tae_App()
for _ in range(int(input())) :
    LaewTaeApp.add_menu(input())
print(LaewTaeApp.list_foods())
