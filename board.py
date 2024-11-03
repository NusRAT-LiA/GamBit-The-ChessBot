import numpy as np

BOARD_ROWS = 6
BOARD_COLS = 5


class Board:
    def __init__(self):
        self.grid = np.array([
            ["bR", "bN", "bB", "bQ", "bK"],
            ["bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK"],
        ], dtype=object)

    def get_square(self, row, col):
        if 0 <= row < BOARD_ROWS and 0 <= col < BOARD_COLS:
            return self.grid[row, col]
        return None

    def set_square(self, row, col, piece):
        if 0 <= row < BOARD_ROWS and 0 <= col < BOARD_COLS:
            self.grid[row, col] = piece

    def is_empty_square(self, row, col):
        return self.get_square(row, col) == "--"
    
    def is_valid_square(row, col):
        return 0 <= row < BOARD_ROWS and 0 <= col < BOARD_COLS
