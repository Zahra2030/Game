import pygame
import random
import math
import time

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1200, 800), pygame.RESIZABLE)

# Title and Icon
pygame.display.set_caption("Bug Debugger")
icon = pygame.image.load("virus.png")
pygame.display.set_icon(icon)

# Game variables
debug_chance = 5
moth_caught = 0
first_level = False
lose = False
win = False
story_shown = False
story_timer = 0

# Images
losing_img = pygame.image.load("game-over.png")
winning_img = pygame.image.load("win.png")
intro_back = pygame.image.load("Introback.png")
intro_img = pygame.image.load("search.png")
intro_img = pygame.transform.scale(intro_img, (256, 256))
intro_txt = pygame.image.load("introdoc.png")
first_level_img = pygame.image.load('FirstLevelBack.jpg')
moth_img = pygame.image.load("corn-borer.png")
moth_img = pygame.transform.scale(moth_img, (98, 98))
tweezers_img = pygame.image.load("tweezer.png")
tweezers_img = pygame.transform.scale(tweezers_img, (160, 160))

# Moth variables
moth_x = random.randint(10, 1050)
moth_y = 150
moth_y_change = 0.8

# Tweezer variables
tweezers_x = 600
tweezers_y = 800 - 160
tweezers_x_change = 0

# Intro animation variables
intro_x = 90
intro_y = 395
intro_txt_x = -800
intro_txt_y = 75

# Story content
firstStoryImg = pygame.image.load("firstlevelstory.png")


def draw_tweezers(x, y):
    screen.blit(tweezers_img, (x, y))


def draw_moth(x, y):
    screen.blit(moth_img, (x, y))


def check_collision(moth_x, moth_y, tweezers_x, tweezers_y):
    distance = math.sqrt(pow((moth_x - tweezers_x), 2) +
                         pow((moth_y - tweezers_y), 2))
    return distance < 70


def show_lose():
    screen.blit(losing_img, (100, 200))


def show_win():
    screen.blit(winning_img, (100, 200))


def display_story():
    screen.blit(firstStoryImg, (-40, -50))


def intro_animation():
    """Animates the introduction elements."""
    global intro_x, intro_txt_x
    screen.blit(intro_img, (intro_x, intro_y))
    screen.blit(intro_txt, (intro_txt_x, intro_txt_y))


# Game loop
running = True
while running:
    screen.fill((76, 0, 153))  # Background color

    if win and not story_shown:
        # Display the winning image for 5 seconds before showing the story
        if story_timer == 0:
            story_timer = time.time()
        if time.time() - story_timer < 1:
            screen.blit(first_level_img, (-50, -250))
            show_win()

        else:
            display_story()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    story_shown = True
    elif lose:
        screen.blit(first_level_img, (-50, -250))
        show_lose()

    elif not first_level:
        # Intro screen
        screen.blit(intro_back, (0, 0))  # Intro background

        # Animate intro elements
        if intro_x < 880:
            intro_x += 8
            intro_txt_x += 8
        intro_animation()

        # Start the first level with a key press
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                first_level = True
    elif first_level:
        # First level screen
        screen.blit(first_level_img, (-50, -250))

        # Draw objects
        draw_tweezers(tweezers_x, tweezers_y)
        draw_moth(moth_x, moth_y)

        # Move moth
        moth_y += moth_y_change

        # Boundary checks
        tweezers_x += tweezers_x_change
        tweezers_x = max(10, min(tweezers_x, 1050))

        if moth_y >= 700:
            moth_y = random.randint(5, 10)
            moth_x = random.randint(10, 1050)
            debug_chance -= 1

        if debug_chance < 0:
            lose = True

        if moth_caught >= 10:
            win = True

        # Collision detection
        if check_collision(moth_x, moth_y, tweezers_x, tweezers_y):
            moth_y = random.randint(5, 10)
            moth_x = random.randint(10, 1050)
            moth_caught += 1

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                tweezers_x_change = -2
            if event.key == pygame.K_RIGHT:
                tweezers_x_change = 2

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                tweezers_x_change = 0

    pygame.display.update()

pygame.quit()
