# main.py

This module represents the main driver of the program. The file instantiates a `Game` object and uses it to track the state of the game.
The program will call functions defined in different files in order to run the program correctly

# Board Class Functions

__init__(self) : initializer with instance attributes

drawToken(self, token) : Draws the symbol (X, O) corresponding to mouse click position

# Game Class Functions

TODO 

# Workflow 

## Game Initialization 

```
     ┌───────┐                ┌───────┐          ┌────────┐
     │main.py│                │game.py│          │board.py│
     └───┬───┘                └───┬───┘          └───┬────┘
         │"construct Game object" │                  │     
         │───────────────────────>│                  │     
         │                        │                  │     
         │     Game instance      │                  │     
         │<───────────────────────│                  │     
         │                        │                  │     
         │        "construct Board instance"         │     
         │──────────────────────────────────────────>│     
         │                        │                  │     
         │        reference to Game instance         │     
         │──────────────────────────────────────────>│     
         │                        │                  │     
         │              Board instance               │     
         │<──────────────────────────────────────────│     
     ┌───┴───┐                ┌───┴───┐          ┌───┴────┐
     │main.py│                │game.py│          │board.py│
     └───────┘                └───────┘          └────────┘
```

`main.py` is responsible for initializing the game and handing off user interaction to `board.py`. To do this, it constructs a `Game` object and passes a reference to it to the `Board` constructor. 

The `Game` object keeps track of the current state of the game and provides functions for modifying the game state. For details, see [game.md](game.md). 

The `Board` object handles all user interaction and draws the UI. For details. see [board.md](board.md). 

