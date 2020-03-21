# Shogi
Shogi repository for Eventbrite "homework" during the coronavirus apocalypse

## Prev requirements

The application makes use of third-party libraries. All dependencies are found in the `requirements.txt` file.

To install the dependencies execute the following command in a virtual python environment:

    pip install -r requirements

## Functionalities implemented
- Piece's movement
- Promoted pieces movement
- A piece can be promoted during the match
- Check implemented, but not check-mate (this only advertised when captured piece is a King)

## Usage
You can run the application executing the following command

```
python play.py
```
And the application shows the initialize board

## Tests
- Tests for pieces movement
- Tests for pieces promoted
- Tests for check (jaque)
You can launch the test suite by running the following command:

    python -m unittest