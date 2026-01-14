# WM 1st types of lists notes

list = ["thing1", "thing2", "cat"]


fruit = ("apple", "orange", "peach", "kiwi", "raspberry")
home = (0,0)
x,y = home

#fruit[3] = "pineapple" - Doesn't work, tuples can't be changed
print(x)



#set
colors = {"Orange", "Purple", "Green", "Blue", "Yellow", "Red", "Green", "Purple"}
colors.add("Pink")
colors.remove("Purple")
for i in colors:
    if i == "Orange":
        i = "Burgendy"
    print(i)




print(colors)