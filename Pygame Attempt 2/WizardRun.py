from turtle import circle, update
import pgzrun

#fireball = Actor('fireball', (1000, 160))
fireball = Actor('fireball', (1000,160))

playerXpos = 50
playerYpos = 160
playerCordinates = playerXpos, playerYpos
wizard = Actor('wizardman', (playerCordinates))


WIDTH =  800
HEIGHT = wizard.height + 200

RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
WHITE = 255, 255, 255
BLACK = 0, 0, 0
LIGHTBLUE = 169,228,239


BOX = Rect((-100, 200), (1000, 100)) #It's x,y and then size
wizardCheck = Rect((playerXpos - 75,playerYpos - 40), (wizard.width, wizard.height - 20))

global currentTile
currentTile = 0

jumpCount = 0

score = 0

gameOver = False

def draw():
    screen.clear()
    screen.fill((BLACK))
    screen.draw.filled_rect(BOX, LIGHTBLUE)
    fireball.draw()
    wizard.draw()
    screen.draw.text(str(score), midtop=(400, 0))
    if gameOver:
        screen.draw.text("Game Over", (350, 60))
    #screen.draw.filled_rect(wizardCheck, RED) This is just to check where the collision rectangle is
    

def update(): 
    global score
    fireball.x -= 2
    if fireball.x < 0 and gameOver == False:
        fireball.x = 1000
        score+=1
    checkGameOver()

def on_key_down(key):
    global jumpCount
    global gameOver
    if jumpCount == 0 and gameOver == False:
        if key == keys.SPACE:
            i = 0
            while i < 100:
                wizard.image = "tile5"
                wizard.y -= 1
                wizardCheck.y -= 1
                i+=1
            else:
                clock.schedule(land, 1.3)
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

        

pgzrun.go()
