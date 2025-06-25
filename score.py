from turtle import Turtle,Screen
class Score(Turtle):
    def __init__(self):
        s=Screen()
        s.bgcolor("black")
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l=0
        self.r=0
        self.goto(-100,200)
        self.write(f"{self.l}",align="center",font=("Courier",50,"normal"))
        self.goto(100, 200)
        self.write(f"{self.r}", align="center", font=("Courier", 50, "normal"))
    def cr(self):
        self.r+=1
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l}", align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(f"{self.r}", align="center", font=("Courier", 50, "normal"))
    def cl(self):
        self.l += 1
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l}", align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(f"{self.r}", align="center", font=("Courier", 50, "normal"))






