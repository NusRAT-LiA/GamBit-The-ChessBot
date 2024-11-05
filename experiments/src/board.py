from const import *
from square import Square
class Board:
    def __init__(self):
        self.squares = [[0,0,0,0,0] for row in range(ROWS)]
        self._create()
        
    def _create(self): #private method
        
        
        for row in range(ROWS):
            for col in range(COLS):
               self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color): #private method
        pass


b = Board()
b._create()
