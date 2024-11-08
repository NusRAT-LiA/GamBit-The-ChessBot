from const import *
from square import Square
from piece import *

from import_all_pieces import *

from move import Move

class Board:
    def __init__(self):
        self.squares = [[0,0,0,0,0] for row in range(ROWS)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

        #test
        #self.move_calculation = Move_Calculation()

    def _create(self): #private method
        
        
        for row in range(ROWS):
            for col in range(COLS):
               self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color): #private method
        row_pawn, row_other = (4,5) if color == 'white' else (1,0)

        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color) )

        self.squares[row_other][0] = Square(row_other, 0, Rook(color) )
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
        self.squares[row_other][4] = Square(row_other, 4, King(color))


    def calc_moves(self, piece, row, col):

        def knight_moves():
            possible_moves = [(row -2,col -1), (row - 2, col + 1), (row + 2, col - 1), (row + 2, col + 1),
                            (row -1, col - 2), (row - 1, col + 2),(row +1, col - 2), (row + 1, col +2)]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range_row(possible_move_row) and Square.in_range_col(possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                       
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        
                        
                        move = Move(initial, final)
                        piece.add_moves(move)

        
        if isinstance(piece, Pawn):
            pass

        if isinstance(piece, Bishop):
            pass

        if isinstance(piece, Knight):
            knight_moves()

        if isinstance(piece,Rook):
            pass

        if isinstance(piece, Queen):
            pass

        if isinstance(piece, King):
            pass

        
#b = Board()
#b._create()
