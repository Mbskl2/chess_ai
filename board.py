import tkinter as tk
from pieces import *


class Board:
    field_color_black = '#b16e41'
    field_color_white = '#ffd599'
    field_size = 100
    
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=Board.field_size * 8, height=Board.field_size * 8)
        self.canvas.pack()
        
        self.board = [[None] * 8, [None] * 8, [None] * 8, [None] * 8, [None] * 8, [None] * 8, [None] * 8, [None] * 8]
        self.rendered_pieces = {}
    
    def reset(self) -> None:
        br1 = Rook('black')
        bk1 = Knight('black')
        bb1 = Bishop('black')
        bq = Queen('black')
        bking = King('black')
        bb2 = Bishop('black')
        bk2 = Knight('black')
        br2 = Rook('black')

        bp1 = Pawn('black')
        bp2 = Pawn('black')
        bp3 = Pawn('black')
        bp4 = Pawn('black')
        bp5 = Pawn('black')
        bp6 = Pawn('black')
        bp7 = Pawn('black')
        bp8 = Pawn('black')

        wr1 = Rook('white')
        wk1 = Knight('white')
        wb1 = Bishop('white')
        wq = Queen('white')
        wking = King('white')
        wb2 = Bishop('white')
        wk2 = Knight('white')
        wr2 = Rook('white')

        wp1 = Pawn('white')
        wp2 = Pawn('white')
        wp3 = Pawn('white')
        wp4 = Pawn('white')
        wp5 = Pawn('white')
        wp6 = Pawn('white')
        wp7 = Pawn('white')
        wp8 = Pawn('white')

        self.board = [
            [br1, bk1, bb1, bq, bking, bb2, bk2, br2],
            [bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8],
            [wr1, wk1, wb1, wq, wking, wb2, wk2, wr2],
        ]
        
    def put(self, piece: Piece, field: str):
        indexes = field_to_indexes(field)
        piece_on_field = self.board[indexes[0]][indexes[1]]
        assert piece_on_field is None, f'Field already taken by {piece_on_field.color} {piece_on_field.type}'
        
        self.board[indexes[0]][indexes[1]] = piece
        
    def get_valid_moves_for(self, color: str) -> list[str]:
        assert color == 'white' or color == 'black'
        pieces = [
            piece 
            for row in self.board 
            for piece in row 
            if piece is not None and piece.color == color]
        assert len(pieces) >= 1
        moves = [
            move
            for piece in pieces
            for move in self.get_valid_moves_for_piece(piece)
        ]
        return moves
            
    
    def get_valid_moves_for_piece(self, piece: Piece) -> list[str]:
        coordinates = self.get_coordinates(piece)
        moves = []
        if piece.type is 'pawn':
                        
            direction = -1 if piece.color == 'white' else +1
            if self.board[coordinates[0] + direction][coordinates[1]] == None:
                moves.append(indexes_to_field(coordinates[0] + direction, coordinates[1]))
                
            left_take_coords = coordinates[0] + direction, coordinates[1] - 1
            if (left_take_coords[1] >= 0 
                and self.board[left_take_coords[0]][left_take_coords[1]] != None 
                and self.board[left_take_coords[0]][left_take_coords[1]].color != piece.color):
                prefix = indexes_to_field(coordinates[0], coordinates[1])[0] + 'x'
                move = prefix + indexes_to_field(left_take_coords[0], left_take_coords[1])
                moves.append(move)
                
            right_take_coords = coordinates[0] + direction, coordinates[1] + 1
            if (right_take_coords[1] <= 7 
                and self.board[right_take_coords[0]][right_take_coords[1]] != None 
                and self.board[right_take_coords[0]][right_take_coords[1]].color != piece.color):
                prefix = indexes_to_field(coordinates[0], coordinates[1])[0] + 'x'
                move = prefix + indexes_to_field(right_take_coords[0], right_take_coords[1])
                moves.append(move)
            
            return moves
        return []
    
    def get_coordinates(self, piece: Piece) -> tuple[int, int]:
        for row in range(8):
            for file in range(8):
                if self.board[row][file] == piece:
                    return (row, file)
        raise Exception(f'Cannot find piece {piece.color} {piece.type}')
    
    def render(self) -> None:
        self.render_fields(self.canvas)
        self.render_pieces(self.board, self.canvas)
        
        # canvas.delete('all')
        self.root.mainloop()

    def render_pieces(self, board, canvas) -> None:
        for i in range(8):
            for j in range(8):
                piece = board[i][j]
                if piece == None:
                    continue
            
                path = './Assets/' + piece.color + '-' + piece.type + '.png'
                img = tk.PhotoImage(file = path)
                self.rendered_pieces[piece] = img # if the img goes out of scope, it disappears from the canvas
                canvas.create_image(j * Board.field_size + 50, i * Board.field_size + 50, image = img)

    def render_fields(self, canvas) -> None:
        for i in range(8):
            for j in range(8):
                color = [Board.field_color_black, Board.field_color_white][(i+j) % 2]
                canvas.create_rectangle(i*Board.field_size, j*Board.field_size, (i+1)*Board.field_size, (j+1)*Board.field_size, fill=color)
            
def field_to_indexes(field: str) -> tuple[int, int]:
    assert len(field) == 2, f'Invalid field: {field}'
    file = field[0]
    assert 'a' <= file <= 'h', f'Invalid field: {field}'
    row = field[1]
    assert '1' <= row <= '8', f'Invalid field: {field}'
    file_index = ord(file) - ord('a')
    row_index = 8 - int(row)
    return row_index, file_index

def indexes_to_field(row_index: int, file_index: int) -> str:
    file = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][file_index]
    row = 8 - row_index
    return file + str(row)