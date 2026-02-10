#WM 1st Movie Filter

import csv
import sys
#Use the code used for the notes to easily access the csv files
#make a main function that leads to all the other functions and exits


def main():
    print("Welcome to the movie filter. You can look at the whole list that we have, or filter it based on several categories.")
    while True:
        choice = input("What would you like to do?\n1.Display whole list\n2.Filter through movies\n3.Exit\n")
        if choice == '1':
            all_m_display()
        elif choice == '2':
            filter_movies()
        elif choice == '3':
            print("Goodbye")
            sys.exit()
#Have the function iterate through a list of all the movies, and have it look nice
def all_m_display():
    print("These are all the movies in the list")
    try:
        with open('individual_projects/Movies list.csv', mode = 'r') as csv_file:
            content = csv.reader(csv_file)
            headers = next(content)
            rows = []
            for line in content:
                rows.append({headers[0]: line[0], headers[1]: line[1], headers[2]: line[2], headers[3]: line[3], headers[4]: line[4], headers[5]: line[5]})

    except:
        print("Can't find the file")
    else:
        for line in rows:
            print(f"Title:{line['Title']}")
            print(f"Director:{line['Director']}")
            print(f"Genre:{line['Genre']}")
            print(f"Rating:{line['Rating']}")
            print(f"Length (min):{line['Length (min)']}")
            print(f"Actors:{line['Notable Actors']}\n")

