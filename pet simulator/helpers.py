import csv

def class_setter():
    class Animal:
        def __init__(self, name, species, age, hunger, happiness, energy):
            self.name = name.capitalize()
            self.species = species.capitalize()
            self.age = age
            self.hunger = hunger
            self.happiness = happiness
            self.energy = energy

            def __str__(self):
                return (f"""Name = {self.name}\nSpecies = {self.species}\nAge = {self.age}\nHunger = {self.hunger}\nHappiness\nEnergy = {self.energy}""")
            
            def feed(self, food_hunger, food_energy):
                self.hunger += food_hunger
                self.energy += food_energy