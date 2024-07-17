import pygame, sys
from pygame.locals import*
pygame.init()
windowSurface = pygame.display.set_mode((500,400), 0, 32)
pygame.display.set_caption('Hello world!')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
basicFont = pygame.font.SysFont(None, 48)
text = basicFont.render('Hello world!', True, BLACK, GREEN)
windowSurface.fill(BLACK)
#bg=pygame.image.load("2-2-kitten-free-download-png.png")
windowSurface.blit(bg, (0, 0))
windowSurface.blit(text,(150, 150))
pygame.draw.polygon(windowSurface,(0,255,0),((146, 0),(291, 106), (236, 277), (56, 227),(0, 106)),4)
pygame.draw.line(windowSurface,(0,0,225),(60,60),(120,60),4)
pygame.draw.circle(windowSurface,(255, 0, 0),(300, 50),20, 0)
pygame.draw.rect(windowSurface,(0,0,255),(20, 20, 80, 160),1)
pygame.display.update()





