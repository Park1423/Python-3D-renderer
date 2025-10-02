##
# Code by Parker Jolly
# On 9/30/2025-10/1/2025
# Program name: Cube renderer
# Notes: This is only a prototype and still VERY buggy. For example, there is no proper render
# order and things can render in the wrong order. Things moved behind the camera also completely break
# I will probably continue working on this. I do not want help; I want to do this all on my own so that
# I can say that I did it.
##

#Import turtle and create turtle
import turtle
cursor = turtle.Turtle()
screen = turtle.Screen()
screen.tracer(0,0)
cursor.color("black","cyan")
cursor.speed(0)
cursor.hideturtle()
FocaL_Length = 400

#Create cube model
triangle1 = [[0,-50,70.71],[0,50,70.71],[-70.71,50,0]]
triangle2 = [[0,-50,70.71],[-70.71,50,00],[-70.71,-50,0]]

triangle3 = [[0,-50,70.71],[0,50,70.71],[70.71,-50,0]]
triangle4 = [[70.71,-50,0],[0,50,70.71],[70.71,50,0]]

triangle5 = [[0,-50,70.71],[70.71,-50,0],[-70.71,-50,0]]
triangle6 = [[0,-50,-70.71],[-70.71,-50,0],[70.71,-50,0]]

triangle7 = [[0,50,-70.71],[-70.71,50,0],[0,50,70.71]]
triangle8 = [[0,50,-70.71],[70.71,50,0],[0,50,70.71]]

triangle9 = [[0,50,-70.71],[-70.71,-50,0],[-70.71,50,0]]
triangle10 = [[0,50,-70.71],[0,-50,-70.71],[-70.71,-50,0]]

triangle11 = [[0,-50,-70.71],[0,50,-70.71],[70.71,50,0]]
triangle12 = [[70.71,50,0],[0,-50,-70.71],[70.71,-50,0]]

shape1geometry = [triangle1,triangle2,triangle3,triangle4,triangle5,triangle6,triangle7,triangle8,triangle9,triangle10,triangle11,triangle12]
shape1pos = [0,10,150]

#render
while True:
    cursor.clear()

    for face in shape1geometry:
        cursor.pu()

        cursor.goto( ((FocaL_Length/(face[2][2]+shape1pos[2]))*(face[2][0]+shape1pos[0])), ((FocaL_Length/(face[2][2]+shape1pos[2]))*(face[2][1]+shape1pos[1])) )

        cursor.begin_fill()
        cursor.pd()

        for point in face:
            globalx = point[0] + shape1pos[0]
            globaly = point[1] + shape1pos[1]
            distance = FocaL_Length/(point[2] + shape1pos[2])

            cursor.goto(
            (distance*globalx),
            (distance*globaly)
            )
            #cursor.dot(10,"red")   #uncomment this to see the points of the cube

        cursor.end_fill()
        cursor.pu()


    screen.update()

   
    shape1pos[0] -= 0.1     #THIS IS WHAT YOU CHANGE TO MOVE THE CUBE shape1pos[0] is left and right, [1] is up and down, and [3] is forward and backward
    print(shape1pos)
    #This code has been commented out to have gradual movement, but you can uncomment it if you want. just make sure you comment the "shape1pos[0] += 0.1" line out
    # shape1pos = input("The cube is at " + str(shape1pos) + ". Input new coordinates or enter stop to end the program: ")
    # if shape1pos == "stop":
    #     break
    # else:
    #     shape1pos = shape1pos.split(",")
    #     shape1pos[0] = int(shape1pos[0])
    #     shape1pos[1] = int(shape1pos[1])
    #     shape1pos[2] = int(shape1pos[2])
    #     cursor.clear()
