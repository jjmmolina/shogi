# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 17/03/2020

"""
from models.pieces import Pawn, King, Rook, Gold_General, Silver_General, Knight, Lance, Bisop
from pandas import *


class Cell():
    """ Class represent a cell of the board"""
    def __init__(self, x, y, piece=None):
        self.x = x
        self.y = y
        self.piece = piece #if piece is not None else set()

    def get_piece(self):
        return self.piece
    def set_piece(self, piece):
        self.piece = piece

    def __str__(self):
        if(self.get_piece() is not None):
            # return f'Piece {self.get_piece()}, Position{ self.x, self.y}'
            return f'{self.get_piece()}'
        else:
            return f' '

class Board():
    shogi_board = [[Cell(x,y) for x in range(9)] for y in range(9)]

    def __init__(self):
        self.shogi_board[0][4].piece = King(King.BLACK)
        self.shogi_board[8][4].piece = King(King.WHITE)

        self.shogi_board[0][5].piece = Gold_General(Gold_General.BLACK)
        self.shogi_board[0][3].piece = Gold_General(Gold_General.BLACK)
        self.shogi_board[8][5].piece = Gold_General(Gold_General.WHITE)
        self.shogi_board[8][3].piece = Gold_General(Gold_General.WHITE)

        self.shogi_board[0][2].piece = Silver_General(Silver_General.BLACK)
        self.shogi_board[0][6].piece = Silver_General(Silver_General.BLACK)
        self.shogi_board[8][2].piece = Silver_General(Silver_General.WHITE)
        self.shogi_board[8][6].piece = Silver_General(Silver_General.WHITE)

        self.shogi_board[0][7].piece = Knight(Knight.BLACK)
        self.shogi_board[0][1].piece = Knight(Knight.BLACK)
        self.shogi_board[8][7].piece = Knight(Knight.WHITE)
        self.shogi_board[8][1].piece = Knight(Knight.WHITE)

        self.shogi_board[0][0].piece = Lance(Lance.BLACK)
        self.shogi_board[0][8].piece = Lance(Lance.BLACK)
        self.shogi_board[8][0].piece = Lance(Lance.WHITE)
        self.shogi_board[8][8].piece = Lance(Lance.WHITE)

        self.shogi_board[1][1].piece = Bisop(Bisop.BLACK)
        self.shogi_board[7][7].piece = Bisop(Bisop.WHITE)

        self.shogi_board[1][7].piece = Rook(Rook.BLACK)
        self.shogi_board[7][1].piece = Rook(Rook.WHITE)

        for p in range(9):
            self.shogi_board[2][p].piece = Pawn(Pawn.BLACK)
            self.shogi_board[6][p].piece = Pawn(Pawn.WHITE)

    def __str__(self):
        print(DataFrame(self.shogi_board))


