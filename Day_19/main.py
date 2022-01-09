from turtle import Turtle, Screen

turtle = Turtle()

screen = Screen()


def move_forward():
    turtle.forward(10)


# Event listener
screen.listen()
screen.onkey(key="space", fun=move_forward) #Higher order function (pass a function inside a function)











screen.exitonclick()