#Have if else statments that check if the input is in the requested filter, and do it twice if they choose two. if it is length, ask for shorter or longer than a certain time and compare them. Then use the same code as in the last function to print them
def filter_movies():
    categories = {
        '1':"Title",
        '2':"Director",
        '3':"Genre",
        '4':"Rating",
        '5':"Length (min)",
        '6':"Actors"
    }
    try:
        with open('individual_projects/Movies list.csv', mode = 'r') as csv_file:
            content = csv.reader(csv_file)
            headers = next(content)
            rows = []
            for line in content:
                rows.append({headers[0]: line[0], headers[1]: line[1], headers[2]: line[2], headers[3]: line[3], headers[4]: line[4], headers[5]: line[5]})
    except:
        print("Can't find the file")
    else:
        while True:
            print("Choose the filters")
            amount = input("1 or 2 filters?\n")
            if amount == '1':
                filter_1 = input("Which category?\n1.Title\n2.Director\n3.Genre\n4.Rating\n5.Length\n6.Actors\n")
                if filter_1 in categories and filter_1 != '5':
                    search = input("Input your search\n")
                    for line in rows:
                        if search in line[categories[filter_1]]:
                            print(f"Title:{line['Title']}")
                            print(f"Director:{line['Director']}")
                            print(f"Genre:{line['Genre']}")
                            print(f"Rating:{line['Rating']}")
                            print(f"Length (min):{line['Length (min)']}")
                            print(f"Actors:{line['Notable Actors']}\n")
                    choice = input("Would you like to search with filters again?y/n\n")
                    choice = choice.strip().lower()
                    if choice == "y":
                        continue
                    else:
                        return
                elif filter_1 == "5":
                    x = input("1.Longer than\n2.Shorter than\n")
                    while True:
                            length = input("Time in minutes: ")
                            if length.isnumeric() == True:
                                length = int(length)
                                break
                            else:
                                print("only use numbers")
                    for line in rows:
                        if x == '1':
                            if length < int(line[categories['5']]):
                                print(f"Title:{line['Title']}")
                                print(f"Director:{line['Director']}")
                                print(f"Genre:{line['Genre']}")
                                print(f"Rating:{line['Rating']}")
                                print(f"Length (min):{line['Length (min)']}")
                                print(f"Actors:{line['Notable Actors']}\n")
                        elif x == '2':
                            if length > int(line[categories['5']]):
                                print(f"Title:{line['Title']}")
                                print(f"Director:{line['Director']}")
                                print(f"Genre:{line['Genre']}")
                                print(f"Rating:{line['Rating']}")
                                print(f"Length (min):{line['Length (min)']}")
                                print(f"Actors:{line['Notable Actors']}\n")
                    choice = input("Would you like to search with filters again?y/n\n")
                    choice = choice.strip().lower()
                    if choice == "y":
                        continue
                    else:
                        return
                else:
                    print("Invalid")

            elif amount == '2':
                filter_1 = input("Which category?\n1.Title\n2.Director\n3.Genre\n4.Rating\n5.Length\n6.Actors\n")
                filter_2 = input("Which category?\n1.Title\n2.Director\n3.Genre\n4.Rating\n5.Length\n6.Actors\n")
                if filter_1 in categories and filter_2 in categories and filter_1 != '5' and filter_2 != '5':
                    search1 = input("Input your first search\n")
                    search2 = input("Input your second search\n")
                    for line in rows:
                        if search1 in line[categories[filter_1]] and search2 in line[categories[filter_2]]:
                            print(f"Title:{line['Title']}")
                            print(f"Director:{line['Director']}")
                            print(f"Genre:{line['Genre']}")
                            print(f"Rating:{line['Rating']}")
                            print(f"Length (min):{line['Length (min)']}")
                            print(f"Actors:{line['Notable Actors']}\n")
                    choice = input("Would you like to search with filters again?y/n\n")
                    choice = choice.strip().lower()
                    if choice == "y":
                        continue
                    else:
                        return
                elif filter_1 == "5" and filter_2 in categories and filter_2 != '5':
                    x = input("1.Longer than\n2.Shorter than\n")
                    while True:
                            length = input("Time in minutes: ")
                            if length.isnumeric() == True:
                                length = int(length)
                                break
                            else:
                                print("only use numbers")
                    y = input("Type the other search\n")
                    for line in rows:
                        if x == '1':
                            if length < int(line[categories['5']]) and y in line[categories[filter_2]]:
                                print(f"Title:{line['Title']}")
                                print(f"Director:{line['Director']}")
                                print(f"Genre:{line['Genre']}")
                                print(f"Rating:{line['Rating']}")
                                print(f"Length (min):{line['Length (min)']}")
                                print(f"Actors:{line['Notable Actors']}\n")
                        elif x == '2':
                            if length > int(line[categories['5']]) and y in line[categories[filter_2]]:
                                print(f"Title:{line['Title']}")
                                print(f"Director:{line['Director']}")
                                print(f"Genre:{line['Genre']}")
                                print(f"Rating:{line['Rating']}")
                                print(f"Length (min):{line['Length (min)']}")
                                print(f"Actors:{line['Notable Actors']}\n")
                    choice = input("Would you like to search with filters again?y/n\n")
                    choice = choice.strip().lower()
                    if choice == "y":
                        continue
                    else:
                        return
                elif filter_2 == '5' and filter_1 in categories and filter_1 != '5':
                    x = input("1.Longer than\n2.Shorter than\n")
                    while True:
                            length = input("Time in minutes: ")
                            if length.isnumeric() == True:
                                length = int(length)
                                break
                            else:
                                print("only use numbers")
                    y = input("Type the other search\n")
                    for line in rows:
                        if x == '1':
                            if length < int(line[categories['5']]) and y in line[categories[filter_1]]:
                                print(f"Title:{line['Title']}")
                                print(f"Director:{line['Director']}")
                                print(f"Genre:{line['Genre']}")
                                print(f"Rating:{line['Rating']}")
                                print(f"Length (min):{line['Length (min)']}")
                                print(f"Actors:{line['Notable Actors']}\n")
                        elif x == '2':
                            if length > int(line[categories['5']]) and y in line[categories[filter_1]]:
                                print(f"Title:{line['Title']}")
                                print(f"Director:{line['Director']}")
                                print(f"Genre:{line['Genre']}")
                                print(f"Rating:{line['Rating']}")
                                print(f"Length (min):{line['Length (min)']}")
                                print(f"Actors:{line['Notable Actors']}\n")
                    choice = input("Would you like to search with filters again?y/n\n")
                    choice = choice.strip().lower()
                    if choice == "y":
                        continue
                    else:
                        return
                else:
                    print("Invalid")

main()