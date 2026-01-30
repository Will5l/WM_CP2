# WM 1st Morse Code translator

import sys


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


def morToEng(e,m):
    morse = input("Input the morse code you have, for dots use periods, for dashes use hyphens (-) for spaces just use spaces. Make sure every letter has a space after\n")
    for x in morse:
        y = ''
        y = y+x
        if y in m:
            
            letter = 
            word = ""
            word = word+letter
    print(word)

    pass

def engToMor(e,m):
    pass
main()