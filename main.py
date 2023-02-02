import pygame
import os
import math
import random

#display
pygame.init()
WIDTH, HEIGHT = 800,500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman!")
#button variable
RADIUS = 20
GAP = 15
letters = []
start_x = round((WIDTH - (RADIUS*2+GAP)*13) /2)
start_y = 400
for i in range(26):
    x = start_x + GAP *2 +((RADIUS*2 +GAP)*(i%13))
    y = start_y + ((i // 13)* (GAP + RADIUS*2))
    letters.append([x,y, chr(65+i),True])
#image
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)
#game variable
hangman_status = 0
words = ["IDE","REPLIT","PYTHON","DEVELOPER","PYGAME"]
word = random.choice(words)

guesse = []
#font
LETTER_FONT = pygame.font.SysFont('comicsans', 30)
WORD_FONT = pygame.font.SysFont("comician",50)
TILTLE_FONT = pygame.font.SysFont("comician",50)
#game loop
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill((255,255,255))
    #draw word
    display_word = ""
    for letter in word:
        if letter in guesse:
            display_word += letter +" "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word,1,(0,0,0))
    win.blit(text,(400,200))


    #draw button
    for letter in letters:
        x,y, ltr,visible = letter
        if visible:

            pygame.draw.circle(win, (0,0,0), (x,y), RADIUS, 3 )
            text = LETTER_FONT.render(ltr,1,(0,0,0))
            win.blit(text, (x - text.get_width()/2,y - text.get_height()/2))
    win.blit(images[hangman_status],(150,100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill((255,153,204))
    text = WORD_FONT.render(message,1,(0,0,0))
    win.blit(text, (WIDTH/2 - text.get_width()/2,HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)
while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x,m_y = pygame.mouse.get_pos()
            for letter in letters:
                x,y,ltr,visible = letter
                dis = math.sqrt((x - m_x)**2 +(y-m_y)**2)
                if dis < RADIUS:
                    letter[3] = False
                    guesse.append(ltr)
                    if ltr not in word:
                        hangman_status +=1


    draw()
    won = True
    for letter in word:
        if letter not in guesse:
            won = False
            break
    if won:
        display_message("YOU mtfk WON")
        break


    if hangman_status == 6:
        display_message("You lose")
        break
pygame.quit()        
