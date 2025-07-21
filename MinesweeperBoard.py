# =============================================================================
# Name        : MinesweeperBoard.py
# Author      : Pallavi Aggarwal
# Version     : 7/20/2025
# Description : This class initializes a Minesweeper board that supports game 
#               logic. The default board is of size 9x9 with 10 randomly placed
#               mines. The board is associated with 10 flags that the user can
#               use to mark the suspected mines. This class contains methods
#               to display the board cells and the number of adjacent mines.
# =============================================================================
import random  # to randomly place mines
import time    # to time user's gameplay

class MinesweeperBoard:
    # Parameters for different gameplay levels
    LEVELS = {
        'beginner': {'rows': 9,  'cols': 9,  'mines': 10},
        'intermediate': {'rows': 16, 'cols': 16, 'mines': 40},
        'expert': {'rows': 16, 'cols': 30, 'mines': 99}
    }

    def __init__(self, level='beginner'):  # default is beginner level
        config = MinesweeperBoard.LEVELS.get(level, MinesweeperBoard.LEVELS['beginner'])
        self.rows = config['rows']
        self.cols = config['cols']
        self.num_mines = config['mines']

        self.board = [[' ' for j in range(self.cols)] for i in range(self.rows)]
        self.revealed = [[False for j in range(self.cols)] for i in range(self.rows)]
        self.flags = [[False for j in range(self.cols)] for i in range(self.rows)]
        self.mine_positions = [[False for j in range(self.cols)] for i in range(self.rows)]

        self.start_time = None
        self.end_time = None
        self.flag_count = 0
        self.game_over = False
        self.smiley = "🙂"  # this is a classic hallmark of Minesweeper!

        self.place_mines()
        self.calculate_numbers()
    
    # Use random number generation to place the mines on the board
    def place_mines(self):
        placed = 0
        while placed < self.num_mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if not self.mine_positions[row][col]:
                self.mine_positions[row][col] = True
                placed += 1

    # Helper function to count the number of mines adjacent to the cell
    def count_adjacent_mines(self, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
        count = 0
        for dir_row, dir_col in directions:
            new_row = row + dir_row
            new_col = col + dir_col
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                if self.mine_positions[new_row][new_col]:
                    count += 1
        return count
    
    # Calculate the numbers filling in each cell on the board
    def calculate_numbers(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.mine_positions[row][col]:
                    self.board[row][col] = '×'  # symbol representing a mine
                else:
                    self.board[row][col] = str(self.count_adjacent_mines(row, col))

    # Display the Minesweeper board
    def display_board(self):
        # Info line at the top
        print(f"\n\tFlags remaining: {self.num_mines - self.flag_count}    {self.smiley}       \n")
    
        # Centered column headers
        print("    " + " ".join(f"{str(i + 1).center(3)}" for i in range(self.cols)))    
        
        # Top border of the board
        print("   ┌" + "───┬" * (self.cols - 1) + "───┐")
    
        for i in range(self.rows):
            row_str = f"{str(i + 1).rjust(2)} │"
            for j in range(self.cols):
                if self.flags[i][j]:
                    cell = "F"
                elif self.revealed[i][j]:
                    cell = self.board[i][j]
                else:
                    cell = "."
                cell_display = cell.center(3)
                row_str += f"{cell_display}│"
            print(row_str)

            if i < self.rows - 1:
                print("   ├" + "───┼" * (self.cols - 1) + "───┤")
            else:
                print("   └" + "───┴" * (self.cols - 1) + "───┘")
    
    # Starts the timer for the user's gameplay session
    def start_timer(self):
        self.start_time = time.time()

    # Stops the timer for the user's gameplay session
    def stop_timer(self):
        self.end_time = time.time()

    # Calculates elapsed time (in seconds) for the user's gameplay session
    def get_elapsed_time(self):
        if self.start_time and self.end_time:
            return round(self.end_time - self.start_time, 2)
        return 0.0

    # Resets the Minesweeper board for new games
    def reset_board(self, level='beginner'):
        self.__init__(level)
        self.smiley = "🙂"  # reset default smiley face
