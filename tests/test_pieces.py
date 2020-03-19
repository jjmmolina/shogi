# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 18/03/2020

"""
import unittest

from app.models.board import Cell, Board
from app.models.pieces import Rook, Bishop


class PiecesTest():
    board = Board()
    board.initialize_board()

class PawnTestCase(unittest.TestCase, PiecesTest):

    def test_move_possible_initial_board(self):
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][8], self.board.shogi_board[3][8]))

    def test_move_not_possible(self):
        self.assertEqual(0, self.board.move(self.board.shogi_board[2][8], self.board.shogi_board[5][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[2][8], self.board.shogi_board[1][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[2][8], self.board.shogi_board[2][7]))

class KingTestCase(unittest.TestCase, PiecesTest):

    def test_move_possible_initial_board(self):
        self.assertEqual(1, self.board.move(self.board.shogi_board[0][4], self.board.shogi_board[1][4]))

    def test_move_not_possible(self):
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][4], self.board.shogi_board[5][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][4], self.board.shogi_board[1][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][4], self.board.shogi_board[2][7]))

class Gold_GeneralTestCase(unittest.TestCase, PiecesTest):

    def test_move_possible_initial_board(self):
        # Black Gold General
        self.assertEqual(1, self.board.move(self.board.shogi_board[0][3], self.board.shogi_board[1][3]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][3], self.board.shogi_board[1][2]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][2], self.board.shogi_board[1][3]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][3], self.board.shogi_board[0][3]))

        self.assertEqual(1, self.board.move(self.board.shogi_board[0][5], self.board.shogi_board[1][5]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][5], self.board.shogi_board[1][6]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][6], self.board.shogi_board[1][5]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][5], self.board.shogi_board[0][5]))

        # White Gold General
        self.assertEqual(0, self.board.move(self.board.shogi_board[8][3], self.board.shogi_board[8][3]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[8][3], self.board.shogi_board[7][3]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][3], self.board.shogi_board[7][2]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][2], self.board.shogi_board[7][3]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][3], self.board.shogi_board[8][3]))

        self.assertEqual(0, self.board.move(self.board.shogi_board[8][5], self.board.shogi_board[8][5]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[8][5], self.board.shogi_board[7][5]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][5], self.board.shogi_board[7][6]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][6], self.board.shogi_board[7][5]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][5], self.board.shogi_board[8][5]))

    def test_move_not_possible(self):
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][3], self.board.shogi_board[0][4]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][3], self.board.shogi_board[1][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][3], self.board.shogi_board[2][7]))

        self.assertEqual(0, self.board.move(self.board.shogi_board[0][5], self.board.shogi_board[0][6]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][5], self.board.shogi_board[1][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][5], self.board.shogi_board[0][8]))

        self.assertEqual(0, self.board.move(self.board.shogi_board[8][3], self.board.shogi_board[8][2]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[8][3], self.board.shogi_board[7][4]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[8][3], self.board.shogi_board[3][2]))

        self.assertEqual(0, self.board.move(self.board.shogi_board[8][5], self.board.shogi_board[8][6]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[8][5], self.board.shogi_board[0][6]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[8][5], self.board.shogi_board[8][3]))

class RookTestCase(unittest.TestCase, PiecesTest):
    board = Board()
    def setUp(self):
        self.board.shogi_board[1][7].piece = Rook(Rook.BLACK)
        self.board.shogi_board[7][1].piece = Rook(Rook.WHITE)

    def test_move_possible_initial_board(self):
        # Black Rook
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][7], self.board.shogi_board[1][2]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][2], self.board.shogi_board[5][2]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[5][2], self.board.shogi_board[5][8]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[5][8], self.board.shogi_board[5][2]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[5][2], self.board.shogi_board[1][2]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][2], self.board.shogi_board[1][7]))

        # White Rook
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][1], self.board.shogi_board[1][1]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][1], self.board.shogi_board[1][5]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][5], self.board.shogi_board[6][5]))


    def test_promoted_move_possible_initial_board(self):
        self.board.shogi_board[1][7].piece.set_promoted()
        self.board.shogi_board[7][1].piece.set_promoted()
        # Black Rook
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][7], self.board.shogi_board[1][2]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][2], self.board.shogi_board[5][2]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[5][2], self.board.shogi_board[5][8]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[5][8], self.board.shogi_board[1][8]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][8], self.board.shogi_board[1][7]))

        self.assertEqual(1, self.board.move(self.board.shogi_board[1][7], self.board.shogi_board[2][6]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][6], self.board.shogi_board[3][7]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[3][7], self.board.shogi_board[0][7]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[0][7], self.board.shogi_board[1][8]))

        # White Rook
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][1], self.board.shogi_board[1][1]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][1], self.board.shogi_board[1][5]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][5], self.board.shogi_board[6][5]))

    def test_move_not_possible(self):
        self.assertEqual(0, self.board.move(self.board.shogi_board[1][7], self.board.shogi_board[2][4]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[1][7], self.board.shogi_board[0][6]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[1][7], self.board.shogi_board[1][7]))

        self.assertEqual(0, self.board.move(self.board.shogi_board[7][1], self.board.shogi_board[8][2]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[7][1], self.board.shogi_board[6][0]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[7][1], self.board.shogi_board[1][7]))

    def tearDown(self):
        self.board.shogi_board = [[Cell(x, y) for x in range(0, 9)] for y in range(0, 9)]

class BishopTestCase(unittest.TestCase, PiecesTest):
    board = Board()
    def setUp(self):
        self.board.shogi_board[1][1].piece = Bishop(Bishop.BLACK)
        self.board.shogi_board[7][7].piece = Bishop(Bishop.WHITE)

    def test_move_possible_initial_board(self):
        # Black Bishop
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][1], self.board.shogi_board[2][0]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][0], self.board.shogi_board[7][4]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][4], self.board.shogi_board[3][8]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[3][8], self.board.shogi_board[0][5]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[0][5], self.board.shogi_board[3][3]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[3][3], self.board.shogi_board[1][1]))

        # White Bishop
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][7], self.board.shogi_board[8][6]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[8][6], self.board.shogi_board[2][0]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][0], self.board.shogi_board[1][1]))


    def test_promoted_move_possible_initial_board(self):
        self.board.shogi_board[1][1].piece.set_promoted()
        self.board.shogi_board[7][7].piece.set_promoted()
        # Black Bishop
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][1], self.board.shogi_board[2][0]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][0], self.board.shogi_board[7][4]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][4], self.board.shogi_board[3][8]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[3][8], self.board.shogi_board[2][8]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][8], self.board.shogi_board[2][7]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][7], self.board.shogi_board[0][5]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[0][5], self.board.shogi_board[3][2]))

        # White Bishop
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][7], self.board.shogi_board[8][6]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[8][6], self.board.shogi_board[2][0]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][0], self.board.shogi_board[3][0]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[3][0], self.board.shogi_board[4][0]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[4][0], self.board.shogi_board[4][1]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[4][1], self.board.shogi_board[3][1]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[3][1], self.board.shogi_board[7][4]))

    def test_move_not_possible(self):
        self.assertEqual(0, self.board.move(self.board.shogi_board[1][1], self.board.shogi_board[2][4]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[1][1], self.board.shogi_board[5][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[1][1], self.board.shogi_board[0][1]))

        self.assertEqual(0, self.board.move(self.board.shogi_board[7][7], self.board.shogi_board[6][7]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[7][7], self.board.shogi_board[8][7]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[7][7], self.board.shogi_board[7][8]))

    def tearDown(self):
        self.board.shogi_board = [[Cell(x, y) for x in range(0, 9)] for y in range(0, 9)]