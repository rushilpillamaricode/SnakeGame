from turtle import Turtle, Screen
import time


POSITIONS = [(0,0),(-20,0),(20,0)]



class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create()
        self.head = self.segments[0]
    
    def create(self):
        for i in range(len(POSITIONS)):
            self.addsegment(POSITIONS[i])

        
    def addsegment(self,position):
        segment1 = Turtle('square')
        segment1.speed("fastest")
        segment1.color("white")
        segment1.penup()
        segment1.goto(position)
        self.segments.append(segment1)
    
    def growth(self):
        self.addsegment(self.segments[-1].position())
    
    def gooverwall(self,x,y):
        self.head.goto(x,y)
    

    def move(self):
        for seg in range(len(self.segments) - 1,0,-1):
            self.segments[seg].goto(self.segments[seg - 1].xcor(),self.segments[seg - 1].ycor())
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
        
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
        
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
        