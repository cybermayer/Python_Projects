import turtle  
import random 
import time  
from playground import Playground
from snake import Snake
from food import Food 
from scoreboard import Scoreboard

choice = input("Choose difficulty level: easy(e), regular(r), hard(h)")  

#Initilaizing the screen
screen = turtle.Screen() 
screen.bgcolor("black")  
screen.setup(width=700, height=700)  
screen.tracer(0)  
screen.listen()  

#Summoning the objects
playground = Playground()  
screen.title("THE SNAKE GAME!")  
food = Food()  
snake = Snake()  
score = Scoreboard() 
screen.update()  

# Setting up event listeners for arrow key inputs to control the snake's movement
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True  # Setting a flag to control the game loop

# Assigning speed levels based on user choice
if choice == "e":
    level = 0.3  
if choice == "r":
    level = 0.2  
if choice == "h":
    level = 0.1  

# Main game loop
while game_on == True:

    #Initialize the game conditions
    if game_on == True:
        snake.move() 
        time.sleep(level)   
        screen.update()  

    #Feed the snake
    if snake.head.distance(food) < 15:
        score.clear()  
        snake.add_part()  
        food.refresh_food()  
        score.add_score()  

    # Checking if the snake hits the wall boundaries
    if snake.head.xcor() <= -300.00 or snake.head.xcor() >= 300.00 or snake.head.ycor() <= -300.00 or snake.head.ycor() >= 300.00:
        snake.head.color("red")  
        screen.update()  
        score.clear()  
        score.game_over()  
        game_on = False  

    # Checking if the snake collides with itself
    for n in range(2, len(snake.snake_parts)):
        if snake.head.distance(snake.snake_parts[n]) < 10:
            snake.head.color("red")  
            snake.snake_parts[n].color("red")  
            screen.update()  
            score.clear()  
            score.game_over()  
            game_on = False  

screen.exitonclick()  
