#WM Classes Notes

# Example 1
class Animal:
    def __init__(self, name, species, age):
        self.name = name.capitalize()
        self.species = species.capitalize()
        self.age = age

    def __str__(self):
        return (f"""Name = {self.name}\nspecies = {self.species}\nage = {self.age}\n""")
    
    def birthday(self):
        self.age +=1

dog = Animal("Doug", "Dog", 4)
bunny = Animal("Fluffy", "Rabbit", 3)
cat = Animal("Luna", "cat", 4)
print(dog)
print(bunny)
print(cat)
dog.birthday()
print(dog)

# Example 2
class ClassPeriod:
    def __init__(self,subject,teacher = "Ms. LaRose",room = None):
        self.subject = subject.capitalize()
        self.teacher = teacher
        self.room = room

    def __str__(self):
        return f"Subject: {self.subject}\nTeacher: {self.teacher}\nRoom: {self.room}\n"

first = ClassPeriod("Computer Programming 2", room=200)
second = ClassPeriod("Computer Programming 2", room=200)
third = ClassPeriod("Computer Programming 2", room=200)
sixth = ClassPeriod("Computer Programming 2", room=200)
seventh = ClassPeriod("Computer Programming 2", room=200)
eighth = ClassPeriod("Computer Programming 2", room=200)
print(first,second,third,sixth,seventh,eighth)