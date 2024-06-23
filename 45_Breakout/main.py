#region IMPORT

import pygame
from paddle import Paddle  
from ball import Ball
from brick import Brick

#endregion

#region INIT

#Initializing pygame
pygame.init()  

#Define colors using RGB values
WHITE = (255, 255, 255)
DARKBLUE = (0, 173, 181)
LIGHTBLUE = (255, 255, 255)
RED = (170, 216, 211)
ORANGE = (238, 238, 238)
YELLOW = (57, 62, 70)

#Specify game stats
score = 0   
lives = 3   

#Initializing the screen
size = (800, 600)   
screen = pygame.display.set_mode(size)   
pygame.display.set_caption("Breakout Game")   

#Create a list for the sprite group
all_sprites_list = pygame.sprite.Group()

#Create a paddle object and set its initial position
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

#Create a ball object and set its initial position
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

#Create groups of bricks and add them to the sprite group
all_bricks = pygame.sprite.Group()

for i in range(7):
    brick = Brick(RED, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)

for i in range(7):
    brick = Brick(ORANGE, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)

for i in range(7):
    brick = Brick(YELLOW, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

#Add paddle and ball to the sprite group
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

gameOn = True    #Flag to control the game loop

clock = pygame.time.Clock()   #Initialize Pygame clock

#endregion

#region MAIN

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)

    all_sprites_list.update()

    # Boundary collisions for ball
    if ball.rect.x >= 790 or ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (250, 300))
            pygame.display.flip()
            pygame.time.wait(3000)
            gameOn = False
    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]
    if pygame.sprite.collide_mask(ball, paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()
    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
        ball.bounce()
        score += 1
        brick.kill()
        if len(all_bricks) == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (200, 300))
            pygame.display.flip()
            pygame.time.wait(3000)
            gameOn = False

    #Updating screen
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20, 10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650, 10))

    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

#endregion
