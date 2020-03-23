# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 23/03/2020

"""
import unittest

from app.models.board import Board, Cell
from app.models.pieces import King, Gold_General, Lance, Pawn, Pieces, Knight


class ReintroduceTestCase(unittest.TestCase):
    board = Board()

    def setUp(self):
        self.board.shogi_board[8][4].piece = King(King.WHITE)
        self.board.shogi_board[3][4].piece = Lance(Lance.WHITE)
        self.board.shogi_board[2][5].piece = Lance(Lance.WHITE)
        self.board.shogi_board[7][7].piece = Knight(Knight.WHITE)
        piece_captured = self.board.shogi_board[2][5].get_piece()
        piece_captured.set_captured()
        self.board.captured_player_black.append(piece_captured)

        piece_captured = self.board.shogi_board[7][7].get_piece()
        piece_captured.set_captured()
        self.board.captured_player_black.append(piece_captured)

        self.board.shogi_board[0][4].piece = King(King.BLACK)
        self.board.shogi_board[0][3].piece = Gold_General(Gold_General.BLACK)
        self.board.shogi_board[6][5].piece = Gold_General(Gold_General.BLACK)
        self.board.shogi_board[7][4].piece = Pawn(Pawn.WHITE)
        self.board.shogi_board[7][5].piece = Pawn(Pawn.BLACK)

        piece_captured = self.board.shogi_board[6][5].get_piece()
        piece_captured.set_captured()
        self.board.captured_player_white.append(piece_captured)

        piece_captured = self.board.shogi_board[7][5].get_piece()
        piece_captured.set_captured()
        self.board.captured_player_white.append(piece_captured)


    def test_reintroduce_piece(self):
        piece = self.board.captured_player_white[0]
        piece._change_color()
        self.assertTrue(self.board.re_introduce_piece(piece, self.board.shogi_board[5][4]))
        self.board.captured_player_white.pop(0)

        piece = self.board.captured_player_white[0]
        piece._change_color()
        self.assertFalse(self.board.re_introduce_piece(piece, self.board.shogi_board[6][4]))
        self.board.shogi_board[7][4].get_piece().set_promoted()
        self.assertFalse(self.board.re_introduce_piece(piece, self.board.shogi_board[0][4]))
        self.assertTrue(self.board.re_introduce_piece(piece, self.board.shogi_board[6][4]))

        piece = self.board.captured_player_black[0]
        piece._change_color()
        self.assertFalse(self.board.re_introduce_piece(piece, self.board.shogi_board[0][4]))
        self.board.captured_player_black.pop(0)

        piece = self.board.captured_player_black[0]
        piece._change_color()
        self.assertFalse(self.board.re_introduce_piece(piece, self.board.shogi_board[1][6]))



    def tearDown(self):
        self.board.captured_player_black = []
        self.board.captured_player_white = []
        self.board.shogi_board = [[Cell(x, y) for x in range(0, 9)] for y in range(0, 9)]