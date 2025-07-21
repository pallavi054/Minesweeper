# =============================================================================
# Name        : PlayMinesweeper.py
# Author      : Ojan Salemi & Pallavi Aggarwal
# Version     : 7/21/2025
# Description : ...
# =============================================================================

from MinesweeperBoard import *

# Create a Minesweeper board
# game = MinesweeperBoard(level='expert')
# game = MinesweeperBoard(level='beginner')
game = MinesweeperBoard(level='intermediate')

# Start the game timer
game.start_timer()

# Display the board
game.display_board()

# =============================================================================
# TO CALL GAMELOGIC CLASS AFTER IT'S DONE
# from GameLogic import *
# 
# def main():
#     print("Welcome to Console Minesweeper!")
#     print("Use 'R row col' to reveal a cell, 'F row col' to place a flag, or 'N' to reset the game.\n")
# 
#     GameLogic()  # start the game
# 
# if __name__ == "__main__":
#     main()
# =============================================================================