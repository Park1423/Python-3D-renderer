import random
import turtle
import time
import keyboard

def point_to_screen(pointpos,objectpos):
    distance = Focal_Length / (pointpos[2] + objectpos[2] - camerapos[2])   #Focal_Length / zpos works when nothing is moving, but here we have the point, camera, and objects positions in play
    localx = pointpos[0] + objectpos[0] - camerapos[0]   #same here. we only need the x or y of the point normally but we have other things in play   
    localy = pointpos[1] + objectpos[1] - camerapos[1]
    return (distance * localx),(distance * localy)  # Final math. We could have done this all on one line, but I used local variables for readability.


c = turtle.Turtle()
s = turtle.Screen()
s.tracer(0,0)
c.speed(0)
c.color("black","cyan")
c.hideturtle()
num_of_triangles = 1
shapepos = [0,0,100]
Focal_Length = 300
camerapos = [0,0,-0.1]
thing = 0
last_time = time.perf_counter()
deltatotal = 0
fpstotal = 0

while True:
    while thing < 4:
        current_time = time.perf_counter() #Do delta/fps stuff
        delta = current_time - last_time
        last_time = current_time
        deltatotal += delta
        fpstotal += 1
        if deltatotal >= 1:
            print(fpstotal)
            fpstotal = 0
            deltatotal = 0

        c.clear()
        c.pu()
        c.goto(-300,300)
        c.write(str(round(1/delta,2)))
        
        for i in range(num_of_triangles):
            

            pos1 = [100,100,100]
            pos2 = [-100,100,100]
            pos3 = [100,-100,100]

            tri = [pos1,pos2,pos3]
            c.pu()
            #c.color("black",("#"+ str(random.randint(100000,999999))))
            c.goto(point_to_screen(pos3,shapepos))
            c.begin_fill()
            c.pd()

            for pos in tri:
                
                c.goto(point_to_screen(pos,shapepos))
            c.end_fill()
        #thing += 1
        s.update()

        if keyboard.is_pressed("w"):
            num_of_triangles = int(input("Enter number of triangles to render: "))


    #num_of_triangles = int(input("Enter number of triangles to render: "))
    thing = 0

