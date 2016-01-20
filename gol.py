#!/usr/bin/env python2

import sys
import pygame
import random

pygame.init()

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

size = (155,155)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Game of Life")
running = True

clock = pygame.time.Clock()

def print_grid(width, height, margin, grid):
    xpos = ypos = margin
    for x in range(10):
        for y in range(10):
            if grid[x][y]:
                pygame.draw.rect(screen, GREEN, [xpos, ypos, width, height])
            else:
                pygame.draw.rect(screen, WHITE, [xpos, ypos, width, height])
            xpos += width + margin
        else:
            xpos = margin
            ypos += height + margin

def update_grid(grid):
    for x in range(10):
        for y in range(10):
            _s = random.randint(0, 1)
            grid[x][y] = _s
    return grid

UPDATEEVENT = pygame.USEREVENT + 1
pygame.time.set_timer(UPDATEEVENT, 500)

grid = [[0 for x in range(10)] for y in range(10)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == UPDATEEVENT:
            grid = update_grid(grid)

    screen.fill((0,0,0))
    print_grid(10,10,5,grid)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
