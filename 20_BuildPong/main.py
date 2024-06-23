import turtle
import random
import time
import board
import score
import start_in
import racket
import ball

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=1300, height=700)
screen.title("BUILD PONG")
screen.mode("logo")


# set up the enviroment
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=1300, height=700)
screen.title("BUILD PONG")
gboard = board.Gameboard()
score = score.Score()


screen.tracer(0)
racket = racket.Racket()
screen.tracer(1)
ball = ball.Ball()


starter = start_in.StartIn()

screen.onkeypress(racket.left_move_up, "w")
screen.onkeypress(racket.left_move_down, "s")
screen.onkeypress(racket.right_move_up, "Up")
screen.onkeypress(racket.right_move_down, "Down")

# binding the movement of rackets with keys
screen.listen()


purgatory = True

while purgatory == True:

    game_on = True
    screen.tracer(0)
    racket.move_zero()
    starter.start()
    screen.tracer(1)

    while game_on == True:

        time.sleep(0.02)
        screen.tracer(0)
        ball.move_ball()
        screen.update()

        for lps in racket.left_parts:
            if ball.distance(lps) < 28:
                ball.racket_bounce()

        for rps in racket.right_parts:
            if ball.distance(rps) < 28:
                ball.racket_bounce()

        if ball.ycor() > 300 or ball.ycor() < -300:
            ball.wall_bounce()

        if ball.xcor() > 610:
            ball.home()
            ball.setheading(90)
            score.increase_left_score()
            game_on = False
        elif ball.xcor() < -610:
            ball.home()
            ball.setheading(270)
            score.increase_right_score()
            game_on = False

screen.exitonclick()
