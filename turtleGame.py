from turtle import *
import random

number = 1

setup(1000, 1000)
Screen()
title("Turtle Keys")
move = Turtle()
hideturtle()
move.pencolor("blue")
move.pensize(5)

def k1():
    move.forward(36)

def k2():
    move.left(36)

def k3():
    move.right(36)

def k4():
    move.pencolor("white")
    move.back(36)
    move.pencolor("blue")

onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
onkey(k4, "Down")

listen()
mainloop()
