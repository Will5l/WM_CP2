# WM 1st Random Password Generator
import sys
import random
#Create main function that greets them and asks if they want to generate or leave
def main():
    #The program will run until they choose to exit via a while loop.
    print("Welcome to the random password generator.")
    while True:
        choice = input("What would you like to do?\n1.Generate password\n2.Exit\n")
        if choice == '1':
            password_gen()
        elif choice == '2':
            print("Goodbye")
            sys.exit()
        else:
            print("Invalid, try again")

#Make a central function for generating the passwords that asks for the length, and what they want in it.
#Make four helper functions that each handle a different requirment, one for uppercase, lowercase, numbers, and special characters
def password_gen():
    while True:
        #If else statements will check if each of the parameters were checked or not, and skip them if not.
        length = input("How long do you want the password?\n")
        uppercase = input("Do you want uppercase letters?y/n\n")
        lowercase = input("Do you want lowercase letters?y/n\n")
        numbers = input("Do you want numbers?y/n\n")
        special_chars = input("Do you want special characters?y/n\n")
        password = ""
        password_count = 1
        if lowercase != "y" and uppercase != "y" and numbers != "y" and special_chars != "y":
            print("You can't make a password if you choose no on everything")
            continue
        #ensures that the length is actually numeric to avoid code breaking
        if length.isnumeric() == True and length != '0':
            length = int(length)
            break
        else:
            print("length was invalid")
    while password_count <= 4:
        password = ""
        #Have two while loops, one for the passwords length, and one to ensure 4 passwords are made
        #After the password is done being made, it will be printed and then a new one will start being made
        while len(password) < length:
            rng = random.randint(1,4)
            if rng == 1 and uppercase == "y":
                password = upper(password)
            if rng == 2 and lowercase == "y":
                password = lower(password)
            if rng == 3 and numbers == "y":
                password = number(password)
            if rng == 4 and special_chars == "y":
                password = special(password)
                #when the length is met, it is printed out and the password count is increased by 1.
        print(f"{password_count}.{password}")
        password_count += 1
                        
#Each of the four functions will have a random variable to select an option from  the list, and then append the password, before returning it
def upper(password):
    x = random.randint(0,25)
    uppercase_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    y = uppercase_letters[x]
    password += y
    return password

def lower(password):
    x = random.randint(0,25)
    lowercase_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    y = lowercase_letters[x]
    password += y
    return password

def number(password):
    x = random.randint(0,9)
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    y = numbers[x]
    password += y
    return password

def special(password):
    x = random.randint(0,6)
    special_characters = ['!','@','#','$','%','&','?']
    y = special_characters[x]
    password += y
    return password
main()