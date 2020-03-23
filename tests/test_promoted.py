# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 20/03/2020

"""
import unittest

from app.models.board import Board, Cell
from app.models.pieces import Rook, Knight, King


class PromotedPiecesTestCase(unittest.TestCase):
    board = Board()
    def setUp(self):
        self.board.shogi_board[1][7].piece = Rook(Rook.BLACK)
        self.board.shogi_board[7][1].piece = Rook(Rook.WHITE)
        self.board.shogi_board[0][7].piece = Knight(Knight.BLACK)
        self.board.shogi_board[0][1].piece = Knight(Knight.BLACK)
        self.board.shogi_board[8][7].piece = Knight(Knight.WHITE)
        self.board.shogi_board[8][1].piece = Knight(Knight.WHITE)
        self.board.shogi_board[0][4].piece = King(King.BLACK)
        self.board.shogi_board[8][8].piece = King(King.WHITE)

    def test_promoted_rook(self):
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][7], self.board.shogi_board[6][7]))
        self.assertTrue(self.board.shogi_board[6][7].piece.promoted)
        self.assertEqual(1, self.board.move(self.board.shogi_board[6][7], self.board.shogi_board[7][6]))

    def test_promoted_move_possible_initial_board(self):
        self.board.shogi_board[0][7].piece.set_promoted()
        self.board.shogi_board[0][1].piece.set_promoted()
        self.board.shogi_board[8][7].piece.set_promoted()
        self.board.shogi_board[8][1].piece.set_promoted()

        self.assertTrue(self.board.shogi_board[0][1].piece.promoted)
        self.assertTrue(self.board.shogi_board[0][7].piece.promoted)
        self.assertTrue(self.board.shogi_board[8][1].piece.promoted)
        self.assertTrue(self.board.shogi_board[8][7].piece.promoted)

        # Black Knights
        self.assertEqual(1, self.board.move(self.board.shogi_board[0][1], self.board.shogi_board[1][1]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][1], self.board.shogi_board[2][2]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][2], self.board.shogi_board[2][1]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[2][1], self.board.shogi_board[1][2]))

        self.assertEqual(1, self.board.move(self.board.shogi_board[0][7], self.board.shogi_board[0][6]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[0][6], self.board.shogi_board[1][5]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][5], self.board.shogi_board[2][4]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][4], self.board.shogi_board[1][4]))


        # White Knights
        self.assertEqual(1, self.board.move(self.board.shogi_board[8][1], self.board.shogi_board[8][2]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[8][2], self.board.shogi_board[8][3]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[8][3], self.board.shogi_board[7][3]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][3], self.board.shogi_board[6][4]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[6][4], self.board.shogi_board[6][5]))

        self.assertEqual(1, self.board.move(self.board.shogi_board[8][7], self.board.shogi_board[8][6]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[8][6], self.board.shogi_board[8][5]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[8][5], self.board.shogi_board[7][4]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[7][4], self.board.shogi_board[8][3]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][4], self.board.shogi_board[8][4]))

    def tearDown(self):
        self.board.shogi_board = [[Cell(x, y) for x in range(0, 9)] for y in range(0, 9)]

