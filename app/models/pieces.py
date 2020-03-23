# -*- coding: UTF-8 -*-

"""

AUTHOR: jesus

DATE: 17/03/2020

"""


class Pieces():
    """This class represents all shogi pieces."""
    BLACK = 'B'
    WHITE = 'W'

    def __init__(self, name, color, promoted=False, captured=False):
        self.name = name
        self.color = color
        self.promoted = promoted
        self.captured = captured

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'

    def __str__(self):
        if self.color==Pieces.BLACK:
            color = 'v'
        else: color ='^'
        piece = self.name+color
        return f'{piece}'

    def _change_color(self):
        if self.color == Pieces.BLACK:
            self.color = Pieces.WHITE
        else:
            self.color = Pieces.WHITE

    def set_promoted(self):
        """Promoted a piece"""
        self.promoted = True

    def set_unpromoted(self):
        """Unpromoted a piece"""
        self.promoted = False

    def set_captured(self):
        """Captured a piece"""
        self.captured = True
        # self._change_color()
        if self.promoted:
            self.promoted = False

    def set_uncaptured(self):
        """Unpromoted a piece"""
        self.promoted = False

    def is_my_movement(self, cell_from, cell_to):
        pass
    def is_my_promoted_movement(self, cell_from, cell_to):
        pass

    def _gold_general_movement(self, cell_from, cell_to):
        if (cell_to != cell_from):
            if (((cell_to.y - cell_from.y) == 0) & (abs(cell_to.x - cell_from.x) == 1)):  # Misma fila
                return True
            if (self.color == self.BLACK):
                if ((cell_to.y - cell_from.y == 1) & (
                        abs(cell_to.x - cell_from.x) <= 1)):  # Movimiento hacia arriba incluye diagonal
                    return True
                if ((abs(cell_to.y - cell_from.y) == 1) & ((cell_to.x - cell_from.x) == 0)):  # movimiento hacia abajo
                    return True
            elif (self.color == self.WHITE):
                if ((cell_to.y - cell_from.y) == -1) & ((cell_to.x - cell_from.x) <= 1):  # Movimiento hacia abajo incluye diagonal
                    return True
                if ((abs(cell_to.y - cell_from.y) == 1) & ((cell_to.x - cell_from.x) == 0)):  # movimiento hacia arriba
                    return True
        return False

class King(Pieces):
    def __init__(self, color):
        Pieces.__init__(self,"K", color, False)

    def is_my_movement(self, cell_from, cell_to):
        if ((abs(cell_to.y - cell_from.y) <= 1) & (abs(cell_to.x - cell_from.x) <= 1)):
            return True
        return False


class Rook(Pieces):
    def __init__(self,  color):
        Pieces.__init__(self,"R", color)

    def is_my_movement(self, cell_from, cell_to):
        if self.promoted:
            return(self.is_my_promoted_movement(cell_from, cell_to))
        else:
            if ((((cell_to.y - cell_from.y) == 0) & (abs(cell_to.x - cell_from.x) >= 1))|
                ((abs(cell_to.y - cell_from.y) > 1) & ((cell_to.x - cell_from.x) == 0))):
                return True
        return False

    def is_my_promoted_movement(self, cell_from, cell_to):
        if self.promoted:
            if ( (((cell_to.y - cell_from.y) == 0) & (abs(cell_to.x - cell_from.x) >= 1))|
                ((abs(cell_to.y - cell_from.y) > 1) & ((cell_to.x - cell_from.x) == 0)) # Mismo movimiento que sin coronar
                |
            #Este movimiento es semejante al del rey
                ((abs(cell_to.y - cell_from.y) <= 1) & (abs(cell_to.x - cell_from.x) <= 1))
            ):
                return True
        return False


class Bishop(Pieces):
    def __init__(self, color):
        Pieces.__init__(self, "B", color)

    def is_my_movement(self, cell_from, cell_to):
        if self.promoted:
            return(self.is_my_promoted_movement(cell_from, cell_to))
        else:
            if ((abs(cell_to.y - cell_from.y) >= 1) & (abs(cell_to.x - cell_from.x) >= 1) & (
                    abs(cell_to.y - cell_from.y) == abs(cell_to.x - cell_from.x))
            ):
                return True
        return False

    def is_my_promoted_movement(self, cell_from, cell_to):
        if self.promoted:
            if (
                    (abs(cell_to.y - cell_from.y) >= 1) & (abs(cell_to.x - cell_from.x) >= 1) & (
                    abs(cell_to.y - cell_from.y) == abs(cell_to.x - cell_from.x)) #Mismo movimiento que sin coronar
                    |
                    # Este movimiento es semejante al del rey
                    ((abs(cell_to.y - cell_from.y) <= 1) & (abs(cell_to.x - cell_from.x) <= 1))
            ):
                return True
        return False

