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
            print(f"Actors:{line['Notable Actors']}")

#Have if else statments that check if the input is in the requested filter, and do it twice if they choose two. if it is length, ask for shorter or longer than a certain time and compare them. Then use the same code as in the last function to print them
def filter_movies():
    pass


main()