import pygame, sys ,time
from pygame.locals import*
pygame.init()
windowWidth=1080
windowHight=720
windowSurface=pygame.display.set_mode((windowWidth, windowHight), 0, 32)
pygame.display.set_caption('Animation')
MOVESPEED=4
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLACK=(0,0,0)
downleft = 'downleft'
downright = 'downright'
upleft = 'upleft'
upright = 'upright'
b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':upright}
b2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':downright}
b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLACK, 'dir':downleft}
boxes = [b1, b2, b3]
while True:
    for even in pygame.event.get():
        if even.type== QUIT:
            pygame.quit()
            sys.exit()
    windowSurface.fill(WHITE)
    for b in boxes:
        if b['dir'] == downleft:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == upleft:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir'] == downright:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == upright:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['rect'].left < 0:
            if b['dir'] == downleft:
                b['dir'] = downright
            if b['dir'] == upleft:
                b['dir'] = upright
        if b['rect'].top < 0:
            if b['dir'] == upleft:
                b['dir'] = downleft
            if b['dir'] == upright:
                b['dir'] = downright
        if b['rect'].bottom > windowHight:
            if b['dir'] == downleft:
                b['dir'] = upleft
            if b['dir'] == downright:
                b['dir'] = upright
        if b['rect'].right > windowWidth:
            if b['dir'] == downright:
                b['dir'] = downleft
            if b['dir'] == upright:
                b['dir'] = upleft
        pygame.draw.rect(windowSurface, b['color'], b['rect'])
    pygame.display.update()
    time.sleep(0.02)
