from abc import ABC, abstractmethod

class BasePiece(ABC):
    @abstractmethod
    def getMoves(self, r, c, moves, gameState):
        pass