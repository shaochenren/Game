import pytest
import pygame as pg, sys
from ttt.colors import WHITE
from ttt.dimensions import BOARD_WIDTH as width, BOARD_HEIGHT as height, TTT as board
from ttt.board import Board
from ttt.game import Game


def test_update_board() -> None:
    '''
    Test the update board action in the game board.

    '''
    board = [[None, None, None], [None, None, None], [None, None, None]]
    pass

def test_check_column_win() -> None:
    '''
    Test the column win scenario in the game board.

    '''
    board = [['O', 'O', 'O'], [None, None, None], [None, None, None]]
    game = Game()
    game._board = board
    winner, direction, value = game.win_checker()
    assert winner == 'o'

def test_check_row_win() -> None:
    '''
    Test the row win scenario in the game board.

    '''
    board = [['X', None, None], ['X', None, None], ['X', None, None]]
    game = Game()
    game._board = board
    winner, direction, value = game.win_checker()
    assert winner == 'x'

def test_check_first_diagonal_win() -> None:
    '''
    Test the first diagonal win scenario in the game board.

    '''
    board = [['X', None, None], [ None, 'X', None], [None, None, 'X']]
    game = Game()
    game._board = board
    winner, direction, value = game.win_checker()
    assert winner == 'x'

def test_check_second_diagonal_win() -> None:
    '''
    Test the second diagonal win scenario in the game board.

    '''
    board = [[None, None, 'O'], [None, 'O', None], ['O', None, None]]
    game = Game()
    game._board = board
    winner, direction, value = game.win_checker()
    assert winner == 'o'

