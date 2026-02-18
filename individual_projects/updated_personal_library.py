# WM 1st Personal Library

import csv
import sys
#Create main function
def interface():
    #greet them to the library
    print(f"Welcome to your personal library")
    books = list([])
    try:
        with open('individual_projects/library.csv', mode = 'r') as csv_file:
            content = csv.reader(csv_file)
            headers = next(content)
            for line in content:
                books.append({headers[0]: line[0], headers[1]: line[1], headers[2]: line[2], headers[3]: line[3]},)
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
                with open('individual_projects/library.csv', 'w', newline = '') as csv_file:
                    fieldnames = ['Title', 'Author', 'Genre', 'Year']
                    reader = csv.reader(csv_file)
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    #writer.writeheader()
                    x = 0
                    writer.writerow({'Title': 'Title',
                                         'Author':'Author',
                                         'Genre': 'Genre',
                                         'Year': 'Year'})
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
    books = list(books)
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
    books.append({'Title':name,'Author':author,'Genre':genre,'Year':year})
    return books


#Make a function that asks them to type in the full name of the book and author they wish to remove, and have it print out all the books.
def removeBooks(books):
    x=0
    for book in books:
        print(f"Title:{books[x]['Title']}")
        print(f"Author:{books[x]['Author']}")
        print(f"Genre:{books[x]['Genre']}")
        print(f"Year:{books[x]['Year']}")
        x+=1
    choice = input("Type out the full name of the book you wish to remove. (Case sensitive)\n")
    x = 0
    for book in books:
        if choice in book['Title']:
            del books[x]
            return books
        x+=1
    print("No books matched")


#Create a function to search for books by the name given in the list.
def searchBooks(books):
    search = input("Type in the title of the book(case sensitive)\n")
    x = -1
    for book in books:
        x+=1
        if search in books[x]['Title']:
            print(f"Title:{books[x]['Title']}")
            print(f"Author:{books[x]['Author']}")
            print(f"Genre:{books[x]['Genre']}")
            print(f"Year:{books[x]['Year']}")
        else:
            print("No books matched your search")
            pass
    return


interface()