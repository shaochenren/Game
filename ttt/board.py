import time

import pygame as pg, sys
from pygame.locals import *
import pygame_gui as pgui
from pygame.locals import QUIT

from ttt.dimensions import *
from ttt.colors import *
from ttt.game import Game, X, O, DRAW, UNDECIDED
from ttt.cpu import Cpu

IMG_DIR = 'img/'

X_IMG_PATH = IMG_DIR + 'x.png'
O_IMG_PATH = IMG_DIR + 'o.png'
OPENING_IMG_PATH = IMG_DIR + 'ttt_opening.jpg'

GAME_NAME = 'Tic Tac Toe'
WIN_MSG = "Player {} has won!"
DRAW_MSG = "It's a draw."
INVALID_MSG = "Invalid position."

class Board:
    def __init__(self, game: Game, player1, player2=None):
        '''
        Constructor for the Board object.
        Parameters:
            game (Game): A reference to the Game object.
        '''
        # initializing the pygame window
        pg.init()

        # instance variables
        self._fps = 30
        self.CLOCK = pg.time.Clock()
        self._game = game

        # initialize the UI window
        flags = 0
        color_depth = 32
        self._screen = pg.display.set_mode(UI_SIZE, flags, color_depth)

        pg.display.set_caption(GAME_NAME)

        # loading the images as python object
        splash_screen = pg.image.load(OPENING_IMG_PATH)
        self._x_img = pg.image.load(X_IMG_PATH)
        self._o_img = pg.image.load(O_IMG_PATH)

        # resizing images
        splash_screen = pg.transform.scale(splash_screen, UI_SIZE)
        self._x_img = pg.transform.scale(self._x_img, GRID_SIZE)
        self._o_img = pg.transform.scale(self._o_img, GRID_SIZE)
        
        # reset and quit button
        self._manager = pgui.UIManager(UI_SIZE)
        self._btn_reset = pgui.elements.UIButton(relative_rect=pg.Rect((0, 400), (100, 50)), text='Reset', manager=self._manager)
        self._btn_quit = pgui.elements.UIButton(relative_rect=pg.Rect((300, 400), (100, 50)), text='Quit', manager=self._manager)
        
        # display splash screen
        origin = (0, 0)
        self._screen.blit(splash_screen, origin)

        # updating the display
        pg.display.update()
        time.sleep(2)

        self._player1 = player1
        self._player2 = player2

        self._draw_ui()


    def run(self, is_hotseat) -> None:
        '''
        Runs the game in an infinite loop, accepting user input all the while.
        '''
        clock = pg.time.Clock()
        while(True):
            timer = clock.tick(60)/1000.0
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    # checks winner
                    self.drawToken(is_hotseat)
                    winner, direction, value = self._game.win_checker()
                    if(winner != 'N'):
                        self._game.reset_game()
                elif event.type == pg.USEREVENT:
                    if event.user_type == pgui.UI_BUTTON_PRESSED:
                        if event.ui_element == self._btn_reset:
                            self._game.reset_button()
                            self._draw_ui()
                        if event.ui_element == self._btn_quit:
                            pg.quit()
                            sys.exit()
                self._manager.process_events(event)
            self._create_button(timer)
            pg.display.update()
            self.CLOCK.tick(self._fps)
            
    def _create_button(self, timer) -> None:
        '''
        Helper function for showing buttons at the bottom of the game screen
        '''
        self._manager.update(timer)
        self._manager.draw_ui(self._screen)
        pg.display.update()

    def drawToken(self, is_hotseat) -> None:
        '''
        Read the current game state and draw a token where appropriate.
        '''
        self._render_status_area()

        # get coordinates of mouse click
        x, y = pg.mouse.get_pos()
        thickness = 4

        # get column of mouse click
        if x < BOARD_WIDTH / 3:
            col = 1
        elif x < BOARD_WIDTH / 3 * 2:
            col = 2
        elif x < BOARD_WIDTH:
            col = 3
        else:
            col = None
    
        # get row of mouse click
        if y < BOARD_HEIGHT / 3:
            row = 1
        elif y < BOARD_HEIGHT / 3 * 2:
            row = 2
        elif y < BOARD_HEIGHT:
            row = 3 
        else:
            row = None

        # If the user clicked an area within bounds, place the token
        if(row and col):
            location = GRID_OFFSETS[row - 1][col - 1]

            # Place the token
            previous_token = self._game.player

            good_move = self._game.place_move(row, col)

            if (good_move == False):
                self.render_message(INVALID_MSG)
                return 

            if (good_move and previous_token == X):
                self._screen.blit(self._x_img, location)

            elif (good_move and previous_token == O):
                self._screen.blit(self._o_img, location)

            pg.display.update()
        
        elif (row == None and (not(x <= 100 and y <= 450)) and (not(x >= 300 and y <= 450 ))):
            self.render_message(INVALID_MSG)
            return 

        # Check if anyone has won. If so, consider the game to be over.
        winner, direction, value = self._game.win_checker()
        if winner != 'N':
            self._draw_winning_line(direction, value)

        elif is_hotseat == 'CPU':
            # computer player's turn.
            # takes place immediately after a user input event is handled
            cpu = Cpu(self._game)
            cpu.printBoard()
            cpu_move = cpu.find_best_move()
        
            # checks winner
            row1 = cpu_move[0]
            col1 = cpu_move[1]
            
            location = GRID_OFFSETS[row1][col1]
            # Place the token
            previous_token = self._game.player

            good_move = self._game.place_move(row1 + 1, col1 + 1)

            if (good_move and previous_token == X):
                self._screen.blit(self._x_img, location)

            elif (good_move and previous_token == O):
                self._screen.blit(self._o_img, location)

            pg.display.update()
            # Check if anyone has won. If so, consider the game to be over.
            winner, direction, value = self._game.win_checker()

        if winner != 'N':
            self._draw_winning_line(direction, value)

        game_over = False

        if winner == DRAW:
            self.render_message(DRAW_MSG)
            game_over = True
        elif winner == UNDECIDED:
            pass
        else:
            if winner == X:
                self.render_message(WIN_MSG.format(self._player1.name))
            else:
                self.render_message(WIN_MSG.format(self._player2.name))
            game_over = True

        # If the game is over, reset and redraw the game.
        if game_over:
            if is_hotseat != 'CPU':
                # Swap the names of the players
                player1Name = self._player1.name
                player2Name = self._player2.name
                self._player1._change_name(player2Name)
                self._player2._change_name(player1Name)

            self._game.reset_game()
            self._draw_ui()

    def drawRowLine(self, row: int) -> None:
        '''
        Draw the winning line across the specified row.

        Paramters:
            row (int): The row number (1 to 3 inclusive).
        '''
        x_end = BOARD_X + BOARD_WIDTH
        y_offset = BOARD_Y + ((row - 1) * GRID_HEIGHT) + (GRID_HEIGHT // 2)

        start = (BOARD_X, y_offset)
        end = (x_end, y_offset)
        thickness = 4

        pg.draw.line(self._screen, RED, start, end, thickness)
        pg.display.update()


    def drawColumnLine(self, column: int) -> None:
        '''
        Draw the winning line down the specified column.

        Parameters:
            column (int): The column number (1 to 3 inclusive).
        '''
        x_offset = BOARD_X + ((column - 1) * GRID_WIDTH) + (GRID_WIDTH // 2)
        y_end = BOARD_Y + BOARD_HEIGHT

        start = (x_offset, BOARD_Y)
        end = (x_offset, y_end)
        thickness = 4

        pg.draw.line(self._screen, RED, start, end, thickness)
        pg.display.update()


    def drawDiagonalRTL(self) -> None:
        '''
        Draw the winning line diagonally from right to left.
        '''
        start = (BOARD_X + BOARD_WIDTH, BOARD_Y)
        end = (BOARD_X, BOARD_Y + BOARD_HEIGHT)
        thickness = 4

        pg.draw.line (self._screen, RED, start, end, thickness)
        pg.display.update()


    def drawDiagonalLTR(self) -> None:
        '''
        Draw the winning line diagonally from left to right.
        '''
        start = (BOARD_X, BOARD_Y)
        end = (BOARD_X + BOARD_WIDTH, BOARD_Y + BOARD_HEIGHT)
        thickness = 4

        pg.draw.line (self._screen, RED, start, end, thickness)


    def render_message(self, message: str) -> None:
        '''
        Render the status message in the status area.

        Parameters:
            message (str): The message to render.
        '''
        self._render_status_area()

        font_size = 30
        font = pg.font.Font(None, font_size)

        antialias = 1
        text = font.render(message, antialias, WHITE)

        x_center = (STATUS_X + STATUS_WIDTH) // 2
        y_center = STATUS_Y + STATUS_HEIGHT // 2
        center = (x_center, y_center)
        text_rect = text.get_rect(center=center)
        self._screen.blit(text, text_rect)

        pg.display.update()
        time.sleep(1)


    def _render_status_area(self) -> None:
        '''
        Render the status area at the bottom of the board
        '''
        status_rectangle = (STATUS_X, STATUS_Y, STATUS_WIDTH, STATUS_HEIGHT)
        self._screen.fill(BLACK, status_rectangle)
        pg.display.update()


    def _draw_ui(self) -> None:
        self._screen.fill(WHITE)

        # drawing vertical lines
        thickness = 7
        pg.draw.line(self._screen, RED, T12, (T32[0], T32[1] + GRID_HEIGHT), thickness)
        pg.draw.line(self._screen, RED, T13, (T33[0], T33[1] + GRID_HEIGHT), thickness)

        # drawing horizontal lines
        pg.draw.line(self._screen, RED, T21, (T23[0] + GRID_WIDTH, T23[1]), thickness)
        pg.draw.line(self._screen, RED, T31, (T33[0] + GRID_WIDTH, T33[1]), thickness)

        self._render_status_area()

        pg.display.update()

    def _draw_winning_line(self, direction, value) -> None:
        # drawing vertical lines
        thickness = 4
        if direction == "col":
            if value == "0":
                pg.draw.line(self._screen, BLUE, WC11, WC31, thickness)
            elif value == "1":
              pg.draw.line(self._screen, BLUE, WC12, WC32, thickness)  
            elif value == "2":
              pg.draw.line(self._screen, BLUE, WC13, WC33, thickness)  

        elif direction == "row":
            if value == "0":
                pg.draw.line(self._screen, BLUE, WR11, WR31, thickness)
            elif value == "1":
                pg.draw.line(self._screen, BLUE, WR12, WR32, thickness)  
            elif value == "2":
                pg.draw.line(self._screen, BLUE, WR13, WR33, thickness) 
                
        elif direction == "LTR":
            if value == "1":
                pg.draw.line(self._screen, BLUE, WD11, WD31, thickness)
        elif direction == "RTL":
            if value == "1":
                pg.draw.line(self._screen, BLUE, WD13, WD33, thickness)

