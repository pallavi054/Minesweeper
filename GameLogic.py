# =============================================================================
# Name        : GameLogic.py
# Author      : Ojan Salemi
# Version     : 7/21/2025
# Description : This class defines the logic of Minesweeper gameplay. This
#               class allows the user to reveal cells and set flags, in addition
#               to describing winning and losing conditions of the game. The
#               user wins if all the cells are opened, all the suspected mines
#               are flagged, and no mines are opened.
# =============================================================================
from MinesweeperBoard import *
from collections import deque

class GameLogic:

    REVEAL = "reveal"
    FLAG = "flag"
    QUIT = "quit"
    NEW_GAME = "new"

    #Takes a level (either 'beginner', 'intermediate', or 'advanced') and initializes the game.
    def __init__(self, level='beginner'):
        self.level = level
        self.board = MinesweeperBoard(level)
        self.first_move_done = False
        self.running = True


    #Game loop driver. Asks the user for their commands in each turn.
    def run(self):
        self.board.display_board()
        while self.running:
            command = input("Use 'R row col' to reveal a cell, 'F row col' to place a flag, or 'N' to reset the game.\n")
            self.process_turn(command)


    #Takes a string command from the user, processes it and updates the game's state.
    def process_turn(self, raw_command):
        try:
            action, row, col = self.parse_input(raw_command)
        except ValueError as error_message:
            print(error_message)

        if action == self.QUIT:
            self.running = False
            print("Thanks for playing!")
            return
        elif action == self.NEW_GAME:
            print("Restarting the game.")
            self.first_move_done = False
            self.board = MinesweeperBoard(self.level)
            self.board.display_board()
            return
        elif action == self.REVEAL:
            if not self.first_move_done:
                self.board.start_timer()
                self.first_move_done = True
            self.reveal_cell(row, col)
        elif action == self.FLAG:
            self.plant_flag(row, col)

        if self.running:
            self.board.display_board()

    #Takes a raw command from the user, processes it, and returns (action, row, column) to be used in process_turn().
    def parse_input(self, raw_command):
        if not raw_command.strip():
            raise ValueError("Emtpy command. Please enter a command.")

        command_parts = raw_command.lower().split()
        token = command_parts[0]


        if token == "q" or token == "quit":
            return self.QUIT, None, None
        elif token == "n":
            return self.NEW_GAME, None, None
        elif token == "r":
            action = self.REVEAL
        elif token == "f":
            action = self.FLAG
        else:
            raise ValueError("Unknown command.")

        if len(command_parts) != 3:
            raise ValueError("Invalid command.")


        try:
            row = int(command_parts[1]) - 1 #minus one because the coordinates for the users start with 1
            col = int(command_parts[2]) - 1
        except:
            raise ValueError("Row and/or column not entered correctly.")

        if row < 0 or col < 0 or row >= self.board.rows or col >= self.board.cols:
            raise ValueError("Out of range.")

        return action, row, col


    #Takes a row and column, reveals it, and handles the consequence according to the game's logic.
    def reveal_cell(self, row, col):
        #Already revealed or flagged
        if self.board.revealed[row][col] or self.board.flags[row][col]:
            return

        #Mine opened
        if self.board.mine_positions[row][col]:
            for i in range(self.board.rows):
                for j in range(self.board.cols):
                    if self.board.mine_positions[i][j]:
                        self.board.revealed[i][j] = True
            self.board.stop_timer()
            self.board.smiley = "☹️"
            self.running = False
            self.board.display_board()
            print("Boom!")
            print("Time passed: " + str(self.board.get_elapsed_time))
            return

        #BFS reveal
        queue = deque([(row, col)])
        while queue:
            print(str(queue))
            queue_row, queue_col = queue.popleft()
            if self.board.revealed[queue_row][queue_col]:
                print("revealed?")
                continue
            self.board.revealed[queue_row][queue_col] = True

            if self.board.board[queue_row][queue_col] == "0":
                print("zero?")
                for diff_row in (-1, 0, 1):
                    for diff_col in (-1, 0, 1):
                        if diff_row == 0 and diff_col == 0:
                            continue
                        new_row = queue_row + diff_row
                        new_col = queue_col + diff_col

                        if 0 <= new_row <self.board.rows and 0 <= new_col < self.board.cols:
                            if not self.board.revealed[new_row][new_col] and not self.board.flags[new_row][new_col]:
                                queue.append((new_row, new_col))
            print(str(queue))
        self.check_win()

        #Takes a row and column position and plants a flag on that cell.
    def plant_flag(self, row, col):
        if self.board.revealed[row][col]:
            print("Already revealed. Cannot plant a flag here.")
            return

        #removing flag
        if self.board.flags[row][col]:
            self.board.flags[row][col] = False
            self.board.flag_count -= 1
        else:
            if self.board.flag_count >= self.board.num_mines:
                print("All flags have been planted. No flags remaining.")
                return
            self.board.flags[row][col] = True
            self.board.flag_count += 1
        self.check_win()

    #Checks to see if the user has won.
    def check_win(self):
        clear_total = self.board.rows * self.board.cols - self.board.num_mines
        revealed_total = 0
        for row in self.board.revealed:
            for cell in row:
                if cell:
                    revealed_total += 1

        if revealed_total == clear_total:
            self.board.stop_timer()
            self.board.smiley = "😎"
            self.running = False
            self.board.display_board()
            print("Congratulations! You cleared all the mines!")
            print("Time passed: " + str(self.board.get_elapsed_time()) + " seconds")
