from base_piece import BasePiece
from move import Move
from board import is_valid_square

class Queen(BasePiece):
    def getMoves(self, r, c, moves, gameState):
        directions = [
            (0, 1), (1, 0), (0, -1), (-1, 0),  # rook directions
            (1, 1), (1, -1), (-1, -1), (-1, 1)  # bishop directions
        ]
        for d in directions:
            for i in range(1, 6):
                endRow = r + d[0] * i
                endCol = c + d[1] * i
                if is_valid_square(endRow, endCol):
                    endPiece = gameState.board[endRow, endCol]
                    if endPiece == "--":
                        moves.append(Move((r, c), (endRow, endCol), gameState.board))
                    elif endPiece[0] != gameState.board[r, c][0]:  # Capture opponent's piece
                        moves.append(Move((r, c), (endRow, endCol), gameState.board))
                        break  # Can't move further in this direction
                    else:
                        break  # Can't move if there's a friendly piece
                else:
                    break  # Out of bounds