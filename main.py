import sys
import time
import pygame
from pygame.locals import *

pygame.init() 
infos = pygame.display.Info()
screen_size = (infos.current_w, infos.current_h)
surface = pygame.display.set_mode(screen_size, SCALED)
clock = pygame.time.Clock()
myfont = pygame.font.SysFont("Arial", 64)

#BUTTONS IMAGES
#UNCLICKED
dfb = 'buttons/' #directory for buttons
up_unclicked = pygame.image.load(dfb+'up_unclicked.png')
up_unclicked = pygame.transform.scale(up_unclicked,(130,130))
down_unclicked = pygame.image.load(dfb+'down_unclicked.png')
down_unclicked = pygame.transform.scale(down_unclicked,(130,130))
left_unclicked = pygame.image.load(dfb+'left_unclicked.png')
left_unclicked = pygame.transform.scale(left_unclicked,(130,130))
right_unclicked = pygame.image.load(dfb+'right_unclicked.png')
right_unclicked = pygame.transform.scale(right_unclicked,(130,130))
A_unclicked = pygame.image.load(dfb+'A_unclicked.png')
A_unclicked = pygame.transform.scale(A_unclicked,(130,130))
B_unclicked = pygame.image.load(dfb+'B_unclicked.png')
B_unclicked = pygame.transform.scale(B_unclicked,(130,130))
C_unclicked = pygame.image.load(dfb+'C_unclicked.png')
C_unclicked = pygame.transform.scale(C_unclicked,(130,130))
D_unclicked = pygame.image.load(dfb+'D_unclicked.png')
D_unclicked = pygame.transform.scale(D_unclicked,(130,130))
#/UNCLICKED
#CLICKED
up_clicked = pygame.image.load(dfb+'up_clicked.png')
up_clicked = pygame.transform.scale(up_clicked,(130,130))
down_clicked = pygame.image.load(dfb+'down_clicked.png')
down_clicked = pygame.transform.scale(down_clicked,(130,130))
left_clicked = pygame.image.load(dfb+'left_clicked.png')
left_clicked = pygame.transform.scale(left_clicked,(130,130))
right_clicked = pygame.image.load(dfb+'right_clicked.png')
right_clicked = pygame.transform.scale(right_clicked,(130,130))
A_clicked = pygame.image.load(dfb+'A_clicked.png')
A_clicked = pygame.transform.scale(A_clicked,(130,130))
B_clicked = pygame.image.load(dfb+'B_clicked.png')
B_clicked = pygame.transform.scale(B_clicked,(130,130))
C_clicked = pygame.image.load(dfb+'C_clicked.png')
C_clicked = pygame.transform.scale(C_clicked,(130,130))
D_clicked = pygame.image.load(dfb+'D_clicked.png')
D_clicked = pygame.transform.scale(D_clicked,(130,130))
#/CLICKED
pause = pygame.image.load(dfb+'pause.png')
pause = pygame.transform.scale(pause,(60,60))
del(dfb)
#/BUTTONS IMAGES

#State of button. True when clicked and False when unclicked
butsta = {'UP': False, 'DOWN': False, 'LEFT': False, 'RIGHT': False, 'A': False, 'B': False, 'C': False, 'D': False, 'PAUSE': False}

#Button ranges of coordinates to detect button clicks on screen
butran = {'UP': list((range(85,180),range(995,1090))),
          'DOWN': list((range(85,180),range(1125, 1205))),
          'LEFT': list((range(-10,190),range(1070,1150))),
          'RIGHT': list((range(170,270),range(1070,1155))),
          'A': list((range(525,620),range(995,1090))),
          'B': list((range(440,540),range(1070,1150))),
          'C': list((range(620,710),range(1070,1150))),
          'D': list((range(525,620),range(1125,1205))),
          'PAUSE': list((range(320,380),range(980,1040)))}
butfreeze = False
colors, cc = {0: 'White', 1: 'Red', 2: 'Green', 3: 'Blue', 4: 'Pink', 5: 'Yellow', 6: 'Orange', 7: 'Black'}, 0
radius = 50

rx, ry = 358, 475
mbd = False

#Game loop
while True:    
    mx,my = pygame.mouse.get_pos()
    mbd = False
    surface.fill((80,80,80))
    pygame.draw.rect(surface, (80,80,80), [0, 950, 720, 350])
    pygame.draw.line(surface, 'white', (0,950), (717, 950)) 
    pygame.draw.circle(surface, colors[cc], (rx, ry), radius)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mbd = True
        if event.type == MOUSEBUTTONUP:
            pygame.mouse.set_pos((0,0))
    
    for key in butran.keys():
        if mx in butran[key][0] and my in butran[key][1]:
            butsta[key] = True
    
    if butfreeze: surface.blit(myfont.render('PAUSED',1,(255,255,255)),(230, 5))
     
    if butsta['UP'] and not butfreeze:
        if not(ry <= radius): ry -= 5
    if butsta['DOWN'] and not butfreeze:
        if not(950-ry <= radius): ry += 5
    if butsta['LEFT'] and not butfreeze:
        if not(rx <= radius): rx -= 5
    if butsta['RIGHT'] and not butfreeze:
        if not(718-rx <= radius): rx += 5
    if butsta['A'] and not butfreeze and mbd:
        if cc == 7: cc = 0
        else: cc += 1
    if butsta['B'] and not butfreeze:
        if cc == 0: cc = 7
        else: cc -= 1
    if butsta['C'] and not butfreeze: 
        if radius <= 250: radius += 10
    if butsta['D'] and not butfreeze:
        if radius >= 10: radius -= 10
    if butsta['PAUSE'] and mbd:
        butfreeze = not butfreeze
        surface.blit(myfont.render('PAUSED',1,(255,255,255)),(230, 5))
     
    surface.blit(up_clicked if butsta['UP'] else up_unclicked,(70,980))
    surface.blit(down_clicked if butsta['DOWN'] else down_unclicked,(70,1110))
    surface.blit(left_clicked if butsta['LEFT'] else left_unclicked,(-10,1050))
    surface.blit(right_clicked if butsta['RIGHT'] else right_unclicked,(150,1050))
    surface.blit(A_clicked if butsta['A'] else A_unclicked,(510,980))
    surface.blit(B_clicked if butsta['B'] else B_unclicked,(430,1050))
    surface.blit(C_clicked if butsta['C'] else C_unclicked,(590,1050))
    surface.blit(D_clicked if butsta['D'] else D_unclicked,(510,1110))
    surface.blit(pause,(320,980))

    for key in butsta.keys():
        butsta[key] = False  
    clock.tick(60)
    pygame.display.update()
    
    
    