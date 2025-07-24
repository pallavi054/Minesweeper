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
#game = MinesweeperBoard(level='intermediate')


from GameLogic import *

def main():
    print("Welcome to Console Minesweeper!")
    diff = input("Please select a difficulity level: beginner, intermediate, expert\n")
    game = GameLogic(diff)  # start the game
    game.run()

if __name__ == "__main__":
 main()
