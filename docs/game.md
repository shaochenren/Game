# game.py

This module represents the state of the game. It handles all game logic and **should not** be involved in touching the UI in any way. The UI might as well not exist as far as this module is concerned. 

# Design

## `Game` Class

### Game Methods
  - `win_checker`
	- This method checks for a winning row, column, or diagonal line on the board
	- Will return a Draw if the whole board is filled up and there are no winning lines
	- Will return Undecided if the board still has available space and there are no winning lines
  - `reset_game`
	- This method will reset the game by cleaning the entire board of X's and O's
	- Resets when there is a winner or a tie
	- Potential Feature: Reset when user clicks on a button to reset board during the game
  - `player`
	- This method will return the current player's move on the board
  - `get_opponent`
	- This method will return the current opponent's move on the board
  - `place_move`
	- This method will place an X or an O, depending on who's turn it is, depending on the space the active player chose
  - `_change_player`
	- This method will cycle turns, after the current player does their move, and allow the other player to play
  - `_winner`
	- This method will determine and return who the winner is depending on who's turn it is and whether there is a winning line


### Constructor 

The state of the game is tracked via a nested list representing the 3x3 grid:

```python 
class Game:
    __init__(self):
	self._player = X
        self._board = [[None] * 3,
                     [None] * 3, 
                     [None] * 3]
        # snip
```

The `Game` class should have some utility functions at the implementer's discretion. Some example might include:

- `Game._get_value(row: int, col: int) -> str`
  - Get the value currently in [`row`, `col`].
  - Params:
    - `row`: Row number in logical form (1 to 3 inclusive)
    - `col`: Column number in logical form (1 to 3 inclusive) 
  - Return whatever's in `self._ttt[row, col]`. Return `None` if empty.

## Interacting with `board.py`

This module **does not** touch the UI in any way. The `Game` class is expected to be an instance variable of `Board` and keeps track of the game state. 

For details, see [board.md](board.md).




