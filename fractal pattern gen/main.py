import turtle
import fractal_generator as f
import sys
# Main function that acts as the UI and access to the other things

def main():
    while True:
        print("Welcome to the Sierpinski Triangle Generator.")
        depth_list = ['1','2','3','4','5']
        #ask them them how many times they want it to repeat, and use a list to see if they chose an option that was available
        depth = input("How many times would you like the fractal to repeat? 1-5\n")
        if depth in depth_list:
            depth = int(depth)
            #Ask them what color they want it to be
            color = input("What color would you like it to be? (purple, blue, green ect.)\n")
            bgcolor = input("What color do you want the background?\n")
            #After getting all the things, call the function and give it the variables that were just gotten
            f.generator(depth,color,bgcolor)
            sys.exit()
        else:
            print("Invalid")
main()