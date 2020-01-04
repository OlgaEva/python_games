#This is a simple Python 3 Pong Game
#I'm learning simple games following freecodecamp's YouTube tutorial

import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


#Main game loop
while True:
    wn.update()

