#region IMPORT

from turtle import Screen
from AlienFleet import Fleet
from SpaceShip import SpaceShip
from Barrier import Barrier
from Scoreboard import Scoreboard
from time import sleep
from Bullet import Bullet  # Adjusted import statement
import random
from AlienBomb import AlienBombManager

#endregion 

#region INIT

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Space Invasion!!")
screen.tracer(0)  # Turn off animation updates for smoother rendering
screen.register_shape('ship', ((-10,0),(0,10),(10,0)))
screen.register_shape('alien.gif')

# Initialize game objects
player = SpaceShip()
barrier1 = Barrier(-260, -220)
fleet = Fleet(-240, 160)
bomb = AlienBombManager()
bullet = None
scoreboard = Scoreboard()

# Keyboard bindings
screen.update()
screen.listen()
screen.onkey(player.go_left, "a")
screen.onkey(player.go_right, "d")
screen.onkey(FireBullet, "space")

#endregion

def FireBullet():

    """<DOC
        
        Fires a bullet.

    DOC?>"""

    #region CODE

    global bullet
    if bullet is None:
        bullet = Bullet(position_x=player.xcor(), position_y=player.ycor())

    #endregion 

def DeleteBullet():

    """<DOC

        Deletes the bullet.
    
    DOC?>"""

    #region CODE

    global bullet
    if bullet is not None:
        bullet.goto(3000, 3000)
        bullet.clear()
        del bullet
        bullet = None

    #endregion 

def RandomAlienBomb():

    #region CODE

    random_chance = random.randint(1, 12)
    if random_chance == 1:
        random_alien = random.choice(fleet.aliens)
        bomb.MakeBomb(position_x=random_alien.xcor(), position_y=random_alien.ycor())

    #endregion

#region MAIN

#Main game loop
game_is_on = True
while game_is_on:
    sleep(0.0001)
    screen.update()

    #Check win condition
    if len(fleet.aliens) <= 0:
        scoreboard.GameOver(Reason="Won")
        game_is_on = False

    #Check lose condition
    if scoreboard.lives <= 0:
        scoreboard.GameOver(Reason="Lives")
        game_is_on = False

    #Alien movements
    fleet.MoveFleet()
    fleet.DetectLeftRightBoundaries()
    if fleet.DetectLowerBoundary():
        scoreboard.GameOver(Reason="Invaded")
        game_is_on = False

    #Alien bomb actions
    RandomAlienBomb()
    bomb.moveBombs()
    bomb.DetectLowerLimit()
    
    #Check collisions with player and barriers
    for bombx in bomb.bombs:
        if player.distance(bombx) < 20:
            scoreboard.RemoveLife()
            bomb.DeleteBomb(Bomb=bombx)
            player.respawn()
            continue
        
        for brick in barrier1.bricks:
            if bombx.distance(brick) < 7:
                barrier1.DeleteBrick(brick=brick)
                bomb.DeleteBomb(Bomb=bombx)
                break

    #Player bullet actions
    if bullet is not None:
        bullet.BulletMove()
        if bullet.DetectTopLimit():
            DeleteBullet()
        else:
            for brick in barrier1.bricks:
                if bullet.distance(brick) < 8:
                    barrier1.DeleteBrick(brick=brick)
                    DeleteBullet()
                    break
            
            if bullet is not None:
                for alien in fleet.aliens:
                    if bullet.distance(alien) < 10:
                        fleet.DeleteAlien(alien)
                        scoreboard.score += 20
                        scoreboard.RefreshScore()
                        DeleteBullet()
                        break
                
                if bullet is not None:
                    for bombx in bomb.bombs:
                        if bullet.distance(bombx) < 5:
                            bomb.DeleteBomb(bombx)
                            scoreboard.score += 5
                            scoreboard.RefreshScore()
                            DeleteBullet()
                            break

screen.mainloop()
screen.exitonclick()

#endregion 
