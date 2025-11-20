##
# Code by Parker Jolly
# On 9/30/2025-10/9/2025
# Program name: Cube renderer
# Notes: This is only a prototype and still VERY buggy. For example, there is no proper render
# order and things can render in the wrong order. Things moved behind the camera also completely break.
# You cant turn around. It's rendered off of the cpu meaning about 16 cubes has ym gaming pc begging for 
# mercy. I will probably continue working on this.
##

#Imports
import turtle
import keyboard
import time
import random

# Create Turtle and screen objects
cursor = turtle.Turtle()
screen = turtle.Screen()

# Change colors
turtle.bgcolor("#81DDFF")
cursor.color("black","#474947")

# Increase speed and disable animations
cursor.speed(0)
screen.tracer(0,0)

# Hide the turtle
cursor.hideturtle()

# Focal length and camera starting position
Focal_Length = 500
camerapos = [0,120,0]

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

cubegeometry = [triangle1,triangle2,triangle3,triangle4,triangle5,triangle6,triangle7,triangle8,triangle9,triangle10,triangle11,triangle12]

# Add shapes to the scene with cube geometry and positions. positions are [x, y, z]
shapes = [
        [cubegeometry,[0,10,150]],
        [cubegeometry,[-200,10,200]],
        ]

# Main
def main():
    # Initilize here to avoid local variable error or something
    current_time = time.perf_counter()
    last_time = time.perf_counter()
    delta = current_time - last_time

    # More Initilization. These are for the FPS counter
    deltaaccumulator = 0
    fpsacculumator = 0
    fps = 0

    while True:
        current_time = time.perf_counter() # Calculate delta stuff
        delta = current_time - last_time
        last_time = current_time
        

        if keyboard.is_pressed("w"):    # Get input and move the camera.
            camerapos[2] += 400 * delta
        elif keyboard.is_pressed("s"):
            camerapos[2] -= 400 * delta
        
        if keyboard.is_pressed("a"):
            camerapos[0] -= 400 * delta
        elif keyboard.is_pressed("d"):
            camerapos[0] += 400 * delta

        if keyboard.is_pressed("space"):
            camerapos[1] += 800 * delta
        elif keyboard.is_pressed("shift"):
            camerapos[1] -= 400 * delta
        
        if camerapos[1] > 120 and not keyboard.is_pressed("space"): # Half simulate gravity
            camerapos[1] -= 500 * delta

        cursor.clear() # Clear the screen so we can put something new on it
        
        deltaaccumulator += delta # FPS calculations
        fpsacculumator += 1
        if deltaaccumulator >= 1:
            fps = fpsacculumator
            fpsacculumator = 0
            deltaaccumulator = 0

        cursor.pu()
        cursor.goto(-300,300)
        cursor.write(f"FPS: {str(round(fps))}") # Display FPS
            
        
        for shape in shapes: # For each shape
            for face in shape[0]: # For each triangle in face
                # Get ready to draw
                cursor.pu()
                cursor.color("black",("#8D1E1E"))
                cursor.goto(point_to_screen(face[2],shape[1])) #Go to the last point to ensure we fill the shape properly

                cursor.begin_fill() # Start filling the triangle
                cursor.pd()

                for point in face: # For each Vertex in the tringle
                    
                    cursor.goto(point_to_screen(point,shape[1]))   # Go to each point of each face and connect the dots.
                    #cursor.dot(10,"pink")   # Uncomment this to see the points of the cube. WARNING! For some reason this practically DOUBLES lag.
                    
                cursor.end_fill() # finish fill
                cursor.pu()

        screen.update() # Force a screen update

def point_to_screen(pointpos,objectpos): # This function takes a list with 3 variables, x, y, and z, and its original shapes position, and turns it into 2d coordinates to put on the screen.
    distance = Focal_Length / (pointpos[2] + objectpos[2] - camerapos[2])   #Focal_Length / zpos works when nothing is moving, but here we have the point, camera, and objects positions in play
    localx = pointpos[0] + objectpos[0] - camerapos[0]   #same here. we only need the x or y of the point normally, but we have other things in play   
    localy = pointpos[1] + objectpos[1] - camerapos[1]
    return (distance * localx),(distance * localy)  # Final math. We could have done this whole function on one line, but I used local variables for readability.
    # I'm not going to explain how all this math works and the logic behind it, since its sorta complicated, needs visuals, and would way to much to type here.

if __name__ == '__main__':
    main()