class Gold_General(Pieces):
    def __init__(self, color):
        Pieces.__init__(self, "G", color, False)

    def is_my_movement(self, cell_from, cell_to):
        return(self._gold_general_movement(cell_from, cell_to))

class Silver_General(Pieces):
    def __init__(self, color):
        Pieces.__init__(self, "S", color)

    def is_my_movement(self, cell_from, cell_to):
        if self.promoted:
           return(self.is_my_promoted_movement(cell_from, cell_to))
        else:
            if (self.color == self.BLACK):
                if ((cell_to.y - cell_from.y == 1) & (abs(cell_to.x - cell_from.x) <= 1)):  # Movimiento hacia arriba incluye diagonal
                    return True
                if((abs(cell_to.y - cell_from.y) == 1) & (abs(cell_to.x - cell_from.x) == 1) & (
                        abs(cell_to.y - cell_from.y) == abs(cell_to.x - cell_from.x))
                  ):  # movimiento hacia atrás excepto la vertical
                    return True
            elif (self.color == self.WHITE):
                if (abs(cell_to.y - cell_from.y) == 1) & (abs(cell_to.x - cell_from.x) <= 1):  # Movimiento hacia abajo incluye diagonal
                    return True
                if ((abs(cell_to.y - cell_from.y) == 1) & ((cell_to.x - cell_from.x) == 1)):  # movimiento hacia arriba
                    return True
        return False

    def is_my_promoted_movement(self, cell_from, cell_to):
        if self.promoted:
            return (self._gold_general_movement(cell_from, cell_to))
        return False

class Knight(Pieces):
    def __init__(self, color):
        Pieces.__init__(self, "N", color)

    def is_my_movement(self, cell_from, cell_to):
        if self.promoted:
            return (self.is_my_promoted_movement(cell_from, cell_to))
        else:
            if (self.color == self.BLACK):
                if ((cell_to.y - cell_from.y) == 2) & (abs(cell_to.x - cell_from.x) == 1):
                    return True
            elif (self.color == self.WHITE):
                if ((cell_to.y - cell_from.y) == -2) & (abs(cell_to.x - cell_from.x) == 1):
                    return True
        return False

    def is_my_promoted_movement(self, cell_from, cell_to):
        if self.promoted:
            return (self._gold_general_movement(cell_from, cell_to))
        return False

class Lance(Pieces):
    def __init__(self, color):
        Pieces.__init__(self, "L", color)

    def is_my_movement(self, cell_from, cell_to):
        if self.promoted:
            return(self.is_my_promoted_movement(cell_from, cell_to))
        else:
            if(self.color == self.BLACK):
                if ( ( (cell_to.y - cell_from.y) >= 1) & ((cell_to.x - cell_from.x) == 0)):
                    return True
            else:
                if (((cell_from.y - cell_to.y) >= 1) & ((cell_to.x - cell_from.x) == 0)):
                    return True
        return False

    def is_my_promoted_movement(self, cell_from, cell_to):
        if self.promoted:
            return (self._gold_general_movement(cell_from, cell_to))
        return False

class Pawn(Pieces):
    def __init__(self, color):
        Pieces.__init__(self, "P", color)

    def is_my_movement(self, cell_from, cell_to):
        if self.promoted:
            return(self.is_my_promoted_movement(cell_from, cell_to))
        else:
            if self.color is self.BLACK:
                if ((cell_to.y-cell_from.y == 1) & (cell_to.x-cell_from.x == 0)):
                    return True
            else:
                if ((cell_to.y-cell_from.y == -1) & (cell_to.x-cell_from.x == 0)):
                    return True
        return False

    def is_my_promoted_movement(self, cell_from, cell_to):
        if self.promoted:
            return (self._gold_general_movement(cell_from, cell_to))
        return False