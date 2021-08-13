'''
Main driver for the game. 

Instantiates the Game object, handles user interactions, and draws the GUI.
'''

import pygame as pg

from ttt.game import Game
from ttt.colors import *
from ttt.board import *
from ttt.cpuselect import *
from ttt.playername import PlayerName

def main():
    player1 = PlayerName()
    player2 = PlayerName()
    select = CpuSelect()
    is_hotseat = select.is_hotseat()

    # Get the name of both players
    if(is_hotseat == OPT_HOTSEAT):
        player1._spawn_dialog()
        player2._spawn_dialog()
    else:
         player1._spawn_dialog()
         player2._change_name("CPU")

    game = Game()
    board = Board(game, player1, player2)
    board.run(is_hotseat)

if __name__ == '__main__':
    main()
