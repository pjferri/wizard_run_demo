from turtle import circle, update
import pgzrun
from pgzhelper import *


#fireball = Actor('fireball', (1000, 160))
fireball = Actor('fireball', (1000,160))

playerXpos = 50
playerYpos = 252
playerCordinates = playerXpos, playerYpos
wizard = Actor('tile0', (playerCordinates))

run_images = ['tile0', 'tile1', 'tile2', 'tile3', 'tile4', 'tile5', 'tile6', 'tile7']
wizard.images = run_images


WIDTH =  800
HEIGHT = wizard.height + 200

RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
WHITE = 255, 255, 255
BLACK = 0, 0, 0
LIGHTBLUE = 169,228,239


Ground = Rect((-100, 300), (1000, 100)) #It's x,y and then size
wizardCheck = Rect((playerXpos - 40,playerYpos - 40), (wizard.width - 170, wizard.height - 100)) #Creates a rectangle around the player for collision

global currentTile
currentTile = 0

jumpCount = 0 #Prevents the player from being able to spam the jump button

score = 0

gameOver = False

def draw():
    screen.clear()
    screen.fill((BLACK))
    screen.draw.filled_rect(Ground, LIGHTBLUE)
    fireball.draw()
    wizard.draw()
    screen.draw.rect(wizardCheck,WHITE) #This shows the collision rectangle
    screen.draw.text(str(score), midtop=(400, 0))
    if gameOver:
        screen.draw.text("Game Over", (350, 60))
    #screen.draw.filled_rect(wizardCheck, RED) This is just to check where the collision rectangle is
    
wizard.fps = 10

def update(): 
    global score
    fireball.x -= 4
    if fireball.x < 0 and gameOver == False: #If fireball reaches the end, reset it and increase the score by one
        fireball.x = 1000
        score+=1
    wizard.animate()
    checkGameOver()

def on_key_down(key):
    global jumpCount
    global gameOver
    if jumpCount == 0 and gameOver == False:
        if key == keys.SPACE:
            i = 0
            while i < 100: #The purpose of using a loop here is so that the player gradually moves rather than teleports
                wizard.image = "tile5"
                wizard.y -= 1
                wizardCheck.y -= 1
                i+=1
            else:
                clock.schedule(land, 1) #Calls a function after some amount of time
            jumpCount = 1

def land():
    global jumpCount
    wizard.y = playerYpos
    wizardCheck.y = playerYpos - 40
    wizard.image = "wizardman"
    jumpCount = 0

def checkGameOver():
    global gameOver
    if fireball.colliderect(wizardCheck):
        # wizard.image = "death"
        gameOver = True

def switchRunImage():
    wizard.next_image()

pgzrun.go()
