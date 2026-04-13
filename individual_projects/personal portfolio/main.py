# WM 1st Personal Portfolio
import tkinter as tk

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
    projecttext = "This project is a finacial calculator that can do various things, such as budgeting, calculate compound interest, tipping amount, and more. This project helped me:\nLearn to use functions effectivly\nSetup a main area where all the functions are called"

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
label = tk.Label(root, text='Programming Portfolio\n\nThis is a portfolio of the projects that I am most proud of.\n Click on one of the buttons below to learn about it, and then run it',font=("timesnewroman",12))
label.config(fg='White', background="Black")
label.pack()
p1btn = tk.Button(root, text="Project 1:\nFinacial calculator", command=project1).pack()
p2btn = tk.Button(root, text="Project 2:\n", command=project2).pack()
p3btn = tk.Button(root, text="Project 3:\n", command=project3).pack()
p4btn = tk.Button(root, text="Project 4:\n", command=project4).pack()
tk.StringVar(projecttext)
desc = tk.Label(root, text=projecttext).pack()
root.mainloop()