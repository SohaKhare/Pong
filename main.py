from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score
### Setting up the screen
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#Creating dashed line along middle
dash = Turtle()
dash.hideturtle()
dash.color("white")
dash.penup()
dash.goto(0, -300)
dash.setheading(90)
dash.width(5)

for _ in range(11):
    dash.pendown()
    dash.forward(30)
    dash.penup()
    dash.forward(30)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

### To use right paddle
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

score = Score()
ball = Ball()
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor()<-280:
        ball.bounce_y()

    #Detect collision with right paddle
    if (ball.xcor()>320 and ball.distance(r_paddle) <= 50) or (ball.xcor()<-320 and ball.distance(l_paddle) <= 50):
        ball.bounce_x()

    if ball.xcor()>350:
        score.leftincrease()
        ball.reset_ball()
    if ball.xcor()<-350:
        score.rightincrease()
        ball.reset_ball()
        

screen.exitonclick()