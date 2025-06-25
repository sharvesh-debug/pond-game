from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Score
score=Score()
import time
screen=Screen()
ball=Ball()
screen.setup(800,600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("pong")
p1=Paddle((350,0))
p2=Paddle((-350,0))
paddles=[p1,p2]

screen.listen()

screen.onkey(p1.up,"Up")
screen.onkey(p1.down,"Down")
screen.onkey(p2.up,"w")
screen.onkey(p2.down,"s")

game=True
while game:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() >290 or ball.ycor() <-290 :
        ball.bounce_y()
    if  ball.xcor()>320 and ball.distance(p1)<50 or ball.xcor()<-320 and ball.distance(p2)<50 :
        ball.bounce_x()
    if ball.xcor()>380 :
         ball.goto(0,0)
         score.cl()
         ball.bounce_x()
    if ball.xcor()<-380 :
         ball.goto(0,0)
         score.cr()
         ball.bounce_x()










screen.exitonclick()
