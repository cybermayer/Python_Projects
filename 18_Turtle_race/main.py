import random 
from turtle import Turtle, Screen  

screen = Screen()  # Creating a Screen object named screen
screen.setup(width=600, height=500)  # Setting up the screen dimensions

# Asking the user to input their bet on the winning turtle
user_bet = screen.textinput(title="Make your bet",
                            prompt="Try to guess which turtle will win the race!")

service_turtle = Turtle()  
service_turtle.penup() 
service_turtle.setposition(218.00, -100.00)  
service_turtle.left(90) 
service_turtle.pendown()  
service_turtle.pensize(3)
service_turtle.forward(350)  

# Creating Turtle objects for each racing turtle with specific attributes
red = Turtle()
red.penup()
red.color("red")
red.shape("turtle")
red.setposition(-300.00, 200.00)

yellow = Turtle()
yellow.penup()
yellow.color("yellow")
yellow.shape("turtle")
yellow.setposition(-300.00, 150.00)

blue = Turtle()
blue.penup()
blue.color("blue")
blue.shape("turtle")
blue.setposition(-300.00, 100.00)

purple = Turtle()
purple.penup()
purple.color("purple")
purple.shape("turtle")
purple.setposition(-300.00, 50.00)

orange = Turtle()
orange.penup()
orange.color("orange")
orange.shape("turtle")
orange.setposition(-300.00, 0.00)

green = Turtle()
green.penup()
green.color("green")
green.shape("turtle")
green.setposition(-300.00, -50.00)

# Creating a list of all the turtle objects
turtles = [red, yellow, blue, purple, orange, green]

def move(color):
  
    #Moves the given turtle forward by a random distance and returns its current x-coordinate.
  
    rspeed = round(random.random(), 2) * random.randint(1, 3) 
    color.forward(rspeed) 
    xcor = color.xcor()  
    return xcor  

finishing_line = 200.00  
actual_xpos = 0 
winner_xpos = -300.00  
winner_color = ''  

# Loop to simulate the race until a turtle crosses the finishing line
while finishing_line > winner_xpos:
    for trtls in turtles:  
        actual_xpos = move(trtls)  
        if winner_xpos < actual_xpos:  
            winner_xpos = actual_xpos 
            winner_color = trtls.color()[0] 

# Checking if the user's bet matches the color of the winning turtle and printing the result
if winner_color == user_bet:
    print(f"Congratulations the {user_bet} won!")
  else:
      print(f"Sorry the {winner_color} won!")

screen.exitonclick()  # Allowing the screen to exit on click
