from turtle import Turtle, Screen  
import random 

picasso = Turtle()  # Creating a Turtle object named picasso
screen = Screen()  # Creating a Screen object named screen

i = 0  #

def random_color(): 
    
    #Generates and returns a random RGB color tuple.
    
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    random_rgb = (r, g, b)

    return random_rgb

picasso.speed("fastest")  
screen.colormode(255)  

picasso.penup()  
picasso.setposition(-300.00, -300.00)  

n = 0  

# Loop to create the grid pattern
for _ in range(30):
    picasso.dot(10, random_color())  
    n += 1  

    # Nested loop to draw horizontal lines and dots
    for _ in range(30):
        picasso.forward(20)  
        picasso.dot(10, random_color())  

    # Determining the turtle's movement based on the value of n
    if n % 2 == 1:
        picasso.left(90)  
        picasso.forward(20)  
        picasso.left(90)  
    elif n % 2 == 0:
        picasso.right(90)  
        picasso.forward(20)  
        picasso.right(90)  

screen.exitonclick()  
