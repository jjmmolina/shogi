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

    def _get_king_white(self):
        for rows in self.shogi_board:
            for element in rows:
                if ((element.get_piece() is not None) & (element.get_piece() is not '')):
                    if ((element.piece.name == 'K') & (element.piece.color == 'W')):
                        return element

    def _get_king_black(self):
        for rows in self.shogi_board:
            for element in rows:
                if ((element.get_piece() is not None) & (element.get_piece() is not '')):
                    if ((element.piece.name == 'K') & (element.piece.color == 'B')):
                       return element

    def _get_cells_around_king(self, y, x):
        matrix = self.shogi_board
        result = []
        if y > 0:
            result.append(matrix[y - 1][x])
            if x > 0:
                result.append(matrix[y - 1][x - 1])
            if x < 8:
                result.append(matrix[y - 1][x + 1])
        if x < 8:
            result.append(matrix[y][x + 1])
        if x > 0:
            result.append(matrix[y][x - 1])
        if y < 8:
            result.append(matrix[y + 1][x])
            if x > 0:
                result.append(matrix[y + 1][x - 1])
            if x < 8:
                result.append(matrix[y + 1][x + 1])
        return result

    def _check_mate(self, cell_from):
        if cell_from.get_piece().color is 'B':
            cell_k = self._get_king_white()
        else:
            cell_k = self._get_king_black()

        cells_around_king = self._get_cells_around_king(cell_k.y, cell_k.x)
        check_mate = False
        mov_enemy=False
        # Can the king move to other cell?
        adding_mov_enemy = 0
        adding_mov_friend = 0
        adding_mov_king = 0
        for adjacent in cells_around_king:
            # Si el rey se puede mover a esa celda adyacente
            if (cell_k.get_piece().is_my_movement(cell_k, adjacent)):
                adding_mov_king+=1
                # Pero alguna pieza enemiga puede llegar a esa celda adyacente
                for cells in self.shogi_board:
                    for element in cells:
                        if ((element.get_piece() is not None) & (element.get_piece() is not '')):
                            # Cojo las piezas del equipo que está atacando
                            if (element.get_piece().color == cell_from.get_piece().color):
                                piece_attacker_team = element.get_piece()
                                #Si algún enemigo se puede mover a esa celda adyacente
                                if piece_attacker_team.is_my_movement(element, adjacent):  # Si el enemigo se puede mover a la celda
                                    adding_mov_enemy += 1
                                    mov_enemy = True
                            # Cojo las piezas del equipo que está defendiendo
                            if ((element.get_piece().color != cell_from.get_piece().color) &(element.get_piece().name is not 'K')):
                                piece_my_team = element.get_piece()
                                # Si algún amigo se puede mover a esa celda adyacente
                                if piece_my_team.is_my_movement(element, adjacent):
                                    adding_mov_friend += 1
                                    mov_friend = True

        if (adding_mov_king == 0):
            return True
        else:
            if ((adding_mov_enemy>adding_mov_friend) & (adding_mov_enemy>=adding_mov_king)):
                return True
            elif (adding_mov_enemy<=adding_mov_friend):
                return False
        return False


    def _check(self,color):
        if color is 'B':
            cell_k = self._get_king_white()
        else:
            cell_k = self._get_king_black()
        for cells in self.shogi_board:
           for element in cells:
               if ((element.get_piece() is not None) & (element.get_piece() is not '')):
                    if(element.get_piece().color == color):
                        piece = element.get_piece()
                        check = piece.is_my_movement(element, cell_k)
                        if check:
                            return True
        return False

    def move(self, cell_from, cell_to):
        piece = cell_from.get_piece()
        if not piece.captured:
            if piece.is_my_movement(cell_from, cell_to):
                # Check if destination is available for my color
                if (cell_to.is_available_for_me(piece.color)):
                    if ((cell_to.get_piece() is not None) & (cell_to.get_piece() is not '')):
                        if (self._check(piece.color)):
                            print(f'Check by piece {piece.__str__()}')
                        if (self._check_mate(cell_from)):
                            print(f'Checkmate by piece {piece.__str__()}. Team {piece.color} WIN!!!!')
                        piece_captured = cell_to.get_piece()
                        piece_captured.set_captured()
                        if (piece_captured.color is 'B'):
                            self.captured_player_white.append(piece_captured)
                        else:
                            self.captured_player_black.append(piece_captured)
                        print(f'Piece {piece_captured.__str__()} captured by piece {piece.__str__()}')
                        if (piece_captured.name == 'K'):
                            print(f'Checkmate by piece {piece.__str__()}. Team {piece.color} WIN!!!!')
                    print(f'Moving piece {piece.name} from {cell_from.y, cell_from.x} to {cell_to.y, cell_to.x}')
                    if not piece.promoted:
                        if(((piece.color is 'W') &(cell_to.y <= 2)) | ((piece.color is 'B') & (cell_to.y >= 6))):
                                piece.set_promoted()
                                print(f'Piece {cell_from.piece.name} has been promoted!!')
                    self.shogi_board[cell_to.y][cell_to.x].set_piece(piece)
                    self.shogi_board[cell_from.y][cell_from.x].set_piece()
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

