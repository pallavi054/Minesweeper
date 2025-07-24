# =============================================================================
# Name        : PlayMinesweeper.py
# Author      : Ojan Salemi & Pallavi Aggarwal
# Version     : 7/23/2025
# Description : This test driver initiates a game of Minesweeper in the console.
#               The user specifies the difficulty level (beginner, intermediate, 
#               or expert) and a board is generated for play.
# =============================================================================
from GameLogic import GameLogic

def main():
    print("Welcome to Console Minesweeper!")
    diff = input("\nPlease select a difficulity level: beginner, intermediate, expert\n")
    game = GameLogic(diff)  # start the game (default game is beginner level)
    game.run()

if __name__ == "__main__":
 main()
