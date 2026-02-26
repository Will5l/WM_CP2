import turtle as t



def fractals(d,fpo,spo,thpo,ft,fp,sp,thp,fps,sps,thps):
    t.speed("fast")
    if d == 1:
        return
    if ft == True:
        fp[0] = (fpo[0]+spo[0])/2
        fp[1] = (fpo[1]+spo[1])/2
        sp[0] = (spo[0]+thpo[0])/2
        sp[1] = (spo[1]+thpo[1])/2
        thp[0] = (thpo[0]+fpo[0])/2
        thp[1] = (thpo[1]+fpo[1])/2
        t.penup()
        t.goto(fp)
        t.pendown()
        t.goto(sp)
        t.goto(thp)
        t.goto(fp)
        ft = False
        return fractals(d-1,fpo,spo,thpo,ft,fp,sp,thp,fps,sps,thps)
    else:
        t.penup()
        thps[0] = (fpo[0]+thp[0])/2
        thps[1] = (fpo[1]+thp[1])/2
        fps[0] = (fp[0]+fpo[0])/2
        fps[1] = (fp[1]+fpo[1])/2
        sps[0] = (sp[0]+fpo[0])/2
        sps[1] = (sp[1]+fpo[1])/2
        t.goto(fps)
        t.pendown()
        t.goto(sps)
        t.goto(thps)
        t.goto(fps)
        t.penup()
        thps[0] = (spo[0]+fp[0])/2
        thps[1] = (spo[1]+fp[1])/2
        fps[0] = (spo[0]+sp[0])/2
        fps[1] = (spo[1]+sp[1])/2
        sps[0] = (sp[0]+fp[0])/2
        sps[1] = (sp[1]+fp[1])/2
        t.goto(thps)
        t.pendown()
        t.goto(fps)
        t.goto(sps)
        t.goto(thps)
        return fractals(d-1,fpo,spo,thpo,ft,fps,sps,thps,fp,sp,thp)
        pass




def generator(depth,color,bg):
    t.speed("fast")
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
    first_point = [-500,-500]
    second_point = [0,370]
    third_point = [500,-500]
    #Use a series of cordinate points to create the triangles
    fp = [0,0]
    sp = [0,0]
    thp = [0,0]
    fps = [0,0]
    sps = [0,0]
    thps = [0,0]
    t.goto(first_point)
    t.pendown()
    t.goto(second_point)
    t.goto(third_point)
    t.goto(first_point)
    first_try = True
    fractals(depth,first_point,second_point,third_point,first_try,fp,sp,thp,fps,sps,thps)

    t.done()
    pass
generator(4,'red','white')