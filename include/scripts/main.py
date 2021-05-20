#!/usr/bin/env python3
import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board
FPS = 60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Checkers')

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    while run:
        clock.tick(FPS)

        for event in pygame.event.get(): # check what event is arledy 
            if event.type == pygame.QUIT: # event for quit loop while you press 'x'
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw(WIN)
        pygame.display.update()

    pygame.quit() # end game

main()