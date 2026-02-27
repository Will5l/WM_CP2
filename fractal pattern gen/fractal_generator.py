import turtle as t



def fractals(d,f,turn,t1,t2,t3):
    t.speed("fast")
    if d == 1:
        return
    else:
        #Have the turtle move forward a decreasing amount so it can make the triangles at the right distance
        #Turtle one
        t1.forward(f)
        t1.right(60)
        t1.forward(f)
        t1.right(turn)
        t1.forward(f)
        t1.right(turn)
        t1.forward(f)
        t1.right(60)
        
        #Turtle two
        t2.forward(f)
        t2.right(60)
        t2.forward(f)
        t2.right(turn)
        t2.forward(f)
        t2.right(turn)
        t2.forward(f)
        t2.right(60)

        #Turtle three
        t3.forward(f)
        t3.right(60)
        t3.forward(f)
        t3.right(turn)
        t3.forward(f)
        t3.right(turn)
        t3.forward(f)
        t3.right(60)
        return fractals(d-1,f/2,turn,t1,t2,t3)
        pass




def generator(depth,color,bg):
    t.speed("fast")
    t1 = t.Turtle()
    t2 = t.Turtle()
    t3 = t.Turtle()

    t1.speed("fast")
    t2.speed("fast")
    t3.speed("fast")

    #Start the function by setting up the turtle so it can draw the shape.
    t.Screen
    try:
        t.color(color)
        t.bgcolor(bg)
        t1.color(color)
        t2.color(color)
        t3.color(color)
    except:
        print("One of the inputed colors wasn't valid, so default colors were set")
        t.color("Black")
        t1.color("Black")
        t2.color("Black")
        t3.color("Black")
        t.bgcolor("White")

    t.penup()
    t.title("Fractal")
    t.hideturtle()
    #The turtle will always start in one place, and then got 1000, turn to make the triangles angle, but there will be three, who will all do the same thing, so that they can do it with less looping
    forward = 800
    turn = 120
    #Turtle one movement
    #t1.hideturtle()
    #t2.hideturtle()
    #t3.hideturtle()

    t1.penup()
    t1.goto(-400,-400)
    t1.pendown()
    t1.left(60)
    t1.forward(forward)

    #Turtle two movement
    t2.penup()
    t2.goto(t1.position())
    t2.pendown()
    t2.right(60)
    t2.forward(forward)
    
    #Turtle three movement
    t3.penup()
    t3.goto(t2.pos())
    t3.pendown()
    t3.right(180)
    t3.forward(forward)
    t3.right(turn)
    t2.right(turn)
    t1.right(turn)
    fractals(depth,forward/2,turn,t1,t2,t3)
    t.done()
    pass
generator(5,'red','white')