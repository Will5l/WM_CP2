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
    else:
         return 0,0,0
        
# Save data of pet
def save_pet_data(pet):
    with open('pet simulator/pets.csv', 'a', newline = '') as csv_file:
                    fieldnames = ['Name', 'Species', 'Age(years)', 'Hunger', 'Happiness', 'Energy', 'Health', 'Healthy', 'Lucky', 'lvl', 'xp']
                    reader = csv.reader(csv_file)
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    #writer.writeheader()

                    x = 0
                    writer.writerow({'Name': pet.name,
                                         'Species':pet.species,
                                         'Age(years)': pet.age,
                                         'Hunger': pet.hunger,
                                         'Happiness': pet.happiness,
                                         'Energy':pet.energy,
                                         'Health': pet.health,
                                         'Healthy': pet.s1,
                                         'Lucky': pet.s2,
                                         'lvl': pet.lvl,
                                         'xp': pet.xp,
                                         })
    
# Function to remove pet in case of death or choosing removal
def remove_pet(pet):
    try:
        with open('pet simulator/pets.csv', mode = 'w') as csv_file:
            content = csv.reader(csv_file)
            headers = next(content)
            rows = []
            for line in content:
                rows.append({headers[0]: line[0], headers[1]: line[1], headers[2]: line[2], headers[3]: line[3], headers[4]: line[4], headers[5]: line[5], headers[6]: line[6], headers[7]: line[7], headers[8]: line[8], headers[9]: line[9], headers[10]: line[10]})

    except:
        print("Can't find the file")
    else:
        fieldnames = ['Name', 'Species', 'Age(years)', 'Hunger', 'Happiness', 'Energy', 'Health', 'Healthy', 'Lucky', 'lvl', 'xp']
        reader = csv.reader(csv_file)
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'Name': {0['Name']},
                                         'Species':{rows[0]['Species']},
                                         'Age(years)':{rows[0]['Age(years)']},
                                         'Hunger': {rows[0]['Hunger']},
                                         'Happiness': {rows[0]['Happiness']},
                                         'Energy':{rows[0]['Energy']},
                                         'Health': {rows[0]['Health']},
                                         'Healthy': {rows[0]['Healthy']},
                                         'Lucky': {rows[0]['Lucky']},
                                         'lvl': {rows[0]['lvl']},
                                         'xp': {rows[0]['xp']},
                                         })
        for line in rows:
            if pet.name in line:
                continue
            else:
                fieldnames = ['Name', 'Species', 'Age(years)', 'Hunger', 'Happiness', 'Energy', 'Health', 'Healthy', 'Lucky', 'lvl', 'xp']
                reader = csv.reader(csv_file)
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writerow({'Name': {line['Name']},
                                         'Species':{line['Species']},
                                         'Age(years)':{line['Age(years)']},
                                         'Hunger': {line['Hunger']},
                                         'Happiness': {line['Happiness']},
                                         'Energy':{line['Energy']},
                                         'Health': {line['Health']},
                                         'Healthy': {line['Healthy']},
                                         'Lucky': {line['Lucky']},
                                         'lvl': {line['lvl']},
                                         'xp': {line['xp']},
                                         })


def select_pet():
    try:
        with open('pet simulator/pets.csv', mode = 'r') as csv_file:
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
            print(f"Energy:{line['Energy']}")
            print(f"Health:{line['Health']}")
            print(f"Level:{line['lvl']}")
    choice = input("Which pet would you like to set as main?(enter the name exactly): ")
    if choice in line['Name']:
        num = 0
        for i, sublist in enumerate(rows):
            num += 1
            if choice in sublist:
                break
        pet_object = Animal(rows[num]['Name'],rows[num]['Species'],rows[num]['Age(years)'],rows[num]['Hunger'],rows[num]['Happiness'],rows[num]['Energy'],rows[num]['Health'],rows[num]['Healthy'],rows[num]['Lucky'],rows[num]['lvl'],rows[num]['xp'])
        return pet_object


