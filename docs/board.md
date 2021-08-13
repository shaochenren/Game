# board.py

This module represents the board and screen of Tic Tac Toe.

# Board

## Appearance

```
+-----+-----+-----+
| T11 | T12 | T13 |
| --- | --- | --- |
| T21 | T22 | T23 |
| --- | --- | --- |
| T31 | T32 | T33 |
+-----+-----+-----+
```

## Gameplay

- Each player has to click one of the 9 availalble squares in each turn. The winner is displayed on the board when a player wins or if the game ends with a draw.

## Board Methods
  - `_create_button`
    - This method is for creating and showing the buttons at the bottom of the game screen.
  - `drawToken`
    - This method reads the current state of the game and draws a token to the board of the screen.
  - `drawRowLine`
    - This method draws the winning line across the row passed in.
  - `drawColumnLine`
    - This method draws the winning line down the column passed in.
  - `drawDiagonalRTL`
    - This method draws the winning line diagonally from right to left.
  - `drawDiagonalLTR`
    - This method draws the winning line diagonally from left to right.
  - `render_message`
    - This method takes the copied rendered message and posts it onto the board.
  - `render_status_area`
    - This method renders the status area at the bottom of the board.
  - `_draw_ui`
    - This method draws the Initial tic tac toe board on the UI with rows and columns hihglighted in red.
  - `_draw_winning_line`
    - This method draws the winning lines given the context of "row", "column", "LTR" diagonal , or "RTL" diagonal with the corresponding row  number or column number


# Design

## `Board` Class

This class is **purely for rendering the UI** based on the state of the `Game` instance contained within. It is mainly used to call the `Game` functions to read, modify the game state.

The `Board` class has the *run()* function visible publicly :

- `Board.run() -> None`
  - Starts an infinite loop to keep the game going by accepting the user input.

The game instance reference is passed by the main function:
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
## Class Diagram

`Board` *contains* `Game`:

```
,---------------------------------------.
|Game                                   |
|---------------------------------------|
|-_ttt: list                            |
|+place_move(row: int, col: int) -> bool|
|+player() -> str               |
|+win_checker() -> tuple(str)           |
|+reset_game() -> void                  |
`---------------------------------------'
                    |
                    |
       ,------------------------.
       |Board                   |
       |------------------------|
       |-_game: Game            |
       |-_screen: pygame.Surface|
       |+run() -> None          |
       `------------------------'
```

## Reading and Modifying the Game State

The game's current state is kept track by the `Game` instance variable.

The current player is determined by the board from the `Game` object calling the `player() -> str` function visible publicly:

```
     ┌─────┐                                ┌─────┐
     │Board│                                │_game│
     └──┬──┘                                └──┬──┘
        │   self._game.player()                │
        │─────────────────────────────────────>│
        │                                      │
        │          ret 'x' or 'o'              │
        │<─────────────────────────────────────│
        │                                      │
        ────┐                                  │
            │ (set game state with 'x' or 'o') │
        <───┘                                  │
     ┌──┴──┐                                ┌──┴──┐
     │Board│                                │_game│
     └─────┘                                └─────┘
```

- The board observes a user click event on row x and col y and needs to modify the game's state accordingly
- `Game` object has a `place_move(row: int, col: int) -> bool` visible publicly when called from the board class sets the grid(x,y) with the current player, changes the active player and returns true on success. If the cell is already chosen earlier by either player, it returns a false.

```
     ┌─────┐                                     ┌─────┐
     │Board│                                     │_game│
     └──┬──┘                                     └──┬──┘
        │      self._game.place_move(2, 1)          │
        │──────────────────────────────────────────>│
        │                                           │
        │ret True if valid move, False otherwise    │
        │<──────────────────────────────────────────│
        │                                           │
        ────┐                                       │
            │ (check game state with True or False) │
        <───┘                                       │
     ┌──┴──┐                                     ┌──┴──┐
     │Board│                                     │_game│
     └─────┘                                     └─────┘
```
