import pygame, random, sys
from pygame.locals import*
WINDOWWIDTH = 1080
WINDOWHEIGHT = 720
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (255, 255, 255)
FPS = 120
TREEMINSIZE = 20
TREEMAXSIZE = 50
TREESPEED = 5
ADDNEWTREERATE = 6
PLAYERMOVERATE = 5
def terminate():
    pygame.quit()
    sys.exit()
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type ==QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return
def playerHasHitTree(playerRect, trees):
    for t in trees:
        if playerRect.colliderect(t['rect']):
            return True
    return False
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Ski Tree')
pygame.mouse.set_visible(False)
font = pygame.font.SysFont(None, 48)
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mid')
backGroundImage = pygame.image.load('snow.jpg')
playerImage = pygame.image.load('skier.png')
playerRect = playerImage.get_rect()
treeImage = pygame.image.load('tree.png')
windowSurface.fill(BACKGROUNDCOLOR)
drawText('Ski Tree', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press any key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()
topScore = 0
while True:
    trees = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reversCheat = slowCheat = False
    treeAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)
    while True:
        score += 1
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == K_w:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == K_s:
                    moveUp = False
                    moveDown = True
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False
            if event.type == MOUSEMOTION:
                playerRect.centerx = event.pos[0]
                playerRect.centery = event.pos[1]
        treeAddCounter += 1
        if treeAddCounter == ADDNEWTREERATE:
            treeAddCounter = 0
            treeSize = random.randint(TREEMINSIZE, TREEMAXSIZE)
            newTree = {'rect':pygame.Rect(random.randint(0, WINDOWWIDTH - treeSize), 0 - treeSize, treeSize, treeSize), 'speed': TREESPEED, 'surface':pygame.transform.scale(treeImage, (treeSize, treeSize)),}
            trees.append(newTree)
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0,-1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        for t in trees:
            t['rect'].move_ip(0, t['speed'])
        for t in trees:
            if t['rect'].top > WINDOWHEIGHT:
                trees.remove(t)
        windowSurface.fill(BACKGROUNDCOLOR)
        drawText('Score: %s' % (score), font, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)
        windowSurface.blit(playerImage, playerRect)
        for t in trees:
            windowSurface.blit(t['surface'], t['rect'])
        pygame.display.update()
        if playerHasHitTree(playerRect, trees):
            if score > topScore:
                topScore = score
            break
        mainClock.tick(FPS)
    pygame.mixer.music.stop()
    gameOverSound.play()
    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Prees a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()
    gameOverSound.stop()
            

                


























            
