# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 18/03/2020

"""
import unittest

from app.models.board import Cell, Board

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