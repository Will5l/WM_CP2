# WM 1st Personal Library

import csv
import sys
#Create main function
def interface():
    #greet them to the library
    print(f"Welcome to your personal library")
    books = []
    try:
        thing="individual_projects/library.csv"
        with open(thing, mode = 'r') as csv_file:
            content = csv.reader(csv_file)
            headers = next(content)
            for line in content:
                books.append({headers[0]: line[0], headers[1]: line[1], headers[2]: line[2], headers[3]: line[3]})
    except:
        print("Can't find the file")
    else:
        
        while True:
            #Ask them what what they would like to do
            print(f"What would you like to do?\n")
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
                with open('individual_projects/library.csv', 'r+', newline = '') as csv_file:
                    fieldnames = ['Title', 'Author', 'Genre', 'Year']
                    reader = csv.reader(csv_file)
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    #writer.writeheader()
                    x = 0
                    while x < len(books):
                        writer.writerow({'Title': books[x]['Title'],
                                         'Author': books[x]['Author'],
                                         'Genre': books[x]['Genre'],
                                         'Year': books[x]['Year']})
                        x+=1
                print(f"Goodbye")
                sys.exit()
                pass
            else:
                print("Invalid")

#Have a for loop iterate through every book and author, and print them out nicely
def viewBooks(books):
    x = 0
    for book in books:
        print(f"Title:{books[x]['Title']}")
        print(f"Author:{books[x]['Author']}")
        print(f"Genre:{books[x]['Genre']}")
        print(f"Year:{books[x]['Year']}")
        x+=1


#Make a function that asks for the name and author of the book, before concatenating them and adding them to the set
def addBooks(books):
    name = input("What is the name of the book?\n")
    author = input("Who is the author?\n")
    genre = input("Whats the genre?\n")
    year = input("What year was it released?\n")
    books.append({name,author,genre,year})
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