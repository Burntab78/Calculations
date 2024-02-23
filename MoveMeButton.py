# screensaver
# import libs and modules
import turtle
import random
import time

# make screen playground
form = turtle.Screen()
form.title("MoveMe")
form.bgcolor('black')
form.setup(800,600)
form.tracer(0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color('white')
ball.shapesize(5,5)
ball.penup()
ball.goto(0,0)
ball.dx = 0.05
ball.dy = 0.1

list = ["red", "blue", "yellow", "green", "purple", "orange", "white" ]

while True:
    form.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        color = random.choice(list)
        ball.color(color)
    
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
        color = random.choice(list)
        ball.color(color)

    if ball.xcor()>390:
        ball.setx(390)
        ball.dx*=-1
        color = random.choice(list)
        ball.color(color)

    if ball.xcor()<-390:
        ball.setx(-390)
        ball.dx*=-1
        color = random.choice(list)
        ball.color(color)
    
time.sleep(10/100)