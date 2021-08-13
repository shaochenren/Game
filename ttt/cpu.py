import pygame as pg, sys
import copy

import random
from ttt.game import *

# custom type that shows the x and y coordinates of the cell (x,y).
_move = (int, int)

class Cpu:
    '''
    Provides functions and other tools for the computer player logic.

    '''

    def __init__(self, game: Game):
        '''
        Constructor for the Cpu class.

        Params:
            game (Game): Reference to a game object. A deep-copy is taken as an
            instance variable.
        '''
        # make a copy of the ongoing game instead of ruining it
        self._game = copy.deepcopy(game)
        self._board = self._game._board
        self._cpuPlayer = self._game._player

        self._opponent = X
        if(self._cpuPlayer == X):
            self._opponent = O
        elif self._cpuPlayer == O:
            self._opponent = X

    def printBoard(self):
        print("printing board")
        print(self._board)

    def find_best_move(self):
        '''
        Find the best possible move for the current game by starting the
        recursive _min_max() call chain.

        Returns:
            move (_move): A (row, col) list representing the best move.
        '''
        bestVal = -1000
        bestMove = (-1, -1)
    
        # Traverse all cells, evaluate minimax function for
        # all empty cells. And return the cell with optimal
        # value.
        for i in range(3) :    
            for j in range(3) :
            
                # Check if cell is empty
                if (self._board[i][j] is None) :
    

                    # Make the move
                    self._board[i][j] = self._cpuPlayer
    
                    # compute evaluation function for this
                    # move.
                    moveVal = self._min_max(0, False)
    
                    # Undo the move
                    self._board[i][j] = None
                    
                    # If the value of the current move is
                    # more than the best value, then update
                    # best/
                    if (moveVal > bestVal) :               
                        bestMove = (i, j)
                        bestVal = moveVal
    
        print("The value of the best Move is (tuple) :", bestMove)
        return bestMove
            

    def _min_max(self, depth: int, min_max: bool) -> int:
        '''
        Simulate all possible moves of the board and return the score once the
        simulation is finished.

        Parameters:
            depth (str): Current depth of the recursive call.
            min_max (bool): Whether the current run is being calculated for the
                            the maximizer

        Returns:
            score (int): Negative for minimizer win, positive for maximizer win.
        '''
        score = self._evaluate_game()
    
        # If Maximizer has won the game return his/her
        # evaluated score
        if (score == 10) :
            return score
    
        # If Minimizer has won the game return his/her
        # evaluated score
        if (score == -10) :
            return score
    
        # If there are no more moves and no winner then
        # it is a tie
        if (self.isMovesLeft() == False) :
            return 0
    
        # If this maximizer's move
        if (min_max) :    
            best = -1000
    
            # Traverse all cells
            for i in range(3) :        
                for j in range(3) :
                
                    # Check if cell is empty
                    if (self._board[i][j] is None) :
                    
                        # Make the move
                        self._board[i][j] = self._cpuPlayer
    
                        # Call minimax recursively and choose
                        # the maximum value
                        best = max( best, self._min_max(depth + 1, not min_max))
                           
                        # Undo the move
                        self._board[i][j] = None
            return best
    
        # If this minimizer's move
        else :
            best = 1000
    
            # Traverse all cells
            for i in range(3) :        
                for j in range(3) :
                
                    # Check if cell is empty
                    if (self._board[i][j] is None) :
                    
                        # Make the move
                        self._board[i][j] = self._opponent
    
                        # Call minimax recursively and choose
                        # the minimum value
                        best = min(best, self._min_max(depth + 1, not min_max))  

                        # Undo the move
                        self._board[i][j] = None
            return best


    def _evaluate_game(self) -> int:
        '''
        Evaluate the finished game and return an appropriate score.

        Returns:
            score (int): The score of the finished game.
                         - Negative = Minimizer wins
                         - Positive = Maximizer wins
                         - Zero = Draw (confirm this with Brandon
        '''
        # Checking for Rows for X or O victory.
        for row in range(3) :    
            if (self._board[row][0] == self._board[row][1] and self._board[row][1] == self._board[row][2]) :       
                if (self._board[row][0] == self._cpuPlayer) :
                    return 10
                elif (self._board[row][0] == self._opponent) :
                    return -10
    
        # Checking for Columns for X or O victory.
        for col in range(3) :
        
            if (self._board[0][col] == self._board[1][col] and self._board[1][col] == self._board[2][col]) :
            
                if (self._board[0][col] == self._cpuPlayer) :
                    return 10
                elif (self._board[0][col] == self._opponent) :
                    return -10
    
        # Checking for Diagonals for X or O victory.
        if (self._board[0][0] == self._board[1][1] and self._board[1][1] == self._board[2][2]) :
        
            if (self._board[0][0] == self._cpuPlayer) :
                return 10
            elif (self._board[0][0] == self._opponent) :
                return -10
    
        if (self._board[0][2] == self._board[1][1] and self._board[1][1] == self._board[2][0]) :
        
            if (self._board[0][2] == self._cpuPlayer) :
                return 10
            elif (self._board[0][2] == self._opponent) :
                return -10
    
        # Else if none of them have won then return 0
        return 0

    # this will return true if any cells are empty or it will return false
    def isMovesLeft(self) :
    
        for row in range(3) :
            for col in range(3) :
                if (self._board[row][col] is None) :
                    return True
        return False