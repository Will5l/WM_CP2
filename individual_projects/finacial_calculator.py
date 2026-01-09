# WM 1st Finacial Calculator
import sys

#Greet them to the calculator
print("Welcome to the finacial calculator")
def interface():
    while True:
        choice = input("What would you like to do?\n1.Saving time calculator (how long it would take to save for something)\n2.Compound intrest calculator\n3.Budget allocator (takes catorgories and percents for a budget of money and distrubutes it)\n4.Sale price calculator (price of item on a given sale)\n5.Tip calculator\n6.Exit\n")
        if choice == '1':
            savTiCalc()
        elif choice == '2':
            savTiCalc()
        elif choice == '3':
            insertfuctionhere
        elif choice == '4':
            insertfuctionhere
        elif choice == '5':
            insertfuctionhere
        elif choice == '6':
            print("Goodbye")
            sys.exit()
        else:
            print("Invalid choice choose again.")
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
def comInCalc():
    print("Welcome to the compund intrest calculator")
    start_amt = input("What is in the account to start with?")
    if start_amt.isnumeric == True:
        start_amt = float(start_amt)
        intratperc = input("What is the intrest rate percent?")
        if intratperc.isnumeric == True:
            intratperc= float(intratperc)
            years = input("Years spent compounding?")
            if years.isnumeric == True:
                for i in range(1,years+1):
                    start_amt += start_amt*1+intratperc
                final = start_amt
                print(f"At the end of {years} years you will have ${final:.2f}")
                return
    else:
        print("invalid")
#ask them what function they would like to use (small description in parenthesis)
interface()
#Each function of the calculator will have its own code function.
#With the budget allocator i'll have an inner function calculate the percents and return them. the larger function will obtain the number of categories and the names.
#After it does the calculations it will ask if they want to do another or leave.
#If they want to do another it will loop
#if they don't it will exit.