import csv
import random

def random_event(healthy, lucky, seeker):
    x = random.randint(1,100)
    if x > 50 or lucky == True:
        if x <75:
            return 20, 0
        elif x <= 100 and healthy:
            



def class_setter():
    class Animal:
        def __init__(self, name, species, age, hunger, happiness, energy, health, healthy, lucky, seeker):
            self.name = name.capitalize()
            self.species = species.capitalize()
            self.age = age
            self.hunger = hunger
            self.happiness = happiness
            self.energy = energy
            self.health = health
            self.s1 = healthy
            self.s2 = lucky
            self.s3 = seeker
            # When printed, the object will print all the data related to it
            def __str__(self):
                return (f"""Name = {self.name}\nSpecies = {self.species}\nAge = {self.age}\nHunger = {self.hunger}%\nHappiness = {self.happiness}%\nEnergy = {self.energy}%\nHealth = {self.health}%""")
            # Function for feeding
            def feed(self, food_hunger, food_energy):
                self.hunger += food_hunger
                self.energy += food_energy
                if self.hunger >100:
                    self.hunger = 100
                if self.energy > 100:
                    self.energy = 100
                self.happiness, self.health += random_event(self.s1,self.s2,self.s3)
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
            # Function for sleeping
            def sleep(self):
