# dimensions.py

This module represents the dimensions (width, height) and coordinates (x and y offsets from `(0,0)`) of the board and the UI elements.

If you're looking for the variable names, click on one of the links below:
- [Board variables](#board-variables)
- [UI variables](#ui-variables)

# Board

## Overview

```
+-----+-----+-----+
| T11 | T12 | T13 |
| --- | --- | --- |
| T21 | T22 | T23 |
| --- | --- | --- |
| T31 | T32 | T33 |
+-----+-----+-----+

```

- The grid location variables (`T11`, `T12`, etc) are numbered in the row-column format, e.g. `T23` represents row 2 column 3.
- All x,y coordinates are:
  - Offsets from the origin (0,0).
  - The values represent the top left corner of the particular element in question.

## Assumptions 

- Each of the player images (x.png and y.png) will be either scaled to fit or be smaller than `GRID_WIDTH` and `GRID_HEIGHT`.

## Board Variables

The board area is defined by the following variables:

### Board
- Size 
  - `BOARD_WIDTH`, `BOARD_HEIGHT`
    - Playable area's width and height.
  - `BOARD_SIZE`
    - Playable area's width and height as a size tuple (width, height).
- Offset
  - `BOARD_X`, `BOARD_Y`
    -  X and Y coordinates of the board.
  - `BOARD_OFFSET`
    - X and Y coordinates of the board as an offset tuple (x, y)

### Grid Squares
- Size
  - `GRID_WIDTH`, `GRID_HEIGHT`
    -  Each grid square's width and height.
  - `GRID_SIZE`
    - Each grid square's width and height as a size tuple (width, height)
- Offset
  - `T11`, `T12`, ... `T33`
    -  X and Y coordinates of each grid square. For example, `T23` represents the upper left corner of row 2 column 3. 

### Winning lines
  - `WC` - Winning column
  - `WR` - Winning row
  - `WD` - Winning diagonal
  - For example, `WC11` is the mid point between `T11` and `T12`. Similarly, `WC31` is the midpoint at the bottom which is between `T31` and `T32`.
    - The other `WC` and `WR` follow the same pattern.
    - For `WD`, the coordinates represent the corners.

## Potential Use Examples 

```python
from ttt.colors.py import *         # RED 
from ttt.dimensions.py import *     # BOARD_X, BOARD_WIDTH, GRID_HEIGHT

screen = pg.display.set_mode(UI_SIZE, 0, 32) 

# snip
# ...

# y-coordinate of the center point of row 1
row1_center_y = T11 + GRID_HEIGHT / 2

# line origin
start = (BOARD_X, row1_center_y)

# line endpoint 
end = (BOARD_X + BOARD_WIDTH, row1_center_y)

# Draw a red line across the first row, straight through the middle of all three squares.
pygame.draw.line(screen, RED, start, end, 4)
```

# User Interface

## Overview

```
+----------------+
| Game Board     |
| (3x3 grid)     |
| -------------- |
| Status Area    |
+----------------+
```

## Assumptions 

- The current plan is to have the status area rendered below the game board.

## UI Variables

The UI area is defined by the following variables:

### Status Area
- Size
  - `STATUS_WIDTH`, `STATUS_HEIGHT`
    -  Status area's width and height.
  - `STATUS_SIZE`
    - Status area's width and height as a size tuple.
- Offset
  - `STATUS_X`, `STATUS_Y`
    - Status area's top left corner xy coordinates.
  - `STATUS_OFFSET`
    - Status area's xy coordinate as an offset tuple (x, y)

### UI 

- Size
  - `UI_WIDTH`, `UI_HEIGHT`
    - The entire UI's width and height.
  - `UI_SIZE`
    - The entire UI's width and height as a size tuple (width, height)


## Potential Use Examples

```python
from ttt.dimensions.py import *    # UI_SIZE

# snip
# ...

flags = 0
color_depth = 32

# Initialize the game window. 
screen = pg.display.set_mode(UI_SIZE, flags, color_depth) 
```
