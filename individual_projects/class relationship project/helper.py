import csv

#Function to create new character

def char_create():
    name = input("Name:")
    while True:
        char_class = input("1.Knight\n2.Fighter\n3.Wizard\n")
        if char_class == '1':
            char_class = 'Knight'
            health, attack, defense = 20, 8, 10
            break
        elif char_class == '2':
            char_class = 'Fighter'
            health, attack, defense = 20, 10, 5
            break
        elif char_class == '3':
            char_class = 'Wizard'
            health, attack, defense = 15, 20, 3
            break
        else:
            print("Invalid input, try again")
    lvl = 1
    char = Character(name,char_class,health,attack,defense,lvl)
    return char
        

#Class with all the things regarding characters, like attacking or viewing

class Character:
    def __init__(self,name,char_class,health,attack,defense,lvl):
        self.name = name
        self.char_class = char_class
        self.health = health
        self.attack = attack
        self.defense = defense
        self.lvl = lvl
        pass

    def attack_act(self,edef,ehealth):
        atk = (int(self.attack) - int(edef))
        if atk>0:
            print(f"{self.name} did {atk} damage")
            return int(ehealth) - int(atk)
        else:
            print("The attack didn't do enough")
            return 0
    
    def view(self):
        print(f"Name = {self.name}\nClass = {self.char_class}\nHealth = {self.health}\nAttack = {self.attack}\nDefense = {self.defense}\nLevel = {self.lvl}")
    
    def update_data(self):
        try:
            with open('individual_projects/class relationship project/char.csv', mode = 'r', newline='') as csv_file:
                content = csv.reader(csv_file)
                headers = next(content)
                rows = []
                for line in content:
                    rows.append({headers[0]: line[0], headers[1]: line[1], headers[2]: line[2], headers[3]: line[3], headers[4]: line[4], headers[5]: line[5]})
        except:
            print("Can't find the file")
        try:
            with open('individual_projects/class relationship project/char.csv', mode = 'w', newline='') as csv_file:
                fieldnames = ['name', 'char_class', 'health', 'attack', 'defense', 'lvl']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for line in rows:
                        if line['name'] != self.name:
                            writer.writerow({'name': line['name'],
                                                    'char_class':line['char_class'],
                                                    'health': line['health'],
                                                    'attack': line['attack'],
                                                    'defense': line['defense'],
                                                    'lvl':line['lvl']})
                        else:
                            continue

        except:
            print("File not found")

        try:
                with open('individual_projects/class relationship project/char.csv', mode = 'a', newline='') as csv_file:
                    fieldnames = ['name', 'char_class', 'health', 'attack', 'defense', 'lvl']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writerow({'name': self.name,
                                                'char_class':self.char_class,
                                                'health': self.health,
                                                'attack': self.attack,
                                                'defense': self.defense,
                                                'lvl':self.lvl})
        except:
            print("File not found")
    def lvlup(self):
        if self.lvl <30:
            self.health*=1.4
            self.attack*=1.4
            self.defense*=1.4
            self.lvl+=1
        else:
            print("Character is max level, can't level up anymore")
            

#Holds characters in a list with some useful info, and is where the character is selected
class Game:
    def __init__(self):
        self.char_list = []
    


    def add_to_list(self,char_name,char_class,health,attack,defense,lvl):
            char = (char_name,char_class,health,attack,defense,lvl)
            self.char_list.append(char)

    def print_list(self):
        for char in self.char_list:
            print(char)
    
    def selection(self):
        while True:
            found = False
            x=0
            choice = input("Which character would you like?(enter name exactly)\n")
            try:
                    with open('individual_projects/class relationship project/char.csv', mode = 'r') as csv_file:
                        content = csv.reader(csv_file)
                        headers = next(content)
                        rows = []
                        for line in content:
                            rows.append({headers[0]: line[0], headers[1]: line[1], headers[2]: line[2], headers[3]: line[3], headers[4]: line[4], headers[5]: line[5]})
            except:
                    print("Can't find the file")
            else:
                    for line in rows:
                        if line['name'] == choice:
                            name = line['name']
                            char = Character(line['name'],line['char_class'],line['health'],line['attack'],line['defense'],line['lvl'])
                            return char
    def battle(self):
        y=0
        while y<2:
            found = False
            x=0
            if y==0:
                choice = input("Which character would you like for 1?(enter name exactly)\n")
            elif y==1:
                choice = input("Which character would you like for 2?(enter name exactly)\n")
            for char in self.char_list:
                if choice in char:
                    found = True
                else:
                    x+=1
            if found == True:
                try:
                    with open('individual_projects/class relationship project/char.csv', mode = 'r') as csv_file:
                        content = csv.reader(csv_file)
                        headers = next(content)
                        rows = []
                        for line in content:
                            rows.append({headers[0]: line[0], headers[1]: line[1], headers[2]: line[2], headers[3]: line[3], headers[4]: line[4], headers[5]: line[5]})
                except:
                    print("Can't find the file")
                else:
                    for line in rows:
                        if line['name'] == choice:
                            name = line['name']
                            if y==0:
                                char1 = Character(line['name'],line['char_class'],line['health'],line['attack'],line['defense'],line['lvl'])
                                y+=1
                            elif y==1 and name!=char1.name:
                                char2 = Character(line['name'],line['char_class'],line['health'],line['attack'],line['defense'],line['lvl'])
                                y+=1
                            else:
                                print("Either you made an invalid input, or you tried to have the same character for both.")
        char1temp = int(char1.health)
        char2temp = int(char2.health)
        while char1temp>0 and char2temp>0:
            char2temp = char1.attack_act(char2.defense,char2temp)
            char1temp = char2.attack_act(char1.defense,char1temp)
        if char1temp == 0 and char2temp!=0:
            print(f"{char2.name} won")
        elif char2temp == 0 and char1temp!=0:
            print(f"{char1.name} won")