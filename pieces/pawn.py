from base_piece import BasePiece
from move import Move
from board import is_valid_square

class Pawn(BasePiece):
    def getMoves(self, r, c, moves, gameState):
        board = gameState.board
        if gameState.whiteToMove:
            if r > 0 and board[r - 1, c] == "--":
                moves.append(Move((r, c), (r - 1, c), board))
                if r == 4 and board[r - 2, c] == "--":
                    moves.append(Move((r, c), (r - 2, c), board))
            if c - 1 >= 0 and board[r - 1, c - 1][0] == 'b':
                moves.append(Move((r, c), (r - 1, c - 1), board))
            if c + 1 < 5 and board[r - 1, c + 1][0] == 'b':
                moves.append(Move((r, c), (r - 1, c + 1), board))
        else:
            if r < 5 and board[r + 1, c] == "--":
                moves.append(Move((r, c), (r + 1, c), board))
                if r == 1 and board[r + 2, c] == "--":
                    moves.append(Move((r, c), (r + 2, c), board))
            if c - 1 >= 0 and board[r + 1, c - 1][0] == 'w':
                moves.append(Move((r, c), (r + 1, c - 1), board))
            if c + 1 < 5 and board[r + 1, c + 1][0] == 'w':
                moves.append(Move((r, c), (r + 1, c + 1), board))