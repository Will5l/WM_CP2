import csv
import random

# Have random events for finding treat, or getting sick that skills affect
def random_event(healthy,lucky,name):
    x = random.randint(1,100)
    if x > 50 or lucky == True:
        if x <75:
            print(f"{name} found a treat")
            return 20, 0, 20
        if x >= 75 and healthy != True:
            print(f"{name} got very sick")
            return -20, -40, 0

def select_pet():
    try:
        with open('pet simulator\pets.csv', mode = 'r') as csv_file:
            content = csv.reader(csv_file)
            headers = next(content)
            rows = []
            for line in content:
                rows.append({headers[0]: line[0], headers[1]: line[1], headers[2]: line[2], headers[3]: line[3], headers[4]: line[4], headers[5]: line[5], headers[6]: line[6], headers[7]: line[7], headers[8]: line[8], headers[9]: line[9], headers[10]: line[10]})

    except:
        print("Can't find the file")
    else:
        for line in rows:
            print(f"Name:{line['Name']}")
            print(f"Species:{line['Species']}")
            print(f"Age:{line['Age(years)']}")
            print(f"Hunger:{line['Hunger']}")
            print(f"Happiness:{line['Happiness']}")
            print(f"Energy:{line['Energy']}\n")
            print(f"Health:{line['Health']}\n")
            print(f"Level:{line['lvl']}\n")
    choice = input("Which pet would you like to set as main?: ")
    if choice in line['Name']:
        for i, sublist in enumerate(rows):
            if choice in sublist:
                num = i
                break
        pet_object = Animal(rows[f'{num}'])


    class Animal:
        def __init__(self, name, species, age, hunger, happiness, energy, health, healthy, lucky, lvl, xp):
            self.name = name.capitalize()
            self.species = species.capitalize()
            self.age = age
            self.hunger = hunger
            self.happiness = happiness
            self.energy = energy
            self.health = health
            self.s1 = healthy
            self.s2 = lucky
            self.lvl = lvl
            self.xp = xp
            # When printed, the object will print all the data related to it
            def __str__(self):
                return (f"""Name = {self.name}\nSpecies = {self.species}\nAge = {self.age}\nHunger = {self.hunger}%\nHappiness = {self.happiness}%\nEnergy = {self.energy}%\nHealth = {self.health}%\nLevel = {self.lvl}\nHealthy = {self.healthy}\nLucky = {self.lucky}""")
            # Function for feeding
            def feed(self, food_hunger, food_happiness):
                self.hunger += food_hunger
                self.happiness += food_happiness
                if self.hunger >100:
                    self.hunger = 100
                if self.happiness > 100:
                    self.happiness = 100
                self.happiness, self.health, self.xp += random_event(self.s1,self.s2,self.name)
                if self.health < 0:
                    self.health = 10
            # Function for playing with pet
            def play(self):
                self.happiness += 50
                self.energy -= 40
                self.hunger -= 30
                if self.happiness > 100:
                    self.happiness = 100
                if self.hunger < 0:
                    self.hunger = 0
                    self.health -= 10
                if self.energy < 0:
                    self.energy = 0
                    self.health -= 10
                self.xp += 10
                self.happiness, self.health, self.xp += random_event(self.s1,self.s2,self.name)
                if self.health < 0:
                    self.health = 10
            # Function for sleeping
            def sleep(self):
                self.energy += 90
                self.hunger -= 10
                if self.energy > 100:
                    self.energy = 100
                if self.hunger < 0:
                    self.hunger = 0
                self.happiness, self.health, self.xp += random_event(self.s1,self.s2,self.name)
                if self.health < 0:
                    self.health = 10
            #Function for going to the vet
            def vet(self):
                self.health += 60
                self.hunger -= 10
                self.happiness -= 10
                if self.health > 100:
                    self.health = 100
                if self.hunger < 0:
                    self.hunger = 0
                if self.happiness < 0:
                    self.hapiness = 0
                self.happiness, self.health, self.xp += random_event(self.s1,self.s2,self.name)
                if self.health < 0:
                    self.health = 10
            #Function to decay health if stats are at 0
            def decay(self):
                if self.health == 0:
                    death()
                if self.hunger == 0:
                    self.health -= 10
                if self.happiness == 0:
                    self.health -= 10
                if self.energy == 0:
                    self.health -= 10
                self.happiness, self.health, self.xp += random_event(self.s1,self.s2,self.name)
                if self.health < 0:
                    self.health = 0
            #Function to clear a pet after it dies
            def death(self):
                pass