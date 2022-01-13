# Full Stack Bootcamp - Unit 01 Lab 16
# Justin Hammond, 01/12/2022

'''
Mini Capstone
For your final Python project, build a program that solves a problem or
accomplishes a task. Your program needs to utilize an external library
(not part of the Python standard library -- this needs to be something
that you pip install).

The functionality of the program is up to you -- use this as an
opportunity to get creative. Sometimes students explore an idea they
want to use for their capstone project or solve an actual problem they
have. For a list of Python libraries to consider using in this project,
check out https://awesome-python.com
'''
import pygame
from Player import *
from GameBoard import *


# Initialize pygame library
pygame.init()

# Setup display window
screenWidth = 640
screenHeight = 480
screenSize = (screenWidth, screenHeight)
display = pygame.display.set_mode(screenSize)
title = 'Tic-Tac-Toe'
pygame.display.set_caption(title)

# Background display and color
backgroundColor = (255, 127, 64)
background = pygame.Surface(screenSize)
background.fill(backgroundColor)
background = background.convert()
display.blit(background, (0, 0))

# Setup clock
fps = 60
frameTime = 0
clock = pygame.time.Clock()

# Main game loop
isRunning = True
while isRunning:
    # Check for input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

    # Count up frame time and tick the clock no more than 60fps
    frameTime += clock.tick(fps)

    # Update FPS in titlebar
    text = f'{title}    FPS: {clock.get_fps()}'
    pygame.display.set_caption(text)

    # Swap display buffers
    pygame.display.flip()

pygame.quit()

