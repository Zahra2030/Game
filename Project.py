import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Minimalist Puzzle Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # white background
    pygame.display.update()

pygame.quit()
