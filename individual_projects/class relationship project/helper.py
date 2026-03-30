class Character:
    def __init__(self,name,char_class,health,attack,defense):
        self.name = name
        self.char_class = char_class
        self.health = health
        self.attack = attack
        self.defense = defense
        pass



class Game:
    def __init__(self):
        self.char_list = []
    


    def add_to_list(self,char_name):
        self.char_list.append(char_name)

    def print_list(self):
        for char in self.char_list:
            print(char)