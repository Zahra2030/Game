import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1200, 800), pygame.RESIZABLE)

# Title and Icon
pygame.display.set_caption("Bug Debugger")
icone = pygame.image.load("virus.png")
pygame.display.set_icon(icone)

# Introduction
IntroBack = pygame.image.load("Introback.png")
IntroImg = pygame.image.load("search.png")
Customsize = (256, 256)
IntroImg = pygame.transform.scale(IntroImg, Customsize)
IntroTxt = pygame.image.load("introdoc.png")
IntroX = 90
IntroY = 395
IntroTxtX = -800
IntroTxtY = 75

# First Level
firstLevelImg = pygame.image.load('FirstLevelBack.jpg')
firstLevel = False


def FirstpageAnimation(x, y, z, n):
    """
    Displays the IntroImg and IntroTxt during the introduction phase.
    """
    screen.blit(IntroImg, (x, y))
    screen.blit(IntroTxt, (z, n))


# Game loop
running = True

while running:
    # RGB - Red, Green, Blue, transparency
    if not firstLevel:
        screen.fill((76, 0, 153, 0.6))  # Background color for intro
        screen.blit(IntroBack, (0, 0))  # Intro background

        # Animate IntroImg and IntroTxt moving horizontally
        if IntroX < 880:
            IntroX += 88
            IntroTxtX += 88
        else:
            IntroX += 0.0
            IntroTxtX += 0.0

        # Display IntroImg and IntroTxt
        FirstpageAnimation(IntroX, IntroY, IntroTxtX, IntroTxtY)
    else:
        # First level background
        screen.fill((76, 0, 153, 0.6))  # Background color for first level
        # Display first level background
        screen.blit(firstLevelImg, (-50, -250))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Transition to the first level
            firstLevel = True

    # Update the display
    pygame.display.update()
