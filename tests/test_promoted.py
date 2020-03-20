# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 20/03/2020

"""
import unittest

from app.models.board import Board
from app.models.pieces import Rook


class PromotedPiecesTestCase(unittest.TestCase):
    board = Board()
    def setUp(self):
        self.board.shogi_board[1][7].piece = Rook(Rook.BLACK)
        self.board.shogi_board[7][1].piece = Rook(Rook.WHITE)

    def test_promoted_rook(self):
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][7], self.board.shogi_board[6][7]))
        self.assertTrue(self.board.shogi_board[6][7].piece.promoted)
        self.assertEqual(1, self.board.move(self.board.shogi_board[6][7], self.board.shogi_board[7][6]))

