# WM Pet Simulator
import sys
from helpers import *
# main will greet them, and then give them all the options. none of them will work until they select a pet to be their main one, or create one if they have none
def main():
    time = 8
    print("Welcome user, this program will simulate pets. You will have to take care of them and keep an eye on their stats. If the pet's stats go to zero, then its health will decay with each action not fixing it, and if health reaches 0 it dies")
    while True:
        pet = None
        while pet == None:
            y = 0
            choice = input("You currently don't have a pet equipped, you can:\n1.Create a pet\n2.Select already made pet\n")
            choice = choice.strip()
            if choice == '1':
                pet = create_pet()

            elif choice == '2':
                pet = select_pet()

            else:
                print("Invalid input, please try again")
        while pet != None:
            if time > 24:
                time = 0
                y+=1
                if y>=5:
                    pet.age_up()
                    print(f"{pet.name} grew a year older")
                
            pet.display()
            choice = input(f"Time. {time}:00\n1. Feed pet\n2. Play with pet\n3. Put pet to sleep\n4. Take to vet\n5. Manage pets\n6. Quit\n")
            if choice == '1':
                while True:
                    type = input("What type of food?\n1.Basic\n2.Treat\n3.Hearty meal\n")
                    if choice == '1':
                        food = (20,10)
                        break
                    elif choice == '2':
                        food = (10,30)
                        break
                    elif choice == '3':
                        food = (50,20)
                        break
                    else:
                        print("Invalid choice, try again")
                pet.feed(food[0], food[1])
                print(f"You fed {pet.name}, hunger+{food[0]} happiness+{food[1]}")
                pet.decay()
                time += 1
            elif choice == '2':
                pet.play()
                print(f"You played with {pet.name}")
                pet.decay()
                time += 1
                pass
            elif choice == '3':
                pet.sleep()
                print(f"You put {pet.name} to sleep")
                pet.decay()
                time+=6
                pass
            elif choice == '4':
                pet.vet()
                print(f"You took {pet.name} to the vet")
                pet.decay
                time+=2
                pass
            elif choice == '5':
                while True:
                    choice = input("1.Change pet\n2.Create new pet\n3.Release current pet\n4.Cancel\n")
                    if choice == '1':
                        remove_pet(pet)
                        save_pet_data(pet)
                        pet = select_pet()
                        break
                    elif choice == '2':
                        remove_pet(pet)
                        save_pet_data(pet)
                        pet = create_pet()
                        break
                    elif choice == '3':
                        remove_pet(pet)
                        pet = None
                        break
                    elif choice == '4':
                        break
                    else:
                        print("Invalid")
            elif choice == '6':
                print("Goodbye")
                remove_pet(pet)
                save_pet_data(pet)
                sys.exit()
            else:
                print("Invalid input")
main()