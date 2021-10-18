
import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))

#creating objects of game
player=pygame.Rect(200,500,30,30)
playerSpeed=20
enemy=pygame.Rect(70,50,40,40)
enemyspeed= -2;

bullet=pygame.Rect(200,400,5,10)
bulletspeed=5 
bulletState="ready"
        
while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x -=playerSpeed
            if event.key ==pygame.K_RIGHT:
                player.x +=playerSpeed
            if event.key == pygame.K_SPACE:
                bulletState="fired"
    #Code for the ready state 
    if bulletState == "ready":
        bullet.x=player.x+12
        bullet.y=player.y
    
    #Add the code for the fired state.
        
        #Add the code to change the state back to ready state once bullet goes out from top edge of the screen
    

                   
    enemy.x= enemy.x + enemyspeed
    
    if enemy.x == 0:
        enemyspeed=enemyspeed * -1
        enemy.y= enemy.y + 20
    
    if enemy.x == 380:
        enemyspeed=enemyspeed * -1
        enemy.y= enemy.y + 20
        
    pygame.draw.rect(screen,(225,225,15),bullet)         
    pygame.draw.rect(screen,(123,200,100),enemy)
    pygame.draw.rect(screen,(23,100,100),player)
    
    
    pygame.display.update()
    clock.tick(30)

