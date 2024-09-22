import uuid

class Piece:
    def __init__(self, color, type, symbol) -> None:
        self.color = color
        self.type = type
        self.guid = uuid.uuid4()
        self.symbol = symbol
        
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Piece):
            return False
        return self.guid == value.guid
    
    def __hash__(self) -> int:
        return self.guid.__hash__()
    
class Pawn(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, 'pawn', '')

class Rook(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, 'rook', 'R')
    
class Knight(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, 'knight', 'N')
        
class Bishop(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, 'bishop', 'B')
        
class Queen(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, 'queen', 'Q')
        
class King(Piece):
    def __init__(self, color) -> None:
        super().__init__(color, 'king', 'K')