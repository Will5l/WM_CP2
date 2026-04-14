def movie_filter(): 

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
            with open('individual_projects/personal portfolio/docs/Movies list.csv', mode = 'r') as csv_file:
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
            with open('individual_projects/personal portfolio/docs/Movies list.csv', mode = 'r') as csv_file:
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


def finacial_calculator():
     # WM 1st Finacial Calculator
    #Greet them to the calculator
    print("Welcome to the finacial calculator")
    def interface():
        while True:
            choice = input("What would you like to do?\n1.Saving time calculator (how long it would take to save for something)\n2.Compound intrest calculator\n3.Budget allocator (takes catorgories and percents for a budget of money and distrubutes it)\n4.Sale price calculator (price of item on a given sale)\n5.Tip calculator\n6.Exit\n")
            if choice == '1':
                savTiCalc()
            elif choice == '2':
                comInCalc()
            elif choice == '3':
                budAllo()
            elif choice == '4':
                salePriceCalc()
            elif choice == '5':
                tipCalc()
            elif choice == '6':
                print("Goodbye")
                return
            else:
                print("Invalid choice choose again.")
                
    #Time saving function
    def savTiCalc():
        while True:
            print("Welcome to the savings time calculator\n")
            goal = input("What amount are you saving too?\n")
            if goal.isnumeric() == True:
                goal = float(goal)
                deposit = input("How much are saving each deposit?\n")
                if deposit.isnumeric() == True:
                    deposit = float(deposit)
                    time = input("How often are your deposits?\n1.Weekly\n2.Monthly\n")
                    if time == '1':
                        length = int(goal//deposit)
                        print(f"If you save ${deposit:.2f} weekly, it'll take {length} weeks to get ${goal:.2f}")
                        return
                    elif time == '2':
                        length = goal//deposit
                        print(f"If you save ${deposit:.2f} monthly, it'll take {length} months to get ${goal:.2f}")
                        return
                    else:
                        print("Invalid input")
                else:
                    print("Invalid input")
            else:
                print("Invalid input")


    #compound interest calculator
    def comInCalc():
        while True:
            print("Welcome to the compund interest calculator")
            start_amt = input("What is in the account to start with?\n")
            if start_amt.isnumeric() == True:
                start_amt = float(start_amt)
                intratperc = input("What is the intrest rate percent?\n")
                if intratperc.isnumeric() == True:
                    intratperc= float(intratperc)
                    years = input("Years spent compounding?\n")
                    if years.isnumeric() == True:
                        years = int(years)
                        for i in range(1,years+1):
                            start_amt = start_amt*(1+(intratperc/100))
                        final = start_amt
                        print(f"At the end of {years} years you will have ${final:.2f}")
                        return
                    else:
                        print("invalid")
                else:
                    print("invalid")    
            else:
                print("invalid")




    #This function will have an inner to take care of the budget allocation equation
    def budAllo():
        categories = {

        }
        print("Welcome to the budget allocater")
        while True:
            income = input("What is your monthly income?\n")
            if income.isnumeric() == True:
                income = int(income)
                amount = input("How many categories are you budgeting with?\n")
                if amount.isnumeric() == True:
                    amount = int(amount)
                    def allocateCalc():
                                    while True:
                                        for i in range(1,amount+1):
                                            holder = input("Category name: ")
                                            percent = input("Category percent: ")
                                            if percent.isnumeric() == True:
                                                percent = float(percent)/100
                                                categories[f'{holder}'] = percent
                                                thing = categories.values()
                                                y = False
                                                x = 0
                                        for z in thing:
                                                x += z
                                        if x == 1:
                                                y = True
                                        else:
                                                print("You gave more than 100 allocated")
                                        if y == True:
                                                for z in categories.keys():
                                                    categories[z] = round(income*categories[z], 2)
                                                return categories
                                        else:
                                                print("You allocated more than 100%")
                    categories = allocateCalc()
                    for i in categories.keys():
                        print(f"{i} is ${categories[i]}")
                    return
                else:
                    print("Invalid")
            else:
                print("Invalid")


    #sale price
    def salePriceCalc():
        while True:
            print("Welcome to the sales price calculator.\n")
            price = input("What is the item price?\n")
            if price.isnumeric() == True:
                price = round(float(price), 2)
                sale = input("What is the sale percent?\n")
                if sale.isnumeric() == True:
                    sale = int(sale)
                    if sale > 100:
                        print("You can't have a sale that big.")
                    else:
                        print(f"Your item is ${(price)-((price/100)*sale)}")
                        return
                else:
                    print("Invalid")
            else:
                print("Invalid")





    #Calculate tips
    def tipCalc():
        while True:
            print("Welcome to the tip calculator.\n")
            bill = input("What is the bill?\n")
            if bill.isnumeric() == True:
                percent = input("What is the tip percent?\n")
                if percent.isnumeric() == True:
                    bill, percent = float(bill), int(percent)
                    print(f"The tip would be ${(bill/100)*percent:.2}")
                    return
                else:
                    print("Invalid")
            else:
                print("Invalid")
    #ask them what function they would like to use (small description in parenthesis)
    interface()
    #Each function of the calculator will have its own code function.
    #With the budget allocator i'll have an inner function calculate the percents and return them. the larger function will obtain the number of categories and the names.
    #After it does the calculations it will ask if they want to do another or leave.
    #If they want to do another it will loop
    #if they don't it will exit.


def updated_personal_library():
     # WM 1st Personal Library

    import csv
    import sys
    #Create main function
    def interface():
        #greet them to the library
        print(f"Welcome to your personal library")
        books = list([])
        try:
            with open('individual_projects/personal portfolio/docs/library.csv', mode = 'r') as csv_file:
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
                    with open('individual_projects/personal portfolio/docs/library.csv', 'w', newline = '') as csv_file:
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
                    return
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


def password_rangen():
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
                return
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
            uppercase = uppercase.strip().lower()
            lowercase = lowercase.strip().lower()
            numbers = numbers.strip().lower()
            special_chars = special_chars.strip().lower()
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
                upper = False
                lower = False
                num = False
                special = False
                rng = random.randint(1,4)
                if rng == 1 and uppercase == "y":
                    upper = True
                    password,upper,lower,num,special = generator(password, upper,lower,num,special)
                if rng == 2 and lowercase == "y":
                    lower = True
                    password,upper,lower,num,special = generator(password, upper,lower,num,special)
                    num = True
                    password,upper,lower,num,special = generator(password, upper,lower,num,special)
                if rng == 4 and special_chars == "y":
                    special = True
                    password,upper,lower,num,special = generator(password, upper,lower,num,special)
                    #when the length is met, it is printed out and the password count is increased by 1.
            print(f"{password_count}.{password}")
            password_count += 1
                            
    #Each of the four functions will have a random variable to select an option from  the list, and then append the password, before returning it
    def generator(password, u, l, n, s):
        if u == True:
            x = random.randint(0,25)
            uppercase_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            y = uppercase_letters[x]
            password += y
            u, l, n, s = False,False,False,False
            return password, u, l, n, s
        elif l == True:
            x = random.randint(0,25)
            lowercase_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            y = lowercase_letters[x]
            password += y
            u, l, n, s = False,False,False,False
            return password, u, l, n, s
        elif n == True:
            x = random.randint(0,9)
            numbers = ['1','2','3','4','5','6','7','8','9','0']
            y = numbers[x]
            password += y
            u, l, n, s = False,False,False,False
            return password, u, l, n, s
        elif s == True:
            x = random.randint(0,6)
            special_characters = ['!','@','#','$','%','&','?']
            y = special_characters[x]
            password += y
            u, l, n, s = False,False,False,False
            return password, u, l, n, s
    main()