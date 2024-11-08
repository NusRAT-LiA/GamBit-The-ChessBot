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
            #pass

        self.squares[row_other][0] = Square(row_other, 0, Rook(color) )
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
        self.squares[row_other][4] = Square(row_other, 4, King(color))

        self.squares[2][2] = Square(2,2, King('white'))


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

        def pawn_moves():
            steps = 1 #not allowing 2 step jump
            start = row + piece.direction
            end = row + (steps + 1)*piece.direction 

            for move_row in range(start, end, piece.direction):
                    if self.squares[move_row][col].is_empty():

                        initial = Square(row, col)
                        final = Square(move_row, col)

                        move = Move(initial, final)

                        piece.add_moves(move)
                    else:
                        break

            diagonal = [-1, 1]
            for d in diagonal:
                if Square.in_range_row(start) and Square.in_range_col(col + d):
                    if self.squares[start][col + d].has_piece():
                        if self.squares[start][col + d].has_rival_piece(piece.color):
                            initial = Square(row, col)
                            final = Square(start, col + d)

                            move = Move(initial, final)

                            piece.add_moves(move)

        def straightline_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr

                possible_move_row = row 
                possible_move_col = col 

                while True:
                    possible_move_row = possible_move_row + row_incr
                    possible_move_col = possible_move_col + col_incr

                    if Square.in_range_row(possible_move_row) and Square.in_range_col(possible_move_col):
                    
                        initial = Square(row,col)
                        final = Square(possible_move_row, possible_move_col)

                        move = Move(initial, final)
                    
                        if self.squares[possible_move_row][possible_move_col].is_empty():
                            piece.add_moves(move)
                        elif self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):
                            piece.add_moves(move)
                            break
                        else:
                            break
                    else:
                        break

        def king_moves():
            adjs = [
                (row, col - 1), (row, col + 1),
                (row +1, col -1), (row  + 1, col +1),
                (row -1, col -1), (row - 1, col + 1),
                (row + 1, col), (row - 1, col)
            ] 

            for possible_move in adjs:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range_row(possible_move_row) and Square.in_range_col(possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)

                        move = Move(initial, final)
                        piece.add_moves(move)        

        if isinstance(piece, Pawn):
            pawn_moves()

        if isinstance(piece, Bishop):
            straightline_moves(
                [(-1,1), (-1,-1), (1, 1), (1,-1)]
            )

        if isinstance(piece, Knight):
            knight_moves()

        if isinstance(piece,Rook):
            straightline_moves(
                [(-1, 0), (1,0), (0,1), (0,-1)]
            )

        if isinstance(piece, Queen):
            straightline_moves(
                [(-1, 0), (1,0), (0,1), (0,-1),
                 (-1,1), (-1,-1), (1, 1), (1,-1)]
            )

        if isinstance(piece, King):
            king_moves()

        
#b = Board()
#b._create()
