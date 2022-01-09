from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()



def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def rotate_clockwise():
    actual_heading = turtle.heading()
    turtle.setheading(actual_heading + 10)


def rotate_Counter_Clockwise():
    actual_heading = turtle.heading()
    turtle.setheading(actual_heading - 10)
    

def clear_drawing():
    turtle.reset()



# Events listeners
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_Counter_Clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear_drawing)


screen.exitonclick()
