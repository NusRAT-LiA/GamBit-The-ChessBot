class Move:
   
    def __init__(self, start_sq: tuple[int, int], end_sq: tuple[int, int], board: list[list[str]]):
        self.start_row, self.start_col = start_sq
        self.end_row, self.end_col = end_sq
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]

   
    @property
    def is_pawn_promotion(self) -> bool:
        """
        Check if this move results in a pawn promotion.
        """
        return (self.piece_moved == "wp" and self.end_row == 0) or \
               (self.piece_moved == "bp" and self.end_row == 5)

    @property
    def is_capture(self) -> bool:
        """
        Determine if this move is a capture.
        """
        return self.piece_captured != "--"  

   