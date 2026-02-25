import turtle as t

def generator(depth,color,bg):
    #Start the function by setting up the turtle so it can draw the shape.
    t.Screen
    try:
        t.color(color)
        t.bgcolor(bg)
    except:
        print("One of the inputed colors wasn't valid, so default colors were set")
        t.color("Black")
        t.bgcolor("White")
    t.penup()
    t.title("Fractal")
    t.hideturtle()
    #The turtle will always have 3 points that it goes to to begin with, that being -500 -500, 0 370, and 500 -500
    t.goto(-500,-500)
    t.pendown()
    t.goto(0,370)
    t.goto()


    t.done()
    pass
generator(1,'red','white')