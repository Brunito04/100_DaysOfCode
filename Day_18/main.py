#from turtle import Turtle, Screen, penup
import turtle as t
import random

turtle = t.Turtle()
turtle.shape("turtle")
turtle.color("green")
turtle.speed('fastest')
turtle.pensize(10)
t.colormode(255)


def draw_square():
        for _ in range(4):
            turtle.forward(100)
            turtle.right(90)



def dashed_line():
        for _ in range(25):
            turtle.forward(10)
            turtle.penup()

            turtle.forward(10)
            turtle.pendown()


def draw_polygon():
    for _ in range(5):
        turtle.forward(100)
        turtle.left(72)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

def random_walk():
    rand_angle = [0, 90, 180, 270]
    turtle.speed(0)
        
    while True:
        turtle.forward(random.randint(0, 50))
        turtle.setheading(random.choice(rand_angle))
        turtle.pencolor(random_color())


def draw_circle(gap_size):
    for _ in range(int(360 / gap_size)):
        turtle.circle(100)
        turtle.pencolor(random_color())
        turtle.setheading(turtle.heading() + gap_size)

    
draw_circle(5)





screen = t.Screen()
screen.exitonclick()

