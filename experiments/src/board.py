from const import *
from square import Square
from piece import *

class Board:
    def __init__(self):
        self.squares = [[0,0,0,0,0] for row in range(ROWS)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def _create(self): #private method
        
        
        for row in range(ROWS):
            for col in range(COLS):
               self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color): #private method
        row_pawn, row_other = (4,5) if color == 'white' else (1,0)

        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color) )

        self.squares[row_other][0] = Square(row_other,col, Rook(color) )
        self.squares[row_other][1] = Square(row_other, col, Knight(color))
        self.squares[row_other][2] = Square(row_other, col, Bishop(color))
        self.squares[row_other][3] = Square(row_other, col, Queen(color))
        self.squares[row_other][4] = Square(row_other, col, King(color))

#b = Board()
#b._create()
