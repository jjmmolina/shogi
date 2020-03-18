# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 17/03/2020

"""
import click as click

from app.models.board import Board


class Play:
    """This class is used to play the game."""
    def run(self):
        """This method is used to start the game. """
        board = Board()
        board.initialize_board()
        tablero = board.__str__()
        print(tablero)

@click.command()
def play():
    """Starts a simulation of the game"""
    Play().run()


if __name__ == '__main__':
    play()