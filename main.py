from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time
DOWN = 270
LEFT_POSITION = (-480, 0)
RIGHT_POSITION = (480, 0)
POSITION = [LEFT_POSITION, RIGHT_POSITION]
my_screen = Screen()
my_screen.setup(width=1000, height=600)
my_screen.bgcolor("black")
my_screen.tracer(0)



#Line setup
tim = Turtle()
tim.shape("square")
tim.color("white")
tim.penup()
tim.goto(0, 300)
tim.hideturtle()
tim.setheading(DOWN)

# Setting up initial game
def create_partition():
    for i in range(30):
        tim.pendown()
        tim.forward(10)
        tim.penup()
        tim.forward(10)
create_partition()
r_paddle = Paddle(RIGHT_POSITION)
l_paddle = Paddle(LEFT_POSITION)

ball = Ball()

r_score = Scoreboard((-40, 260))
l_score = Scoreboard((20, 260))
r_score.display_right_score()
l_score.display_left_score()

my_screen.listen()
my_screen.onkey(l_paddle.go_up, "w")
my_screen.onkey(l_paddle.go_down, "s")
my_screen.onkey(r_paddle.go_up, "Up")
my_screen.onkey(r_paddle.go_down, "Down")

is_on = True
while(is_on):
    time.sleep(0.1)
    my_screen.update()
    ball.move()
    if  ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if (ball.distance(r_paddle)<55 and ball.xcor()>450) or (ball.distance(l_paddle)<55 and ball.xcor()<-450):
        ball.bounce_x()
    if ball.xcor()>500:
        l_score.update_left_score()
        ball.retsart()
    if ball.xcor()<-500:
        r_score.update_right_score()
        ball.retsart()

my_screen.exitonclick()