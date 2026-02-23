import time_checking_word_counter*
import file_updater
import sys
#Have a main funtion that calls all the other dependancies and things
def main():
    print("Welcome to the word counter. You can write and save to a document here, and update the word count, as well as the time it was updated.")
    # Have the file name be a variable that can be changed, but has a default if it doesn't get changed
    while True:
        choice = input("What would you like to do?\n1. Edit the file\n2. Change the file location(if this isn't updated, then it won't work)\n3. Word count and last updated\n4. Exit\n")
        if choice == '1':
            insertfuctionhere
        elif choice == '2':
            file_name = input("Insert the path for the text file: ")
        elif choice == '3':
            word_count, = word_time_checker(file_name)
        elif choice == '4':
            print("Program exiting")
            sys.exit()
        else:
            print("Your choice was not valid, try again.")