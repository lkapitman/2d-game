import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Anus Game")

walkRight = [pygame.image.load('right_1.png'),pygame.image.load('right_2.png'),pygame.image.load('right_3.png'),pygame.image.load('right_4.png'),pygame.image.load('right_5.png'),pygame.image.load('right_6.png')]
walkLeft = [pygame.image.load('left_1.png'),pygame.image.load('left_2.png'),pygame.image.load('left_3.png'),pygame.image.load('left_4.png'),pygame.image.load('left_5.png'),pygame.image.load('left_6.png')]

bg = pygame.image.load('bg.jpg')

playerStand = pygame.image.load('idle.png')

clock = pygame.time.Clock()

x = 50
y = 430

widht = 60
height = 71
speed = 5
isJump = False
countJump = 10

left = False
right = False
animCount = 0

def drawWindow():
    global animCount
    win.blit(bg, (0, 0))
    if animCount + 1 >= 30:
        animCount = 0
    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))
    pygame.display.update()

while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 -widht - 5:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if countJump >= -10:
            if countJump < 0:
                y += (countJump ** 2) / 2
            else:
                y -= (countJump ** 2) / 2
            countJump -= 1
        else:
            isJump = False
            countJump = 10

    drawWindow()
