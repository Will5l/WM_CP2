# WM Pet Simulator
import sys
from helpers import *
# main will greet them, and then give them all the options. none of them will work until they select a pet to be their main one, or create one if they have none
def main():
    print("Welcome user, this program will simulate pets")
    pet = None
    while pet == None:
        choice = input("You currently don't have a pet equipped, you can:\n1.Create a pet\n2.Select already made pet")
        choice = choice.strip()
        if choice == '1':
            pet = functionname

        elif choice == '2':
            pet = functionname

        else:
            print("Invalid input, please try again")
    while True:
        print()
        pass