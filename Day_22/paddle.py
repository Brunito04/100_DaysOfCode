from turtle import Turtle

class Paddle(Turtle): 
    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.speed("fastest")
        self.setposition(position)
        self.setheading(90)    
    
    
    def move(self): 
        self.forward(10)

    def up(self):
        self.setheading(90)
        self.move()

    def down(self): 
        self.setheading(270)
        self.move()
