import tkinter as tk
import PIL as pil
from board import Board

# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Unrestricted
# .\Scripts\Activate.ps1
#
#

if __name__ == '__main__':
    board = Board()
    board.reset()
    board.render()