import tkinter as tk

def leftKey(event):
    print("Left key pressed")
def rightKey(event):
    print("Right key pressed")
def upKey(event):
    print("Up key pressed")
def downKey(event):
    print("Down key pressed")
# Define functions for other arrow keys similarly

root = tk.Tk()
frame = tk.Frame(root, width=10, height=10)
frame.pack()
frame.focus_set() # set focus to the frame to capture key events

# Bind arrow keys to functions
frame.bind('<Left>', leftKey)
frame.bind('<Right>', rightKey)
frame.bind('<Up>', upKey)
frame.bind('<Down>', downKey)

# Bind '<Right>', '<Up>', and '<Down>' to their respective functions

root.mainloop()