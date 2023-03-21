from turtle import Turtle, Screen
from Scoreboard import Scoreboard
from Paddle import Paddle
from Ball import Ball
import time

screen = Screen()
screen.bgcolor('green')
screen.setup(height= 600, width = 900)
screen.title('Naveen Pong')
screen.tracer(0)

tt = Turtle()
score = Scoreboard()
ball = Ball()


r_paddle = Paddle((400, 0))
l_paddle = Paddle((-400, 0))



screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')



game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # Detect collision of the ball with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect R paddle miss
    if ball.xcor() > 390:
        ball.reset_position()
        score.l_point()



    # Detect L paddle miss
    if ball.xcor() < -390:
        ball.reset_position()
        score.r_point()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 385 or ball.distance(l_paddle) < 50 and ball.xcor() < -385:
        ball.bounce_x()
        print('Ball is near the right paddle')







screen.exitonclick()