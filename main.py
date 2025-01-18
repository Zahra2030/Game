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

# Game states
INTRO = 0
FIRST_LEVEL = 1
SHOWING_firstSTORY = 2
SECOND_LEVEL = 3
WINNING_NOTIF = 4
LOSING_NOTIF = 5
current_state = INTRO

# Game variables
debug_chance = 5
moth_caught = 0
story_timer = 0
reset = True

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

# First level story images
firstStory_BackImg = pygame.image.load("firstlevelstory.png")
firstStory_TxtImg = pygame.image.load("firstlevelstoryTxt.png")
firstStory_TxtImg_Y = -750
firstStory_TxtImg_Ychange = 15

# Second level images
background = pygame.image.load('SecondLevel.png')
background = pygame.transform.scale(background, (1565, 815))
state_one = pygame.image.load('Clear.png')  # State 1: Clear
state_one = pygame.transform.scale(state_one, (80, 80))
state_two = pygame.image.load('manipulated.png')  # State 2: Manipulated
state_two = pygame.transform.scale(state_two, (80, 80))
state_three = pygame.image.load('Isolated.png')  # State 3: Isolated
state_three = pygame.transform.scale(state_three, (80, 80))

# Node positions and states for the second level
nodesX = [515, 735, 975]
nodesY = [145, 380, 625]
pc_states = [1, 2, 3]  # 1 = Clear, 2 = Manipulated, 3 = Isolated
fixed_states = []

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
    global firstStory_TxtImg_Y
    screen.blit(firstStory_BackImg, (-18, -18))
    screen.blit(firstStory_TxtImg, (5, firstStory_TxtImg_Y))
    if firstStory_TxtImg_Y < 20:
        firstStory_TxtImg_Y += firstStory_TxtImg_Ychange


def intro_animation():
    global intro_x, intro_txt_x
    screen.blit(intro_img, (intro_x, intro_y))
    screen.blit(intro_txt, (intro_txt_x, intro_txt_y))
    if intro_x < 880:
        intro_x += 8
        intro_txt_x += 8


def initialize_nodes():
    global fixed_states
    fixed_states = [
        [nodesX[i], nodesY[j], random.choice(pc_states[:2])]
        for i in range(len(nodesX)) for j in range(len(nodesY))
    ]


def draw_nodes():
    for objX, objY, state in fixed_states:
        if state == 1:
            screen.blit(state_one, (objX, objY))
        elif state == 2:
            screen.blit(state_two, (objX, objY))
        elif state == 3:
            screen.blit(state_three, (objX, objY))


def is_click_on_pc(x, y, objX, objY):
    pc_width, pc_height = state_one.get_size()
    return objX <= x <= objX + pc_width and objY <= y <= objY + pc_height


def isolate(x, y):
    for node in fixed_states:
        objX, objY, state = node
        if is_click_on_pc(x, y, objX, objY) and state == 1:
            node[2] = 3
            break


def clear(x, y):
    for node in fixed_states:
        objX, objY, state = node
        if is_click_on_pc(x, y, objX, objY) and state == 2:
            node[2] = 1
            break


# Main game loop
running = True
while running:
    screen.fill((76, 0, 153))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if current_state == INTRO:
                current_state = FIRST_LEVEL
            elif current_state == SHOWING_firstSTORY:
                current_state = SECOND_LEVEL
            elif current_state == FIRST_LEVEL:
                if event.key == pygame.K_LEFT:
                    tweezers_x_change = -2
                elif event.key == pygame.K_RIGHT:
                    tweezers_x_change = 2

        if event.type == pygame.KEYUP and current_state == FIRST_LEVEL:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                tweezers_x_change = 0

        if event.type == pygame.MOUSEBUTTONDOWN and current_state == SECOND_LEVEL:
            x, y = event.pos
            if event.button == 1:
                isolate(x, y)
            elif event.button == 3:
                clear(x, y)

    if current_state == INTRO:
        screen.blit(intro_back, (0, 0))
        intro_animation()

    elif current_state == FIRST_LEVEL:
        screen.blit(first_level_img, (-50, -250))
        draw_tweezers(tweezers_x, tweezers_y)
        draw_moth(moth_x, moth_y)
        tweezers_x += tweezers_x_change
        moth_y += moth_y_change
        if moth_y >= 700:
            moth_y = random.randint(5, 10)
            moth_x = random.randint(10, 1050)
            debug_chance -= 1
        if debug_chance < 0:
            current_state = LOSING_NOTIF
        if moth_caught >= 10:
            current_state = WINNING_NOTIF
        if check_collision(moth_x, moth_y, tweezers_x, tweezers_y):
            moth_y = random.randint(5, 10)
            moth_x = random.randint(10, 1050)
            moth_caught += 1

    elif current_state == SHOWING_firstSTORY:
        display_story()

    elif current_state == SECOND_LEVEL:
        if reset:
            initialize_nodes()
            reset = False
        screen.blit(background, (-15, -5))
        draw_nodes()

    elif current_state == WINNING_NOTIF:
        if story_timer == 0:
            story_timer = time.time()
        if time.time() - story_timer < 3:
            show_win()
        else:
            current_state = SHOWING_firstSTORY

    elif current_state == LOSING_NOTIF:
        if story_timer == 0:
            story_timer = time.time()
        if time.time() - story_timer < 3:
            show_lose()
        else:
            current_state = INTRO
            debug_chance = 5
            moth_caught = 0

    pygame.display.update()

pygame.quit()
