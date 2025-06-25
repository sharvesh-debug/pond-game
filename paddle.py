from turtle import Turtle,Screen
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        s=Screen()
        s.bgcolor("black")
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.setheading(90)
        self.shapesize(1, 5)
        self.goto(position)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
