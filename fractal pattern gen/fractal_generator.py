import turtle as t



def fractals(d,f,turn,t1,p1,p2,p3):
    t.speed(5)
    if d == 1:
        return
    else:
        t.forward(f/2)
        t.right(60)
        t.forward(f/2)
        t.right(120)
        t.forward(f/2)
        t.right(120)
        t.forward(f/2)
        t.right(60)
        t.forward(f/2)

        


        t.right(120)
        t.penup()
        t.goto(p2)
        t.pendown()

        t.forward(f/2)
        t.right(60)
        t.forward(f/2)
        t.right(120)
        t.forward(f/2)
        t.right(120)
        t.forward(f/2)
        t.right(60)
        t.forward(f/2)
        t.right(120)
        t.penup()
        t.goto(p3)
        t.pendown()


        t.forward(f/2)
        t.right(60)
        t.forward(f/2)
        t.right(120)
        t.forward(f/2)
        t.right(120)
        t.forward(f/2)
        t.right(60)
        t.forward(f/2)
        t.right(120)
        t.penup()
        t.goto(p1)
        t.pendown()


        return fractals(d-1,f/2,turn,t1,p1,p2,p3)
        pass




def generator(depth,color,bg):
    t.speed(5)
    
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
    #The turtle will always start in one place, and then got 1000, turn to make the triangles angle
    forward = 800
    turn = 120

    t.penup()
    t.goto(-400,-400)
    t.pendown()
    t.left(60)
    t.forward(forward)
    t.right(120)
    t.forward(forward)
    t.right(120)
    t.forward(forward)
    t.right(120)
    t.forward(forward/2)
    point1 = t.pos()
    t.right(60)
    t.forward(forward/2)
    point2 = t.pos()
    t.right(120)
    t.forward(forward/2)
    point3 = t.pos()
    t.right(120)
    t.forward(forward/2)
    t.right(60)
    
    fractals(depth,forward/2,turn,t,point1,point2,point3)
    t.done()
    pass