from ast import Or
from turtle import circle, update
import pgzrun
from pgzhelper import *
import random


playerXpos = 50
playerYpos = 252
playerCordinates = playerXpos, playerYpos
wizard = Actor('tile0', (playerCordinates))

run_images = ['tile0', 'tile1', 'tile2', 'tile3', 'tile4', 'tile5', 'tile6', 'tile7']
wizard.images = run_images

fireball = Actor('fire0', (1000, 140))
fire_flames = ['fire0','fire1','fire2','fire3','fire4']
fireball.images = fire_flames

orb = Actor('orb0', (1000, 250)) #250 is where the player is, 160 is just above him
orb_flare = ['orb1','orb2','orb3','orb4','orb5','orb6','orb7','orb8','orb9','orb10','orb11', 'orb12','orb13']
orb.images = orb_flare

background = Actor("background3", (320,200))
background2 = Actor("background3", (960,200))
background3 = Actor("background3", (1600,200))

WIDTH =  800
HEIGHT = wizard.height + 200

RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
WHITE = 255, 255, 255
BLACK = 0, 0, 0
LIGHTBLUE = 169,228,239
DARKGREY = 27,27,27


Ground = Rect((-100, 300), (1000, 100)) #It's x,y and then size
wizardCheck = Rect((playerXpos - 40, playerYpos - 40), (wizard.width - 170, wizard.height - 100)) #Creates a rectangle around the player for collision

global currentTile
currentTile = 0

jumpCount = 0 #Prevents the player from being able to spam the jump button

score = 0

gameOver = False

def draw():
    screen.clear()
    screen.fill((BLACK))
    background.draw()
    background2.draw()
    background3.draw()
    screen.draw.filled_rect(Ground, DARKGREY)
    fireball.draw()
    wizard.draw()
    orb.draw()
    
    #screen.draw.rect(wizardCheck,WHITE) #This shows the collision rectangle
    screen.draw.text(str(score), midtop=(400, 0))
    if gameOver:
        screen.draw.text("Game Over", (350, 60))
    #screen.draw.filled_rect(wizardCheck, RED) This is just to check where the collision rectangle is
    
wizard.fps = 10 #Controls the animation speed, the default is 5
orb.fps = 10
fireball.fps = 10

fireballSpeed = 4
orbSpeed = 3

def update(): 
    global score
    if gameOver == False:
        background.x -= 1.75
        background2.x -= 1.75
        background3.x -= 1.75
    if background.x < -320:
        background.x = 1600
    if background2.x < -320:
        background2.x = 1600
    if background3.x < -320:
        background3.x = 1600

    fireball.x -= fireballSpeed
    if fireball.x < 0 and gameOver == False: #If fireball reaches the end, reset it and increase the score by one
        fireball.x = 1000
        score+=1
    orb.x -= orbSpeed
    if orb.x < 0 and gameOver == False:
        orb.x = 1000
        score+=1
    if gameOver == False and jumpCount < 1:
        wizard.animate()
    if score % 4 == 0 and score > 1:
        clock.schedule(increaseDifficulty, 0.1)

    orb.animate()
    fireball.animate()
    checkGameOver()

def on_key_down(key):
    global jumpCount
    global gameOver
    if jumpCount == 0 and gameOver == False:
        if key == keys.SPACE:
            i = 0
            while i < 100: #The purpose of using a loop here is so that the player gradually moves rather than teleports
                wizard.image = "jump0"
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
    jumpCount = 0

#alt fireball.colliderect(wizardCheck)
def checkGameOver():
    global gameOver
    if fireball.circle_collidepoint(70, wizardCheck.x, wizardCheck.y) or orb.circle_collidepoint(70, wizardCheck.x, wizardCheck.y): #70 represents the size of the collision circle, the x and y are 
        wizard.image = "death5"
        gameOver = True


def increaseDifficulty():
    global fireballSpeed
    global orbSpeed
    global score
    
    if score == 4:
        fireballSpeed = 5
        orbSpeed = 5
    if score == 8:
        fireballSpeed = 6
        orbSpeed = 6
    if score == 12:
        fireballSpeed = 7
        orbSpeed = 7
    if score == 16:
        fireballSpeed = 8
        orbSpeed = 8
    if score == 20:
        fireballSpeed = 9
        orbSpeed = 9
    if score > 24:
        fireballSpeed = 10
        orbSpeed = 10

pgzrun.go()
