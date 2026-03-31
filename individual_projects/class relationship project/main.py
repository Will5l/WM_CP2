# WM 1st Class relationship project
from helper import *
import sys
char = None
def main():
    #Welcom user
    print("Welcome to Game Character Creator")
    my_game = Game()
    try:
            with open('individual_projects/class relationship project/char.csv', mode = 'r+') as csv_file:
                content = csv.reader(csv_file)
                headers = next(content)
                rows = []
                for line in content:
                    rows.append({headers[0]: line[0], headers[1]: line[1], headers[2]: line[2], headers[3]: line[3], headers[4]: line[4], headers[5]: line[5]})
    except:
            print("Can't find the file")
    else:
            for line in rows:
                fieldnames = ['name', 'char_class', 'health', 'attack', 'defense', 'lvl']
                my_game.add_to_list(line['name'],line['char_class'],line['health'],line['attack'],line['defense'],line['lvl'])
    while True:
        #Options
        choice = input("1.Create new character\n2.View character\n3.Level up character\n4.Battle characters\n5.View all characters\n6.Select character\n7.Exit\n")
        if choice == '1':
            try:
                char.update_data()
                char = char_create()
            except:
                char = char_create()
        elif choice == '2':
            try:
                char.view()
            except:
                print("No character selected, try again when you've selected one.")
        elif choice == '3':
            char.lvlup()
        elif choice == '4':
            my_game.print_list()
            my_game.battle()
        elif choice == '5':
            my_game.print_list()
        elif choice == '6':
            try:
                char.update_data()
                my_game.print_list()
                char = my_game.selection()
            except:
                my_game.print_list()
                char = my_game.selection()
        elif choice == '7':
            try:
                char.update_data()
                print("Goodbye")
            except:
                print("Goodbye")
            sys.exit()
main()