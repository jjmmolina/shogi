# Shogi
Shogi repository for a selection process in an international company during the coronavirus quarantine. It is not a version to play, but you 
can run a lot of tests that show the functionalities implemented. 
This document includes a brief summary about how to install the code, a list of functionalities implemented, a how to use
the application, tests include and, finally, a TODO list for the future.

## Prev requirements

The application makes use of third-party libraries. All dependencies are found in the `requirements.txt` file. It uses 
_pandas_ library to print quickly the matrix 9*9 that represent the board.

To install the dependencies execute the following command in a virtual python environment:

    pip install -r requirements

## Classes
The code is divided in classes (inside folder _models_). 
- **File _board.py_** -> It includes the class **Board**. This is the main class and it includes features like move a piece, check if is mate or reintroduce a captured piece.
A board is a 9*9 matrix with 2 arrays to save pieces captures (one per team). Other class in this file is **Cell** class, that 
represent a single cell of the board's matrix. This cell contains a piece.
- **File _pieces.py_** -> This file contains a class called **Pieces** that is the superclass of the rest of shogi pieces. All pieces 
share common methods and attributes, for example, _is_my_movement_ or _is_my_promoted_movement_. Also, Pieces contains methods to
capture, change color, promoted or undone all them

## Functionalities implemented
- Piece's movement
- Promoted pieces movement
- A piece can be promoted during the match
- Check and check-mate 
- Reintroduced captured pieces

## Usage
You can run the application executing the following command

```
python play.py
```
And the application shows the initialize board.

## Tests
All tests are implemented in the folder called test. This includes:
- Tests for pieces movement.
- Tests for pieces promoted.
- Tests for check (jaque) and check-mate.
- Tests for reintroduce captured pieces.

You can launch the test suite by running the following command:

    python -m unittest
 
 ## TO-DO list
 - Create a match in which you and a partner can move the pieces to play a real game.
 - User Interface.
 - Initialize the game with famous matchs
 
