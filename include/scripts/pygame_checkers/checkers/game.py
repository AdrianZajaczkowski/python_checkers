import pygame
from .constants import COLORS ,SQUARE_SIZE
from .board import Board 


class Game:
    def __init__(self,win):
        self._init()
        self.win = win
    
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self): #private methood to initialize game 
        self.selected = None
        self.board = Board()
        self.turn = COLORS['WHITE'] # current valid moves from player
        self.valid_moves = {}

    def reset(self):
        self._init()

    def select(self,row,col):
        if self.selected: 
            result = self._move(row,col) # try to move piece what we selected
            if not result:
                self.selected = None # clear select 
                self.select(row,col) # reselect new piece

        piece = self.board.get_piece(row,col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def winner(self):
        return self.board.winner()
        
    def _move(self,row,col):
        piece = self.board.get_piece(row,col)
        if self.selected and piece == 0 and (row,col) in self.valid_moves:
            self.board.move_pieces(self.selected,row,col)
            skipped = self.valid_moves[(row,col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True

    def draw_valid_moves(self,moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, COLORS['BLUE'], (col* SQUARE_SIZE+ SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), int(SQUARE_SIZE//4) )
   
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == COLORS['WHITE']:
            self.turn = COLORS['BLACK']
        else:
            self.turn = COLORS['WHITE']

