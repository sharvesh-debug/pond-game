from turtle import Turtle,Screen

class Ball(Turtle):
    def __init__(self):

        super().__init__()
        s=Screen()
        s.bgcolor("black")
        s.setup(800, 600)
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(1)
        self.dx=10
        self.dy=10
    def move(self):
        nx=self.xcor()+self.dx
        ny=self.ycor() +self.dy
        self.goto(nx,ny)


    def bounce_y(self):
        self.dy*=-1
    def bounce_x(self):
        self.dx*=-1




