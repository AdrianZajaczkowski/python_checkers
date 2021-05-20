#!/usr/bin/env python3
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, COLORS
from checkers.board import Board 
from checkers.game import Game
FPS = 60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Checkers')

def catch_piece(pos):
    x, y = pos 
    row = y // SQUARE_SIZE 
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    
    while run:
        clock.tick(FPS)

        for event in pygame.event.get(): # check what event is arledy 
            if event.type == pygame.QUIT: # event for quit loop while you press 'x'
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = catch_piece(pos)
                game.select(row,col)
            
        game.update()

    pygame.quit() # end game

main()