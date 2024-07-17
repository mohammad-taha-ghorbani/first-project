import pygame, sys ,time
from pygame.locals import*
pygame.init()
windowWidth=1080
windowHight=720
windowSurface=pygame.display.set_mode((windowWidth, windowHight), 0, 32)
pygame.display.set_caption('Animation')
MOVESPEED=10000
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLACK=(0,0,0)
BLUE=(0,0,255)
DOWN='down'
b1 = {'rect':pygame.Rect(865, 56, 56, 200), 'color':RED, 'dir':DOWN}
b2 = {'rect':pygame.Rect(678, 256, 70, 344), 'color':GREEN, 'dir':DOWN}
b3 = {'rect':pygame.Rect(234, 158, 39, 62), 'color':BLACK, 'dir':DOWN}
b4 = {'rect':pygame.Rect(412, 186, 25, 94), 'color':BLUE, 'dir':DOWN}
boxes = [b1, b2, b3, b4]
while True:
    for even in pygame.event.get():
        if even.type== QUIT:
            pygame.quit()
            sys.exit()
    windowSurface.fill(WHITE)
    for b in boxes:
        if b['dir'] == DOWN:
            b['rect'].top += MOVESPEED
        if b['rect'].top > windowHight:
            b['rect'].bottom= 0
        pygame.draw.rect(windowSurface, b['color'], b['rect'])
    pygame.display.update()
    time.sleep(0.02)









            
