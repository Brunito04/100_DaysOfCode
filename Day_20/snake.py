from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake():
    def __init__(self):
        #Variables
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def move(self): 
        for seg_num in range(len(self.segments) - 1, 0, -1): # The first argunment is the last position (start=), the second is the first one (stop=), and the third is the (step=) where the first element will move
        
            #Moves each square to the next position
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
        
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)\

         
    def add_segment(self, position):
        new_object = Turtle("square")
        new_object.color("white")
        new_object.penup()
        new_object.goto(position)
        self.segments.append(new_object)

    def extend(self): 
        self.add_segment(self.segments[-1].position())
        


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
        else:
            pass

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        else: 
            pass
            

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
        else: 
            pass

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
        else: 
            pass

        