class Animal:
        def __init__(self, name, species, age, hunger, happiness, energy, health, healthy, lucky, lvl, xp):
            self.name = name.capitalize()
            self.species = species.capitalize()
            self.age = int(age)
            self.hunger = int(hunger)
            self.happiness = int(happiness)
            self.energy = int(energy)
            self.health = int(health)
            self.s1 = healthy
            self.s2 = lucky
            self.lvl = lvl
            self.xp = int(xp)
            self.happinesstem, self.healthtem, self.xptem = 0, 0, 0
            # When printed, the object will print all the data related to it
        def display(self):
                print(f"""Name = {self.name}\nSpecies = {self.species}\nAge = {self.age}\nHunger = {self.hunger}%\nHappiness = {self.happiness}%\nEnergy = {self.energy}%\nHealth = {self.health}%\nLevel = {self.lvl}\nHealthy = {self.s1}\nLucky = {self.s2}""")
            # Function for feeding
        def feed(self, food_hunger, food_happiness):
                self.hunger += food_hunger
                self.happiness += food_happiness
                if self.hunger >100:
                    self.hunger = 100
                if self.happiness > 100:
                    self.happiness = 100
                self.happinesstem, self.healthtem, self.xptem = random_event(self.s1,self.s2,self.name)
                self.happiness += self.happinesstem
                self.health += self.healthtem
                self.xp += self.xptem
                if self.hunger >100:
                    self.hunger = 100
                if self.happiness > 100:
                    self.happiness = 100
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
                self.happinesstem, self.healthtem, self.xptem = random_event(self.s1,self.s2,self.name)
                self.happiness += self.happinesstem
                self.health += self.healthtem
                self.xp += self.xptem
                if self.hunger >100:
                    self.hunger = 100
                if self.happiness > 100:
                    self.happiness = 100
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
                self.happinesstem, self.healthtem, self.xptem = random_event(self.s1,self.s2,self.name)
                self.happiness += self.happinesstem
                self.health += self.healthtem
                self.xp += self.xptem
                if self.hunger >100:
                    self.hunger = 100
                if self.happiness > 100:
                    self.happiness = 100
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
                self.happinesstem, self.healthtem, self.xptem = random_event(self.s1,self.s2,self.name)
                self.happiness += self.happinesstem
                self.health += self.healthtem
                self.xp += self.xptem
                if self.hunger >100:
                    self.hunger = 100
                if self.happiness > 100:
                    self.happiness = 100
                if self.health < 0:
                    self.health = 10
            #Function to clear a pet after it dies
        def death(self):
                print(f"{self.name} died :<")
                remove_pet()
                pet = None
                print("Your active pet died.")
                return
            #Function to increase age
        def age_up(self):
            self.age += 1
            #Function to decay health if stats are at 0
        def decay(self):
                if self.health == 0:
                    self.death()
                if self.hunger == 0:
                    self.health -= 10
                else:
                    self.hunger -= 10
                if self.happiness == 0:
                    self.health -= 10
                else:
                    self.happiness -= 10
                if self.energy == 0:
                    self.health -= 10
                else:
                    self.energy -= 10
                if self.health < 0:
                    self.health = 0


#Function to create a new pet
def create_pet():
    name = input("What is the pets name?\n")
    while True:
        species = input("What species?\n1.Dog\n2.Cat\n3.Fish\n4.Hampster\n5.Bird\n")
        if species == '1':
            species = "Dog"
            break
        elif species == '2':
            species = "Cat"
            break
        elif species == '3':
            species = "Fish"
            break
        elif species == '4':
            species = "Hampster"
            break
        elif species == '5':
            species = "Bird"
            break
        else:
            print("Invalid species selection. Try again")
    while True:
        skill1 = False
        skill2 = False
        skill = input("do you want your pet to be: 1. Lucky(always triggers random events), or 2. Healthy(never gets the sick event)")
        if skill == '1':
            skill1 = True
            break
        if skill == '2':
            skill2 = True
            break
        else:
            print("Invalid selection")
    pet = Animal(name,species,0,100,100,100,100,skill2,skill1,0,0)
    return pet