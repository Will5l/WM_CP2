# WM 1st Personal Library

import sys

#Create main function
def interface():
    #Ask for users name and greet them to the library
    user = input("What is your name?\n")
    print(f"Welcome to your personal library, {user}")
    books = {"Fablehaven by Brandon Mull", "The Hunger Games by Suzzane Collins"}
    while True:
        #Ask them what what they would like to do
        print(f"What would you like to do, {user}?\n")
        choice = input("1.View\n2.Add\n3.Remove\n4.Search\n5.Exit\n")
        #Have if else statments check the choice and call the respective function, or exit
        if choice == '1':
            viewBooks(books)
            pass
        elif choice == '2':
            books = addBooks(books)
            pass
        elif choice == '3':
            books = removeBooks(books)
            pass
        elif choice == '4':
            searchBooks(books)
            pass
        elif choice == '5':
            print(f"Goodbye, {user}")
            sys.exit()
            pass
        else:
            print("Invalid")

#Have a for loop iterate through every book and author, and print them out nicely
def viewBooks(books):
    for i in books:
        print(f"{i}\n")
    if books == False:
        print("You have no books")


#Make a function that asks for the name and author of the book, before concatenating them and adding them to the set
def addBooks(books):
    print(f"What book would you like to add?")
    name = input("What is the name of the book?\n")
    author = input("Who is the author?\n")
    full_thing = (f"{name} by {author}")
    books.add(full_thing)
    return books


#Make a function that asks them to type in the full name of the book and author they wish to remove, and have it print out all the books.
def removeBooks(books):
    while True:
        again = False
        for i in books:
            print(f"{i}\n")
        choice = input("Type out the full name and author of the book you wish to remove. (Case sensitive)\n")
        if choice in books:
            books.remove(choice)
            return books
        else:
            #if something goes wrong have it ask if they want to try again or go back to the menu
            while again == False:
                again = input("something went wrong, would you like to try again, or go back to the menu?y/n\n")
                if again == "y":
                    again = True
                    continue
                elif again == "n":
                    again = False
                    return books
                else:
                    print("Invalid choice")


#Create a function to search for books by the name given in the list.
def searchBooks(books):
    search = input("Type in the title/author of the book\n")
    for i in books:
        if search in i:
            print(i)
        else:
            pass
    return


interface()