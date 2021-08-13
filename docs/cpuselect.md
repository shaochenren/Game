# cpuselect.py

This module is responsible for spawning a dialogue window that asks the player whether they want to play a hotseat game (PvP) or agains the computer (PvCpu). 

## Dependencies 

Dialogues and buttons seem to be from a module called `pygame_gui`: 

- [pygame_gui](https://pygame-gui.readthedocs.io/en/latest/index.html)
- [Doc about listening to button clicks](https://pygame-gui.readthedocs.io/en/latest/events.html)

## cpuselect Methods
  - `is_hotseat`
    - This method returns True if the user clicks hotseat and False if the user clicks solo
  - `_spawn_dialog`
    - This method creates the GUI for the user to select which version of the game that they want to play
  - `_listen_for_clicks`
    - This method listens for when the user clicks on the screen 
  - `_update_ui`
    - This method updates the GUI slection screen with buttons

## Potential Use
```python
from ttt.cpuselect.py import *         # cpuselects

select = CpuSelect()
is_hotseat = select.is_hotseat()
if is_hotseat == 'EXIT':
   quit()
# snip
board.run(is_hotseat)
```

#### cpuselect Sequence Diagram

```
     ┌───────┐                                        ┌────────────┐          ┌───────┐          ┌────────┐
     │main.py│                                        │cpuselect.py│          │game.py│          │board.py│
     └───┬───┘                                        └─────┬──────┘          └───┬───┘          └───┬────┘
         │               select = CpuSelect()               │                     │                  │     
         │──────────────────────────────────────────────────>                     │                  │     
         │                                                  │                     │                  │     
         │                CpuSelect instance                │                     │                  │     
         │<──────────────────────────────────────────────────                     │                  │     
         │                                                  │                     │                  │     
         │         is_hotseat = select.is_hotseat()         │                     │                  │     
         │──────────────────────────────────────────────────>                     │                  │     
         │                                                  │                     │                  │     
         │True if [Hotseat] clicked, False if [Solo] clicked│                     │                  │     
         │<──────────────────────────────────────────────────                     │                  │     
         │                                                  │                     │                  │     
         │                                                  │                     │                  │     
         │                             game = Game()        │                     │                  │     
         │───────────────────────────────────────────────────────────────────────>│                  │     
         │                                                  │                     │                  │     
         │                             Game instance        │                     │                  │     
         │<───────────────────────────────────────────────────────────────────────│                  │     
         │                                                  │                     │                  │     
         │                                                  │                     │                  │     
         │                                    board = Board(game)                 │                  │     
         │───────────────────────────────────────────────────────────────────────────────────────────>     
         │                                                  │                     │                  │     
         │                                      Board instance                    │                  │     
         │<───────────────────────────────────────────────────────────────────────────────────────────     
         │                                                  │                     │                  │     
         │                                   board.run(is_hotseat)                │                  │     
         │───────────────────────────────────────────────────────────────────────────────────────────>     
     ┌───┴───┐                                        ┌─────┴──────┐          ┌───┴───┐          ┌───┴────┐
     │main.py│                                        │cpuselect.py│          │game.py│          │board.py│
     └───────┘                                        └────────────┘          └───────┘          └────────┘
```
