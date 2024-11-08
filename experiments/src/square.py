from piece import Piece

class Square:
    def __init__(self, row, col, piece = None):
        self.row = row
        self.col = col
        self.piece = piece

    def has_piece(self):
        return self.piece!= None 
    
    def isempty_or_rival(self, color):
        return self.is_empty() or self.has_rival_piece(color)

    def has_rival_piece(self, color):
        return self.has_piece and self.piece.color!= color
    
    def has_team_piece(self, color):
        return self.has_piece and self.piece.color == color

    def is_empty(self):
        return not self.has_piece()
    

    
    
    
    @staticmethod
    def in_range_row(*args):
        for arg in args:
            if arg < 0 or arg > 5:
                return False
            
        return True
    
    @staticmethod
    def in_range_col(*args):
        for arg in args:
            if arg < 0 or arg >4:
                return False
        return True