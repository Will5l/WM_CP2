# WM 1st Personal Portfolio
import tkinter as tk
from helper import finacial_calculator as fc
from helper import movie_filter as mf
from helper import updated_personal_library as upl
from helper import password_rangen as pr

# the four will be finacial calculator, movie filter, updated personal library, and password randomgen

def project1():
    global p1
    global p2
    global p3
    global p4
    global projecttext
    p1 = True
    p2 = False
    p3 = False
    p4 = False
    projecttext = "This project is a finacial calculator that can do various things, such as budgeting,\n calculate compound interest, tipping amount, and more.\nFrom this project I learned:\nLearn to use functions effectivly\nSetup a main area where all the functions are called\nHad to get a hang of use functions correctly."
    desc.tk.config(text=projecttext).pack()
def project2():
    global p1
    global p2
    global p3
    global p4
    global projecttext
    p1 = False
    p2 = True
    p3 = False
    p4 = False
    projecttext = "This project is a movie filter, that allows you to filter through a list of movies, or see all movies in the file.\n This also allows you to search by name of movie or the actors involed in it, and more.\nFrom this project I learned:\nHow to deal with csv files well\nHow to use if else statements more effectivly\nI had to understand how to print out things from a specific line of a csv"
    desc.tk.config(text=projecttext).pack()

def project3():
    global p1
    global p2
    global p3
    global p4
    global projecttext
    p1 = False
    p2 = False
    p3 = True
    p4 = False
    projecttext = "This project is a library, that can hold books, have them removed, or added, and saves between uses. It also allows you to search.\nFrom this project I learned:\nHow to update a csv file\nHow to search a csv file\nI had to figure out how to correctly save and delete things from a csv"
    desc.tk.config(text=projecttext).pack()

def project4():
    global p1
    global p2
    global p3
    global p4
    global projecttext
    p1 = False
    p2 = False
    p3 = False
    p4 = True
    projecttext = "This project is a random password generator. It asks you for length, and if you want numbers, capitals, and special characters.\nFrom this project I learned:\nHow to effectivly stupid proof\nHow to generate things.\nI had to figure out how to count the length and append it correctly."
    desc.tk.config(text=projecttext).pack()

def main():
    global root
    root = tk.Tk()
    p1 = False
    p2 = False
    p3 = False
    p4 = False
    projecttext = ''
    root.title("Will Malloch -- Programming Portfolio")
    root.configure(background="black")
    root.minsize(600,600)
    root.maxsize(600,600)
    root.geometry("300x300+550+250")
    label = tk.Label(root, text='Programming Portfolio\n\nThis is a portfolio of the projects that I am most proud of.\n Click on one of the buttons below to learn about it, and then run it with the run button',font=("timesnewroman",12))
    label.config(fg='White', background="Black")
    label.pack()
    p1btn = tk.Button(root, text="Project 1:\nFinacial calculator", command=project1).pack()
    p2btn = tk.Button(root, text="Project 2:\nMovie Filter", command=project2).pack()
    p3btn = tk.Button(root, text="Project 3:\nPersonal Library", command=project3).pack()
    p4btn = tk.Button(root, text="Project 4:\nRandom Password Generator", command=project4).pack()
    global desc
    desc = tk.Label(root, text=projecttext).pack()
    root.mainloop()
main()