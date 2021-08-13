# cpu.py 

This module is responsible for handling the computer player logic. 

# Algorithm 

The CPU uses the MinMax Alogorith to calculate the best spot to place a token to beat the user or force a draw. Minmax is a kind of backtracking algorithm that is used in decision making and game theory to find the optimal move for a player, assuming that your opponent also plays optimally. The maximizer tries to get the highest score possible while the minimizer tries to do the opposite and get the lowest score possible. For more information click the link below:

- [http://article.sapub.org/10.5923.j.jgt.20200901.01.html](http://article.sapub.org/10.5923.j.jgt.20200901.01.html)
- [https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/)

## CPU Methods
  - `printBoard`
    - This method prints the board to the console screen.
  - `find_best_move`
    - This method recursivily calls the _min_max() function to find the best possible move and returns it
  - `_min_max`
    - This method simulates all possible moves on the board as defined in the Minimax algorithm and returns the score calculated 
  - `_evaluate_game`
    - This method evaluates the game board and returns an appropriate score  
  - `isMovesLeft`
    - This method checks to see if there are any possible moves still left/if the board is full

## Potential Use Examples 
```python
from ttt.cpu.py import *         # CPU 

Cpu cpu

cpu = Cpu(self._game)
cpu.printBoard()
cpu_move = cpu.find_best_move()
row1 = cpu_move[0]
col1 = cpu_move[1]
```

## Interacting with `game.py`

The `Cpu` object should contain a reference to the `Game` object, which represents the current state of the game:

```python
from ttt.game import Game

class Cpu():
    __init__(self, game: Game):
        self._game = copy.deepcopy(game)
        self._board = self._game._board

    # snip
```

#### CPU Play Sequence Diagram 

```
     ┌──────┐               ┌───────────┐                        ┌──────┐          ┌───────┐
     │PyGame│               │Board.run()│                        │cpu.py│          │game.py│
     └──┬───┘               └─────┬─────┘                        └──┬───┘          └───┬───┘
        │      pg.event.get()     │                                 │                  │    
        │ <────────────────────────                                 │                  │    
        │                         │                                 │                  │    
        │ (a list of input events)│                                 │                  │    
        │ ────────────────────────>                                 │                  │    
        │                         │                                 │                  │    
        │                         │      human player: Game.place_move(row, col)       │    
        │                         │ ──────────────────────────────────────────────────>│    
        │                         │                                 │                  │    
        │                         │         ret True if valid, False otherwise         │    
        │                         │ <──────────────────────────────────────────────────│    
        │                         │                                 │                  │    
        │                         │           cpu = Cpu()           │                  │    
        │                         │ ────────────────────────────────>                  │    
        │                         │                                 │                  │    
        │                         │          (Cpu instance)         │                  │    
        │                         │ <────────────────────────────────                  │    
        │                         │                                 │                  │    
        │                         │       cpu.find_best_move()      │                  │    
        │                         │ ────────────────────────────────>                  │    
        │                         │                                 │                  │    
        │                         │ (best move in (row, col) format)│                  │    
        │                         │ <────────────────────────────────                  │    
        │                         │                                 │                  │    
        │                         │     computer player: Game.place_move(row, col)     │    
        │                         │ ──────────────────────────────────────────────────>│    
        │                         │                                 │                  │    
        │                         │         ret True if valid, False otherwise         │    
        │                         │ <──────────────────────────────────────────────────│    
     ┌──┴───┐               ┌─────┴─────┐                        ┌──┴───┐          ┌───┴───┐
     │PyGame│               │Board.run()│                        │cpu.py│          │game.py│
     └──────┘               └───────────┘                        └──────┘          └───────┘
```
