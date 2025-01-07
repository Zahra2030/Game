import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 800))

# Title and icone
pygame.display.set_caption("Bug Debugger")
icone = pygame.image.load("virus.png")
pygame.display.set_icon(icone)

# Introdoction
IntroBack = pygame.image.load("Introback.png")
IntroImg = pygame.image.load("search.png")
Customsize = (256, 256)
IntroImg = pygame.transform.scale(IntroImg, Customsize)
IntroTxt = pygame.image.load("introdoc.png")
# IntroTxt = pygame.transform.scale(IntroTxt, (512, 512))
IntroX = 90
IntroY = 395
IntroTxtX = -800
IntroTxtY = 75


def FirstpageAnimation(x, y, z, n):
    screen.blit(IntroImg, (x, y))
    screen.blit(IntroTxt, (z, n))


# Game loop
running = True

while running:

    # RGB - Red, Green, Blue, transparency
    screen.fill((76, 0, 153, 0.6))
    screen.blit(IntroBack, (0, 0))

    if IntroX < 880:
        IntroX += 4
        IntroTxtX += 4
    else:
        IntroX += 0.0
        IntroTxtX += 0.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    FirstpageAnimation(IntroX, IntroY, IntroTxtX, IntroTxtY)

    pygame.display.update()
