# How Everything *Should* Work Together 

Not everything is set in stone. All are subject to modification pending team input.

We should probably have a documentation for each of the modules, too. They don't have to be detailed. Just concise and informative enough so everyone knows what's what. Things like what a function does, etc. 

## main.py

This is the main entry point to the program. It instantiates a `Game` object and uses it to track the state of the game.

Probably imports:
- board.py
- game.py
- cpu.py 
- maybe more? 

## ttt/board.py

This contains the non-member function definitions for anything related to manipulating the [Game](#ttt-game-py) object.

This is also where the board rendering function should be defined.

Example: 

```
def reset_game(game: Game):
    game.reset()
    print("The game has been reset")
```

Probably imports: 
- game.py
- colors.py 

## ttt/colors.py 

This contains the colors to be used in the program, defined in a format recognized by PyGame. 

Each color object is an RGB tuple, e.g. `(red, green, blue)`:

```
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
```

## ttt/cpu.py


This contains any functions, objects, or routines related to the computer player logic.

Should we make a `Cpu` class for the computer player? If it's implemented as a FSM then it wouldn't hurt, maybe? 

Potential example: 
```
def next_move(game: Game): 
    board = game.get_state()
    for row in board:
        some_other_func()
```

Probably imports:
- game.py 

## ttt/dimensions.py

Similar to [colors.py](#ttt-colors-py), except it stores coordinates and dimensions to be used in the game. Instead of hardcoding lengths and whatnot, put them in here.

All definitions are in tuples, following PyGame's convention: 

- Coordinates are in `(x, y)` format 
- Rectangles are in `(x_offset, y_offset, width, height)` format, where:
  - `x_offset`: Offset from the top left corner of the surface 
  - `y_offset`: Offset from the top left corner of the surface

Judging from the example code, the coordinates for each of the matrix "cells" are its upper left corners. Someone can correct this if this is wrong.

Regardless, the naming scheme should be either:

```
+----+----+----+
| aa | ab | ac |
| -- | -- | -- |
| ba | bb | bc |
| -- | -- | -- |
| ca | cb | cc |
+----+----+----+

aa = (0, 0)
#... 
```

or:

```
+-----+-----+-----+
| t11 | t12 | t13 |
| --- | --- | --- |
| t21 | t22 | t23 |
| --- | --- | --- |
| t31 | t32 | t33 |
+-----+-----+-----+

t11 = (0, 0)
#...
```

Probably imports:
- ??? 


## ttt/game.py

This contains the `Game` class and its member functions. 

A `Game` object will be instantiated by [main.py](#main-py) and will be used to represent the current state of the game.

Example:

```
class Game:
    def __init__(self):
        self._board = []
```


Probably imports:
- None (??)
