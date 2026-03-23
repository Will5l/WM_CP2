# WM Pet Simulator
import sys
from helpers import *
# main will greet them, and then give them all the options. none of them will work until they select a pet to be their main one, or create one if they have none
def main():
    print("Welcome user, this program will simulate pets. You will have to take care of them and keep an eye on their stats. If the pet's stats go to zero, then its health will decay with each action not fixing it, and if health reaches 0 it dies")
    pet = None
    while pet == None:
        choice = input("You currently don't have a pet equipped, you can:\n1.Create a pet\n2.Select already made pet")
        choice = choice.strip()
        if choice == '1':
            pass

        elif choice == '2':
            pet = select_pet()

        else:
            print("Invalid input, please try again")
    while True:
        print("1. Feed pet\n2. Feed pet\n3. Feed pet\n4. Feed pet\n5. Feed pet\n6. Feed pet\n")
        pass