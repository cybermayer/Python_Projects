def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear() == False:
        turn_left()
    else:
        move()
        turn_right()
            
            
       
        
