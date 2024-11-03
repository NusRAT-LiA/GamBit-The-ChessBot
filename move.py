# move.py

class Move:

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow, self.startCol]
        self.pieceCaptured = board[self.endRow, self.endCol]
        self.is_pawn_promotion = (self.pieceMoved == "wp" and self.endRow == 0) or (self.pieceMoved == "bp" and self.endRow == 5)

    def is_capture(self):
        return self.pieceCaptured is not None

    # def __eq__(self, other):
    #     if isinstance(other, Move):
    #         return self.moveId == other.moveId
    #     return False

    # def getChessNotation(self):
    #     return f"{self.getRankFile(self.startRow, self.startCol)}->{self.getRankFile(self.endRow, self.endCol)}"

    # def getRankFile(self, r, c):
    #     return self.colsToFiles[c] + self.rowsToRanks[r]
