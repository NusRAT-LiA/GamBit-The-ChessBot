from .base_piece import BasePiece
from move import Move
from board import is_valid_square

class King(BasePiece):
    def getMoves(self, r, c, moves, gameState):
        king_moves = [
            (1, 0), (0, 1), (-1, 0), (0, -1),
            (1, 1), (1, -1), (-1, -1), (-1, 1)
        ]
        for move in king_moves:
            endRow = r + move[0]
            endCol = c + move[1]
            if is_valid_square(endRow, endCol):
                endPiece = gameState.board[endRow, endCol]
                if endPiece == "--":
                    moves.append(Move((r, c), (endRow, endCol), gameState.board))
                elif endPiece[0] != gameState.board[r, c][0]:  # Capture opponent's piece
                    moves.append(Move((r, c), (endRow, endCol), gameState.board))
