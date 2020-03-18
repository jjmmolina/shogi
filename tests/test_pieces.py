# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 18/03/2020

"""
import unittest

from app.models.board import Cell, Board


class PawnTestCase(unittest.TestCase):
    board = Board()
    board.initialize_board()

    def test_move_possible(self):
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][8], self.board.shogi_board[3][8]))

    def test_move_not_possible(self):
        self.assertEqual(0, self.board.move(self.board.shogi_board[2][8], self.board.shogi_board[5][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[2][8], self.board.shogi_board[1][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[2][8], self.board.shogi_board[2][7]))

class KingTestCase(unittest.TestCase):
    board = Board()
    board.initialize_board()

    def test_move_possible(self):
        self.assertEqual(1, self.board.move(self.board.shogi_board[0][4], self.board.shogi_board[1][4]))

    def test_move_not_possible(self):
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][4], self.board.shogi_board[5][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][4], self.board.shogi_board[1][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][4], self.board.shogi_board[2][7]))