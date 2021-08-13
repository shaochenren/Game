import pytest
from ttt.board import Board
from ttt.cpu import Cpu

# Test the best move the CPU can do
def test_find_best_move():
    cpu = Cpu()
    board = Board()
    cpu_move = cpu.find_best_move()
    pass

# Test the AI to consider all possible scenarios and makes the most optimal move
def test_min_max():
    cpu = Cpu()
    board = Board()
    pass

# Test for when we evaluate the finished game
def test_evaluate_game():
    cpu = Cpu()
    board = Board()
    pass
