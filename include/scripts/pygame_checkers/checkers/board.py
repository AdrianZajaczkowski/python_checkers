import pygame
from .constants import COLORS, ROWS, COLS, SQUARE_SIZE
from .piece import Piece


class Board:

    def __init__(self):
        self.board = []
        self.black_left = self.white_left = 12
        self.black_kings = self.white_kings = 0
        self.create_board()  # automaticly call method to create board

    def draw_squares(self, win):
        win.fill(COLORS['GREY'])
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(
                    win, COLORS['L_GREEN'], (row*SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        # append pieces with COLORS on row&col
                        self.board[row].append(
                            Piece(row, col, COLORS['WHITE']))
                    elif row > 4:
                        self.board[row].append(
                            Piece(row, col, COLORS['BLACK']))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def move_pieces(self, piece, row, col):
        # swap pos values of pieces to make it move
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == 'WHITE':
                self.white_kings += 1
            else:
                self.black_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        if piece.color == COLORS['BLACK'] or piece.king:
            # row-1 start above current row, max(row -3,-1) check 2 pieces away from start or one
            moves.update(self._traverse_left(
                row - 1, max(row - 3, -1), -1, piece.color, left))
            # right is for the right direction
            moves.update(self._traverse_right(
                row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == COLORS['WHITE'] or piece.king:
            moves.update(self._traverse_left(
                row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(
                row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == COLORS['BLACK']:
                    self.black_left -= 1
                else:
                    self.white_left -= 1

    def winner(self):
        if self.black_left <= 0:
            return COLORS['WHITE']
        elif self.white_left <= 0:
            return COLORS['BLACK']

        return None

    # step -> can go up diagonal or down diagonal
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:  # found empty square
                if skipped and not last:  # if we skip piece and have blank square and we cant skip again over piece
                    break
                elif skipped:  # if we skip and find another place to skip over
                    # update move to last + skipped move
                    moves[(r, left)] = last+skipped
                else:
                    # if we didnt skip anything we had valid move
                    moves[(r, left)] = last

                if last:  # we can jump over enemy piece but how much times?
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    # again jump until we stop getting empty space above enemy piece
                    moves.update(self._traverse_left(
                        r+step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(
                        r+step, row, step, color, left+1, skipped=last))
                break
            elif current.color == color:  # if we find piece with our color
                break  # no moves
            else:
                last = [current]  # chance to jump over enemy piece

            left -= 1
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            current = self.board[r][right]
            if current == 0:  # found empty square
                if skipped and not last:  # if we skip piece and have blank square and we cant skip again over piece
                    break
                elif skipped:  # if we skip and find another place to skip over
                    # update move to last + skipped move
                    moves[(r, right)] = last+skipped
                else:
                    # if we didnt skip anything we had valid move
                    moves[(r, right)] = last

                if last:  # we can jump over enemy piece but how much times?
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    # again jump until we stop getting empty space above enemy piece
                    moves.update(self._traverse_left(
                        r+step, row, step, color, right-1, skipped=last))
                    moves.update(self._traverse_right(
                        r+step, row, step, color, right+1, skipped=last))
                break
            elif current.color == color:  # if we find piece with our color
                break  # no moves
            else:
                last = [current]  # chance to jump over enemy piece

            right += 1
        return moves
