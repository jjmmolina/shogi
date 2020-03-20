# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 17/03/2020

"""
from app.models.pieces import Pawn, King, Rook, Gold_General, Silver_General, Knight, Lance, Bishop
from pandas import *


class Cell():
    """ Class represent a cell of the board"""
    def __init__(self, x, y, piece=None):
        self.x = x
        self.y = y
        self.piece = piece

    def get_piece(self):
        return self.piece
    def set_piece(self, piece=None):
        if piece:
            self.piece = piece
        else:
            self.piece = ''

    def is_available_for_me(self, color):
        if (self.get_piece() is not None) & (self.get_piece() is not ''):
            if(self.get_piece().color == color):
                return False
        return True

    def piece_color(self):
        if (self.get_piece() is not None):
            return self.get_piece().color

    def __str__(self):
        if(self.get_piece() is not None):
            return f'{self.get_piece()}'
        else:
            return f' '





class Board():
    def __init__(self):
        self.shogi_board = [[Cell(x, y) for x in range(0, 9)] for y in range(0, 9)]
        self.captured_player_black = []
        self.captured_player_white = []

    def initialize_board(self):
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

        self.shogi_board[1][1].piece = Bishop(Bishop.BLACK)
        self.shogi_board[7][7].piece = Bishop(Bishop.WHITE)

        self.shogi_board[1][7].piece = Rook(Rook.BLACK)
        self.shogi_board[7][1].piece = Rook(Rook.WHITE)

        for p in range(9):
            self.shogi_board[2][p].piece = Pawn(Pawn.BLACK)
            self.shogi_board[6][p].piece = Pawn(Pawn.WHITE)


    def __str__(self):
        print(DataFrame(self.shogi_board))

    def _check_mate(color):
        pass

    def _check(color):
        pass

    def move(self, cell_from, cell_to):
        piece = cell_from.get_piece()
        if not piece.captured:
            if piece.is_my_movement(cell_from, cell_to):
                # Check if destination is available for my color
                if (cell_to.is_available_for_me(piece.color)):
                    if ((cell_to.get_piece() is not None) & (cell_to.get_piece() is not '')):
                        piece_captured = cell_to.get_piece()
                        piece_captured.set_captured()
                        if (piece_captured.color is 'B'):
                            self.captured_player_white.append(piece_captured)
                        else:
                            self.captured_player_black.append(piece_captured)
                        print(f'Piece {piece_captured.__str__()} captured by piece {piece.__str__()}')
                    print(f'Moving piece {piece.name} from {cell_from.y, cell_from.x} to {cell_to.y, cell_to.x}')
                    if not piece.promoted:
                        if(((piece.color is 'W') &(cell_to.y <= 2)) | ((piece.color is 'B') & (cell_to.y >= 6))):
                                piece.set_promoted()
                                print(f'Piece {cell_from.piece.name} has been promoted!!')
                    self.shogi_board[cell_to.y][cell_to.x].set_piece(piece)
                    self.shogi_board[cell_from.y][cell_from.x].set_piece()
                    #TODO comprobar si hay jaque o jaquemate
                    if(self._check(piece.color)):
                        print(f'Check by piece {piece.__str__()}')
                    if(self._check_mate()):
                        print(f'Checkmate by piece {piece.__str__()}. Team {piece.color} WIN!!!!')

                    # self.__str__()
                    return 1
                else:
                    print(f'Movement not possible for piece {cell_from.piece} because destination cell is ocuped by other piece of my colour')
                    return 0
            else:
                print(f'Movement not possible for piece {cell_from.piece}')
                return 0
        else:
            print(f'Movement not possible for piece {cell_from.piece} because it is captured')
        return 0

