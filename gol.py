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

def seed_grid(grid):
    for x in range(10):
        for y in range(10):
            _s = random.randint(0, 100)
            if _s > 65:
                grid[x][y] = 1
            else:
                grid[x][y] = 0
    return grid

def update_grid(grid):
    newgrid = [[0 for x in range(10)] for y in range(10)]
    for x in range(10):
        for y in range(10):
            nr = count_neigh(x, y, grid)
            if grid[x][y]:
                if (nr == 2) or (nr == 3):
                    newgrid[x][y] = 1
                else:
                    newgrid[x][y] = 0
            else:
                if nr == 3:
                    newgrid[x][y] = 1
    return newgrid

def count_neigh(x, y, grid):
    nr = 0
    for xx in range(x-1, x+2):
        for yy in range(y-1, y+2):
            if (xx < 0 or xx > 9) or (yy < 0 or yy > 9):
                pass
            else:
                if (xx == x) and (yy == y):
                    pass
                else:
                    if grid[xx][yy]:
                        nr += 1

    return nr

UPDATEEVENT = pygame.USEREVENT + 1
pygame.time.set_timer(UPDATEEVENT, 500)

grid = [[0 for x in range(10)] for y in range(10)]

grid = seed_grid(grid)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == UPDATEEVENT:
            grid = update_grid(grid)

    screen.fill((0,0,0))
    print_grid(10,10,0,grid)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
