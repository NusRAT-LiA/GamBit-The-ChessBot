class Piece:
    def __init__(self,name, color, value, texture = None, texture_rect = None ):
        self.name = name
        self.color = color

        value_sign = 1 if color == 'white' else -1
        self.value = value_sign*value
        self.texture = texture

        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture():
        


class pawn(Piece):

    def __init__(self,color):
        if(color == 'white'):
            self.direction = -1
        else:
            self.direction = 1


        super().__init__('Pawn',color, 1.0,)


class Knight(Piece):

    def __init__(self, color):

        super().__init__('knight', color, 3.0)

class Bishop(Piece):

    def __init__(self, color):
        super().__init__('Bishop', color, 3.0)


class Rook(Piece):

    def __init__(self, color):
        super().__init__('Rook',color, 5.0)


class Queen(Piece):

    def __init__(self,color):
        super().__init__('Queen', color, 9.0)


class King(Piece):
    def __init__(self,color):
        super().__init__('King', color, 1000.0)