# WM 1st Random Password Generator

import sys

def main():
    print("Welcome to the random password generator.")
    while True:
        choice = input("What would you like to do?\n1.Generate password\n2.Exit")
        if choice == '1':
            password_gen()
        elif choice == '2':
            print("Goodbye")
            sys.exit()
        else:
            print("Invalid, try again")

def password_gen():
    length = input("How long do you want the password?\n")
    uppercase = input("Do you want uppercase letters?y/n\n")
    lowercase = input("Do you want lowercase letters?y/n\n")