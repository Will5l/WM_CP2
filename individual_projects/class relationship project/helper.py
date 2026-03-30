import csv
class Character:
    def __init__(self,name,char_class,health,attack,defense):
        self.name = name
        self.char_class = char_class
        self.health = health
        self.attack = attack
        self.defense = defense
        pass
    
    def attack(self,edef,ehealth):
        atk = (self.attack - edef)
        if atk>0:
            print(f"{self.name} did {atk} damage")
            return ehealth - atk
        else:
            print("The attack didn't do enough")
            return 0
    
    def view(self):
        return (f"""Name = {self.name}\nClass = {self.char_class}\nHealth = {self.health}\nAttack = {self.attack}\nDefense = {self.defense}""")
    
    def remove_pet(pet):
        try:
            with open('individual_projects/class relationship project/char.csv', mode = 'w') as csv_file:
                content = csv.reader(csv_file)
                headers = next(content)
                rows = []
                for line in content:
                    rows.append({headers[0]: line[0], headers[1]: line[1], headers[2]: line[2], headers[3]: line[3], headers[4]: line[4], headers[5]: line[5]})
        except:
            print("Can't find the file")
        else:
            for line in rows:
                    fieldnames = ['name', 'char_class', 'health', 'attack', 'defense' 'lvl']
                    reader = csv.reader(csv_file)
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writerow({'name': line['name'],
                                            'char_class':line['name'],
                                            'Age(Years)': line['name'],
                                            'Hunger': line['name'],
                                            'Happiness': line['name'],
                                            'Energy':line['name'],
                                            'Health': line['name'],
                                            'Healthy': pet.s1,
                                            'Lucky': pet.s2,
                                            'lvl': pet.lvl,
                                            'xp': pet.xp,
                                            })


class Game:
    def __init__(self):
        self.char_list = []
    


    def add_to_list(self,char_name,char_class,lvl):
        self.char_list.append(char_name,char_class,lvl)

    def print_list(self):
        for char in self.char_list:
            print(char)