# game_state.py
import numpy as np
from board import is_valid_square
from move import Move
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King

class GameState:
    def __init__(self):
        self.board = np.array([
            ["bR", "bN", "bB", "bQ", "bK"],
            ["bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK"],
        ], dtype=object)
        self.whiteToMove = True
        self.moveLog = []
        self.whiteKingLocation = (5, 4)
        self.blackKingLocation = (0, 4)
        self.checkMate = False
        self.staleMate = False

    def makeMove(self, move):
        self.board[move.startRow, move.startCol] = "--"
        self.board[move.endRow, move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove

        if move.pieceMoved == 'bK':
            self.blackKingLocation = (move.endRow, move.endCol)
        elif move.pieceMoved == 'wK':
            self.whiteKingLocation = (move.endRow, move.endCol)

        if move.is_pawn_promotion:
            self.board[move.endRow, move.endCol] = move.pieceMoved[0] + "Q"

    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow, move.startCol] = move.pieceMoved
            self.board[move.endRow, move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove
            if move.pieceMoved == 'bK':
                self.blackKingLocation = (move.startRow, move.startCol)
            elif move.pieceMoved == 'wK':
                self.whiteKingLocation = (move.startRow, move.startCol)

    def getValidMoves(self):
        moves = self.getAllPossibleMoves()
        for i in range(len(moves) - 1, -1, -1):
            self.makeMove(moves[i])
            self.whiteToMove = not self.whiteToMove
            if self.inCheck():
                moves.remove(moves[i])
            self.whiteToMove = not self.whiteToMove
            self.undoMove()
        return moves

    def getAllPossibleMoves(self):
        moves = []
        for r in range(6):
            for c in range(5):
                piece = self.board[r, c][1]
                if (self.board[r, c][0] == 'w' and self.whiteToMove) or (self.board[r, c][0] == 'b' and not self.whiteToMove):
                    if piece == 'p':
                        Pawn().getMoves(r, c, moves, self)
                    elif piece == 'R':
                        Rook().getMoves(r, c, moves, self)
                    elif piece == 'N':
                        Knight().getMoves(r, c, moves, self)
                    elif piece == 'B':
                        Bishop().getMoves(r, c, moves, self)
                    elif piece == 'Q':
                        Queen().getMoves(r, c, moves, self)
                    elif piece == 'K':
                        King().getMoves(r, c, moves, self)
        return moves

    def squareAttack(self, r, c):
        self.whiteToMove = not self.whiteToMove
        oppMoves = self.getAllPossibleMoves()
        self.whiteToMove = not self.whiteToMove
        for move in oppMoves:
            if move.endRow == r and move.endCol == c:
                return True
        return False

    def inCheck(self):
        if self.whiteToMove:
            return self.squareAttack(self.whiteKingLocation[0], self.whiteKingLocation[1])
        else:
            return self.squareAttack(self.blackKingLocation[0], self.blackKingLocation[1])
