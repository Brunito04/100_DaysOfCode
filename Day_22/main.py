from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
# Right paddle
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

# Left paddle
screen.onkey(l_paddle.up, ".")
screen.onkey(l_paddle.down, "e")



while game_is_on:
    screen.update()
    r_paddle.move()
    l_paddle.move()
    ball.move()

    #Detect paddle right colision with wall
    if r_paddle.ycor() > 260:
        r_paddle.down()
    elif r_paddle.ycor() < -260:
        r_paddle.up()
    
    
    #Detect paddle left collision with wall
    if l_paddle.ycor() > 260:
        l_paddle.down()
    elif l_paddle.ycor() < -260:
        l_paddle.up()
    
    
    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    #Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect when right paddle misses
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()
    
    #Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()










screen.exitonclick()