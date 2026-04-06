# WM 1st GUI with Tkinter
import tkinter as tk
count = 0

root = tk.Tk()

root.title("Testing")
root.configure(background="orange")
root.minsize(250,250)
root.maxsize(1000,1000)
root.geometry("300x300+750+250")
label = tk.Label(root, text='This is currently working!',font=("timesnewroman",12))
label.config(fg='blue', background="orange")
#stuff about button
root.count = 0
def add():
    root.count+=1
    tk.Label(root, text=root.count).pack()

btn = tk.Button(root, text='ADD', command=add).pack()



label.pack()

root.mainloop()