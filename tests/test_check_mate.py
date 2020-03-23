# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 22/03/2020

"""
import unittest

from app.models.board import Board, Cell
from app.models.pieces import King, Gold_General, Lance, Pawn, Pieces, Knight


class CheckMateTestCase(unittest.TestCase):
    board = Board()

    def setUp(self):
        self.board.shogi_board[8][4].piece = King(King.WHITE)
        self.board.shogi_board[3][4].piece = Lance(Lance.WHITE)
        self.board.shogi_board[2][5].piece = Lance(Lance.WHITE)

        self.board.shogi_board[0][4].piece = King(King.BLACK)
        self.board.shogi_board[0][3].piece = Gold_General(Gold_General.BLACK)
        self.board.shogi_board[6][5].piece = Gold_General(Gold_General.BLACK)
        self.board.shogi_board[7][4].piece = Pawn(Pawn.BLACK)


    def test_check(self):
        self.assertTrue(self.board._check(Pieces.BLACK))
        self.assertTrue(self.board._check(Pieces.WHITE))

    def test_check_mate_white(self):
        if((self.board.shogi_board[0][2].get_piece() is None) | (self.board.shogi_board[0][2].get_piece() is '')):
            self.board.move(self.board.shogi_board[0][3], self.board.shogi_board[0][2])
        self.board.shogi_board[2][3].piece = Pawn(Pawn.WHITE)
        self.board.shogi_board[2][2].piece = Knight(Knight.WHITE)
        self.assertTrue(self.board._check_mate(self.board.shogi_board[3][4]))

    def test_check_mate_black(self):
        self.assertFalse(self.board._check_mate(self.board.shogi_board[7][4]))
        self.assertFalse(self.board._check_mate(self.board.shogi_board[6][5]))

    def test_check_no_mate_white(self):
        if ((self.board.shogi_board[0][2].get_piece() is None) | (self.board.shogi_board[0][2].get_piece() is '')):
            self.board.move(self.board.shogi_board[0][3], self.board.shogi_board[0][2])
        self.board.shogi_board[2][3].piece = ''
        self.board.__str__()
        self.assertFalse(self.board._check_mate(self.board.shogi_board[3][4]))

    def test_check_no_mate_white_corner(self):
        if ((self.board.shogi_board[0][2].get_piece() is None) | (self.board.shogi_board[0][2].get_piece() is '')):
            self.board.move(self.board.shogi_board[0][3], self.board.shogi_board[0][2])
        self.board.shogi_board[2][3].piece = ''
        self.board.shogi_board[1][1].piece = Pawn(Pawn.WHITE)
        self.board.shogi_board[3][0].piece = Lance(Lance.WHITE)
        self.assertFalse(self.board._check_mate(self.board.shogi_board[3][4]))

    def test_check_mate_white_corner(self):
        if ((self.board.shogi_board[0][2].get_piece() is None) | (self.board.shogi_board[0][2].get_piece() is '')):
            self.board.move(self.board.shogi_board[0][3], self.board.shogi_board[0][2])
        self.board.shogi_board[2][3].piece = ''
        self.board.shogi_board[1][1].piece = ''
        self.board.shogi_board[0][4].piece = ''
        self.board.shogi_board[3][0].piece = Lance(Lance.WHITE)
        self.board.shogi_board[2][1].piece = Lance(Lance.WHITE)
        self.board.shogi_board[0][0].piece = King(King.BLACK)
        self.assertTrue(self.board._check_mate(self.board.shogi_board[3][4]))

    def tearDown(self):
        self.board.shogi_board = [[Cell(x, y) for x in range(0, 9)] for y in range(0, 9)]