from time_checking_word_counter import *
from file_updater import *
import sys
#Have a main funtion that calls all the other dependancies and things
def main():
    print("Welcome to the word counter. You can write and save to a document here, and update the word count, as well as the time it was updated.")
    file_name_made = False
    # Have the file name be a variable that can be changed, but has a default if it doesn't get changed
    while True:
        choice = input("What would you like to do?\n1. Edit the file/view it\n2. Change the file location(if this isn't updated, then it won't work)\n3. update word count\n4. Exit\n")
        if choice == '1':
            #Have the different choices call functions from other files.
            if file_name_made == True:
                choice = input("1.View\n2.Edit\n")
                if choice == '1':
                    view_file(file_name)
                elif choice == '2':
                    edit_file(file_name)
                else:
                    print("Invalid choice")
            else:
                print("You can't edit a file if you haven't given one.")
        elif choice == '2':
            #Let them set the file as a variable so they can edit whatever text file they want
            file_name = input("Insert the path for the text file: ")
            file_name_made = True
        elif choice == '3':
            if file_name_made == True:
                word_count,last_update_time = word_time_checker(file_name)
            else:
                print("You didn't add a file, so you can't update the word count or date.")
        elif choice == '4':
            print("Program exiting")
            sys.exit()
        else:
            print("Your choice was not valid, try again.")
main()