# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 18/03/2020

"""
import unittest

from app.models.board import Cell, Board
from app.models.pieces import Rook, Bishop, Lance, Silver_General, Knight, King, Pawn, Gold_General
class CheckMateTestCase(unittest.TestCase):
    board = Board()
    board.shogi_board[0][4].piece = King(King.BLACK)
    board.shogi_board[0][5].piece = King(King.WHITE)

    def test_check(self):
        self.assertEqual(1, self.board.move(self.board.shogi_board[0][4], self.board.shogi_board[0][5]))

    def test_check_mate(self):
        pass

class PawnTestCase(unittest.TestCase):
    board = Board()

    def setUp(self):
        self.board.shogi_board[2][8].piece = Pawn(Pawn.BLACK)

    def test_move_possible_initial_board(self):
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][8], self.board.shogi_board[3][8]))

    def test_move_not_possible(self):
        self.assertEqual(0, self.board.move(self.board.shogi_board[2][8], self.board.shogi_board[5][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[2][8], self.board.shogi_board[1][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[2][8], self.board.shogi_board[2][7]))

    def test_promoted_move_possible_initial_board(self):
        self.board.shogi_board[2][8].piece.set_promoted()
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][8], self.board.shogi_board[3][7]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[3][7], self.board.shogi_board[3][6]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[3][6], self.board.shogi_board[4][5]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[4][5], self.board.shogi_board[3][5]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[3][5], self.board.shogi_board[4][6]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[4][6], self.board.shogi_board[3][5]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[4][6], self.board.shogi_board[3][7]))

    def tearDown(self):
        self.board.shogi_board = [[Cell(x, y) for x in range(0, 9)] for y in range(0, 9)]

class KingTestCase(unittest.TestCase):
    board = Board()

    def setUp(self):
        self.board.shogi_board[0][4].piece = King(King.BLACK)
        self.board.shogi_board[8][4].piece = King(King.WHITE)

    def test_move_possible_initial_board(self):
        self.assertEqual(1, self.board.move(self.board.shogi_board[0][4], self.board.shogi_board[1][4]))

    def test_move_not_possible(self):
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][4], self.board.shogi_board[5][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][4], self.board.shogi_board[1][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][4], self.board.shogi_board[2][7]))

    def tearDown(self):
        self.board.shogi_board = [[Cell(x, y) for x in range(0, 9)] for y in range(0, 9)]

class Gold_GeneralTestCase(unittest.TestCase):
    board = Board()

    def setUp(self):
        self.board.shogi_board[0][5].piece = Gold_General(Gold_General.BLACK)
        self.board.shogi_board[0][3].piece = Gold_General(Gold_General.BLACK)
        self.board.shogi_board[8][5].piece = Gold_General(Gold_General.WHITE)
        self.board.shogi_board[8][3].piece = Gold_General(Gold_General.WHITE)

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
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][3], self.board.shogi_board[0][5]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][3], self.board.shogi_board[1][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][3], self.board.shogi_board[2][7]))

        self.assertEqual(0, self.board.move(self.board.shogi_board[0][5], self.board.shogi_board[0][7]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][5], self.board.shogi_board[1][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][5], self.board.shogi_board[0][8]))

        self.assertEqual(0, self.board.move(self.board.shogi_board[8][3], self.board.shogi_board[8][1]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[8][3], self.board.shogi_board[6][4]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[8][3], self.board.shogi_board[3][2]))

        self.assertEqual(0, self.board.move(self.board.shogi_board[8][5], self.board.shogi_board[8][7]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[8][5], self.board.shogi_board[0][6]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[8][5], self.board.shogi_board[8][3]))

    def tearDown(self):
        self.board.shogi_board = [[Cell(x, y) for x in range(0, 9)] for y in range(0, 9)]

class RookTestCase(unittest.TestCase):
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

class BishopTestCase(unittest.TestCase):
    board = Board()
    def setUp(self):
        self.board.shogi_board[1][1].piece = Bishop(Bishop.BLACK)
        self.board.shogi_board[7][7].piece = Bishop(Bishop.WHITE)

    def test_move_possible_initial_board(self):
        # Black Bishop
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][1], self.board.shogi_board[2][0]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][0], self.board.shogi_board[6][4]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[6][4], self.board.shogi_board[3][7]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[3][7], self.board.shogi_board[0][4]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[0][4], self.board.shogi_board[3][1]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[3][1], self.board.shogi_board[1][3]))

        # White Bishop
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][7], self.board.shogi_board[8][6]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[8][6], self.board.shogi_board[2][0]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][0], self.board.shogi_board[1][1]))


    def test_promoted_move_possible_initial_board(self):
        self.board.shogi_board[1][1].piece.set_promoted()
        self.board.shogi_board[7][7].piece.set_promoted()
        # Black Bishop
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][1], self.board.shogi_board[2][0]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][0], self.board.shogi_board[6][4]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[6][4], self.board.shogi_board[3][7]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[3][7], self.board.shogi_board[2][8]))
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
        self.assertEqual(1, self.board.move(self.board.shogi_board[3][1], self.board.shogi_board[6][4]))

    def test_move_not_possible(self):
        self.assertEqual(0, self.board.move(self.board.shogi_board[1][1], self.board.shogi_board[2][4]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[1][1], self.board.shogi_board[5][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[1][1], self.board.shogi_board[0][1]))

        self.assertEqual(0, self.board.move(self.board.shogi_board[7][7], self.board.shogi_board[6][7]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[7][7], self.board.shogi_board[8][7]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[7][7], self.board.shogi_board[7][8]))

    def tearDown(self):
        self.board.shogi_board = [[Cell(x, y) for x in range(0, 9)] for y in range(0, 9)]

class LanceTestCase(unittest.TestCase):
    board = Board()
    def setUp(self):
        self.board.shogi_board[0][0].piece = Lance(Lance.BLACK)
        self.board.shogi_board[0][8].piece = Lance(Lance.BLACK)
        self.board.shogi_board[8][0].piece = Lance(Lance.WHITE)
        self.board.shogi_board[8][8].piece = Lance(Lance.WHITE)

    def test_move_possible_initial_board(self):
        # Black Lance
        self.assertEqual(1, self.board.move(self.board.shogi_board[0][0], self.board.shogi_board[2][0]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][0], self.board.shogi_board[7][0]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[7][0], self.board.shogi_board[0][0]))

        self.assertEqual(1, self.board.move(self.board.shogi_board[0][8], self.board.shogi_board[1][8]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][8], self.board.shogi_board[3][8]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[3][8], self.board.shogi_board[7][8]))

        # White Lance
        self.assertEqual(1, self.board.move(self.board.shogi_board[8][0], self.board.shogi_board[7][0]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][0], self.board.shogi_board[2][0]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][0], self.board.shogi_board[1][0]))

        self.assertEqual(1, self.board.move(self.board.shogi_board[8][8], self.board.shogi_board[5][8]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[5][8], self.board.shogi_board[2][8]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][8], self.board.shogi_board[1][8]))


    def test_promoted_move_possible_initial_board(self):
        self.board.shogi_board[0][0].piece.set_promoted()
        self.board.shogi_board[0][8].piece.set_promoted()
        self.board.shogi_board[8][0].piece.set_promoted()
        self.board.shogi_board[8][8].piece.set_promoted()

        self.assertTrue(self.board.shogi_board[0][0].piece.promoted)
        self.assertTrue(self.board.shogi_board[0][8].piece.promoted)
        self.assertTrue(self.board.shogi_board[8][0].piece.promoted)
        self.assertTrue(self.board.shogi_board[8][8].piece.promoted)

        # Black Lance
        self.assertEqual(1, self.board.move(self.board.shogi_board[0][0], self.board.shogi_board[1][0]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][0], self.board.shogi_board[2][1]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][1], self.board.shogi_board[1][1]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][1], self.board.shogi_board[0][1]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[0][1], self.board.shogi_board[0][0]))

        self.assertEqual(1, self.board.move(self.board.shogi_board[0][8], self.board.shogi_board[1][8]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][8], self.board.shogi_board[1][7]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][7], self.board.shogi_board[0][7]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[0][7], self.board.shogi_board[1][6]))

        # White Lance
        self.assertEqual(1, self.board.move(self.board.shogi_board[8][0], self.board.shogi_board[8][1]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[8][1], self.board.shogi_board[8][2]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[8][2], self.board.shogi_board[7][2]))

        self.assertEqual(1, self.board.move(self.board.shogi_board[8][8], self.board.shogi_board[7][7]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][7], self.board.shogi_board[6][6]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[6][6], self.board.shogi_board[5][5]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[5][5], self.board.shogi_board[4][4]))

    def test_move_not_possible(self):
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][0], self.board.shogi_board[5][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][8], self.board.shogi_board[4][4]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[8][0], self.board.shogi_board[7][1]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[8][8], self.board.shogi_board[5][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[5][8], self.board.shogi_board[8][8]))


    def tearDown(self):
        self.board.shogi_board = [[Cell(x, y) for x in range(0, 9)] for y in range(0, 9)]


class Silver_GeneralTestCase(unittest.TestCase):
    board = Board()
    def setUp(self):
        self.board.shogi_board[0][2].piece = Silver_General(Silver_General.BLACK)
        self.board.shogi_board[0][6].piece = Silver_General(Silver_General.BLACK)
        self.board.shogi_board[8][2].piece = Silver_General(Silver_General.WHITE)
        self.board.shogi_board[8][6].piece = Silver_General(Silver_General.WHITE)

    def test_move_possible_initial_board(self):
        self.assertFalse(self.board.shogi_board[0][2].piece.captured)
        self.assertFalse(self.board.shogi_board[0][6].piece.captured)
        self.assertFalse(self.board.shogi_board[8][2].piece.captured)
        self.assertFalse(self.board.shogi_board[8][6].piece.captured)
        # Black Silver General
        self.assertEqual(1, self.board.move(self.board.shogi_board[0][2], self.board.shogi_board[1][2]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][2], self.board.shogi_board[2][1]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][1], self.board.shogi_board[1][0]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][0], self.board.shogi_board[2][1]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][1], self.board.shogi_board[1][2]))


        self.assertEqual(1, self.board.move(self.board.shogi_board[0][6], self.board.shogi_board[1][6]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][6], self.board.shogi_board[2][7]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][7], self.board.shogi_board[1][8]))

        # White Silver General
        self.assertEqual(1, self.board.move(self.board.shogi_board[8][2], self.board.shogi_board[7][1]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][1], self.board.shogi_board[6][0]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[6][0], self.board.shogi_board[5][1]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[5][1], self.board.shogi_board[6][2]))

        self.assertEqual(1, self.board.move(self.board.shogi_board[8][6], self.board.shogi_board[7][7]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][7], self.board.shogi_board[6][6]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[6][6], self.board.shogi_board[7][5]))


    def test_promoted_move_possible_initial_board(self):
        self.board.shogi_board[0][2].piece.set_promoted()
        self.board.shogi_board[0][6].piece.set_promoted()
        self.board.shogi_board[8][2].piece.set_promoted()
        self.board.shogi_board[8][6].piece.set_promoted()

        self.assertTrue(self.board.shogi_board[0][2].piece.promoted)
        self.assertTrue(self.board.shogi_board[0][6].piece.promoted)
        self.assertTrue(self.board.shogi_board[8][2].piece.promoted)
        self.assertTrue(self.board.shogi_board[8][6].piece.promoted)

        # Black Silver General
        self.assertEqual(1, self.board.move(self.board.shogi_board[0][2], self.board.shogi_board[1][1]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][1], self.board.shogi_board[2][2]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][2], self.board.shogi_board[2][1]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[2][1], self.board.shogi_board[1][2]))

        self.assertEqual(1, self.board.move(self.board.shogi_board[0][6], self.board.shogi_board[0][5]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[0][5], self.board.shogi_board[1][5]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[1][5], self.board.shogi_board[2][4]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][4], self.board.shogi_board[1][4]))


        # White Silver General
        self.assertEqual(1, self.board.move(self.board.shogi_board[8][2], self.board.shogi_board[8][3]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[8][3], self.board.shogi_board[7][3]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][3], self.board.shogi_board[6][4]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[6][4], self.board.shogi_board[6][5]))

        self.assertEqual(1, self.board.move(self.board.shogi_board[8][6], self.board.shogi_board[8][5]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[8][5], self.board.shogi_board[7][4]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[7][4], self.board.shogi_board[8][3]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[7][4], self.board.shogi_board[8][4]))

    def test_move_not_possible(self):
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][2], self.board.shogi_board[5][8]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][6], self.board.shogi_board[4][4]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[8][2], self.board.shogi_board[7][5]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[8][6], self.board.shogi_board[5][8]))


    def tearDown(self):
        self.board.shogi_board = [[Cell(x, y) for x in range(0, 9)] for y in range(0, 9)]

class KnightTestCase(unittest.TestCase):
    board = Board()
    def setUp(self):
        self.board.shogi_board[0][7].piece = Knight(Knight.BLACK)
        self.board.shogi_board[0][1].piece = Knight(Knight.BLACK)
        self.board.shogi_board[8][7].piece = Knight(Knight.WHITE)
        self.board.shogi_board[8][1].piece = Knight(Knight.WHITE)

    def test_move_possible_initial_board(self):
        self.assertFalse(self.board.shogi_board[0][7].piece.captured)
        self.assertFalse(self.board.shogi_board[0][1].piece.captured)
        self.assertFalse(self.board.shogi_board[8][7].piece.captured)
        self.assertFalse(self.board.shogi_board[8][1].piece.captured)
        # Black Knights
        self.assertEqual(1, self.board.move(self.board.shogi_board[0][1], self.board.shogi_board[2][0]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][0], self.board.shogi_board[4][1]))

        self.assertEqual(1, self.board.move(self.board.shogi_board[0][7], self.board.shogi_board[2][6]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[2][6], self.board.shogi_board[4][5]))

        # White Silver General
        self.assertEqual(1, self.board.move(self.board.shogi_board[8][1], self.board.shogi_board[6][2]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[6][2], self.board.shogi_board[4][1]))
        #TODO aquí ha comido una pieza

        self.assertEqual(1, self.board.move(self.board.shogi_board[8][7], self.board.shogi_board[6][6]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[6][6], self.board.shogi_board[4][5]))
        #TODO aquí ha comido al otro caballo



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

    def test_move_not_possible(self):
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][1], self.board.shogi_board[5][8]))
        self.assertEqual(1, self.board.move(self.board.shogi_board[0][1], self.board.shogi_board[2][2]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[2][2], self.board.shogi_board[0][1]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[0][7], self.board.shogi_board[4][4]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[8][1], self.board.shogi_board[7][5]))
        self.assertEqual(0, self.board.move(self.board.shogi_board[8][7], self.board.shogi_board[5][8]))


    def tearDown(self):
        self.board.shogi_board = [[Cell(x, y) for x in range(0, 9)] for y in range(0, 9)]