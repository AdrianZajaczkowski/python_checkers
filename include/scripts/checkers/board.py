import pygame
from .constants import COLORS, ROWS, COLS, SQUARE_SIZE , SQUARE_SIZE
from .piece import Piece

class Board():

    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board() # automaticly call method to create board
    def draw_squares(self,win):
        win.fill(COLORS['RED'])
        for row in range(ROWS):
            for col in range(row % 2, COLS,2):
                pygame.draw.rect(win,COLORS['GREY'], (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col %2 == ((row + 1 ) %2 ):
                    if row < 3:
                        self.board[row].append(Piece(row,col,COLORS['WHITE'])) # append pieces with COLORS on row&col
                    elif row > 4:
                        self.board[row].append(Piece(row,col,COLORS['BLACK']))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self,win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0 :
                    piece.draw(win)
                    