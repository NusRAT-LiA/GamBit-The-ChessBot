import os
#from abc import ABC, abstractmethod


class Piece():
    def __init__(self,name, color, value, texture = None, texture_rect = None ):

        self.name = name
        self.color = color

        value_sign = 1 if color == 'white' else -1
        self.value = value_sign*value

        self.texture = texture
        self.set_texture(80)

        self.texture_rect = texture_rect

        self.moves = []
        self.moved = False

    def set_texture(self,size):
        self.texture = os.path.join(
            #f'/home/nafis/Desktop/GamBit-The-ChessBot/experiments/assets/images/imgs-{size}px/{self.color}_{self.name}.png'
            f'experiments/assets/images/imgs-{size}px/{self.color}_{self.name}.png'
        )

    def add_moves(self, move):
        self.moves.append(move)


""" 
class Pawn(Piece):

    def __init__(self,color):
        if(color == 'white'):
            self.direction = -1
        else:
            self.direction = 1


        super().__init__('pawn',color, 1.0)




class Knight(Piece):

    def __init__(self, color):

        super().__init__('knight', color, 3.0)



class Bishop(Piece):

    def __init__(self, color):
        super().__init__('bishop', color, 3.0)


class Rook(Piece):

    def __init__(self, color):
        super().__init__('rook',color, 5.0)


class Queen(Piece):

    def __init__(self,color):
        super().__init__('queen', color, 9.0)


class King(Piece):
    def __init__(self,color):
        super().__init__('king', color, 1000.0)
"""