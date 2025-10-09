import main
import random
import turtle
import time

c = turtle.Turtle()
s = turtle.Screen()
c.hideturtle()
num_of_triangles = 1
shapepos = [0,0,0]
Focal_Length = 300
camerapos = [0,0,0]

while True:

    for i in range(num_of_triangles):

        pos1 = [random.randint(-1000,1000),random.randint(-1000,1000),random.randint(-1000,1000)]
        pos2 = [random.randint(-1000,1000),random.randint(-1000,1000),random.randint(-1000,1000)]
        pos3 = [random.randint(-1000,1000),random.randint(-1000,1000),random.randint(-1000,1000)]

        tri = [pos1,pos2,pos3]
        c.pu()
        c.begin_fill()
        c.goto(main.point_to_screen(pos3,shapepos))
        c.pd()

        for pos in tri:
            
            main.point_to_screen(pos,shapepos)


