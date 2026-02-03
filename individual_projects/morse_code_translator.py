# WM 1st Morse Code translator

import sys

#Main function to run the interface
def main():
    while True:
        english = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        morse = ['.- ','-... ','-.-. ','-.. ','. ','..-. ','--. ','.... ','.. ','.--- ','-.- ','.-.. ','-- ','-. ','--- ','.--. ','--.- ','.-. ','... ','- ','..-','...-','.--','-..-','-.--','--..']
        print("Welcome to the Morse code translator")
        choice = input("Would you like to \n1.Translate Morse code to English\n2.Translate English to Morse code\n3.Exit\n")
        if choice == '1':
            morToEng(english,morse)
        elif choice == '2':
            engToMor(english,morse)
        elif choice == '3':
            print("Goodbye")
            sys.exit()

#Function that takes in . and - as morse code and translates it to english
def morToEng(e,m):
    prnt = False
    while prnt == False:
        prnt = True
        morse = input("Input the morse code you have, for dots use periods, for dashes use hyphens (-) for spaces just use spaces(do not include the letter spaces as actual spaces). Make sure every letter has a space after\n")
        word = ""
        y = ''
        for x in morse:
            y = y+x
            if y == ' ':
                word = word+' '
                y = ''
                continue
            elif y in m:
                z = m.index(y)
                letter = e[z]
                word = word+letter
                y = ''
                continue
            elif x != ' ' and x != '-' and x != '.':
                print("Something was invalid, try again")
                prnt = False
                break
        print(word)

    pass
#Function that takes in english and turns it into the corresponding . and - combo for morse code.
def engToMor(e,m):
        prnt = False
        while prnt == False:
            prnt = True
            words = input("Type what you would like to translate to morse code (use all caps)\n")
            morse = ''
            for x in words:
                if x == " ":
                    morse = morse+" "
                elif x in e:
                    y = e.index(x)
                    morse = morse+m[y]
                else:
                    print("Something was invalid, try again")
                    prnt = False
                    break
                
        print(morse)
main()