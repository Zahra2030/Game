import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 800))

# Title and icone
pygame.display.set_caption("Bug Debugger")
icone = pygame.image.load("virus.png")
pygame.display.set_icon(icone)

# Player

PlayerImg = pygame.image.load("search.png")
PlayerX = 0
PlayerY = 125


def Player():
    screen.blit(PlayerImg, (PlayerX, PlayerY))


def FirstpageAnimation(x, y):
    screen.blit(PlayerImg, (x, y))


# Game loop
running = True

while running:

    # RGB - Red, Green, Blue, transparency
    screen.fill((76, 0, 153, 0.6))

    PlayerX += 0.5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    FirstpageAnimation(PlayerX, PlayerY)

    pygame.display.update()
