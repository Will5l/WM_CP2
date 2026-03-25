# WM Pet Simulator
import sys
from helpers import *
# main will greet them, and then give them all the options. none of them will work until they select a pet to be their main one, or create one if they have none
def main():
    time = 8
    print("Welcome user, this program will simulate pets. You will have to take care of them and keep an eye on their stats. If the pet's stats go to zero, then its health will decay with each action not fixing it, and if health reaches 0 it dies")
    pet = None
    while pet == None:
        choice = input("You currently don't have a pet equipped, you can:\n1.Create a pet\n2.Select already made pet")
        choice = choice.strip()
        if choice == '1':
            pet = create_pet()

        elif choice == '2':
            pet = select_pet()

        else:
            print("Invalid input, please try again")
    while True:
        print(pet)
        choice = input(f"Time. {time}:00\n1. Feed pet\n2. Play with pet\n3. Put pet to sleep\n4. Take to vet\n5. Manage pets\n6. Quit\n")
        if choice == '1':
            while True:
                type = input("What type of food?\n1.Basic\n2.Treat\n3.Hearty meal")
                if choice == '1':
                    food = (20,10)
                elif choice == '2':
                    food = (10,30)
                elif choice == '3':
                    food = (50,20)
                else:
                    print("Invalid choice, try again")
                pet.feed(food)
                print(f"You fed {pet.name}, hunger+{food[0]} happiness{food[1]}")
                break
        if choice == '2':
            pass
        if choice == '3':
            pass
        if choice == '4':
            pass
        if choice == '5':
            pass
        if choice == '6':
            print("Goodbye")
            sys.exit()
        