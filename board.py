import tkinter as tk
import uuid

class Board:
    field_color_black = '#b16e41'
    field_color_white = '#ffd599'
    field_size = 100
    
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=Board.field_size * 8, height=Board.field_size * 8)
        self.canvas.pack()
        
        self.board = [[None] * 8] * 8
        self.rendered_pieces = {}
    
    def reset(self) -> None:
        br1 = Piece('black', 'rook')
        bk1 = Piece('black', 'knight')
        bb1 = Piece('black', 'bishop')
        bq = Piece('black', 'queen')
        bking = Piece('black', 'king')
        bb2 = Piece('black', 'bishop')
        bk2 = Piece('black', 'knight')
        br2 = Piece('black', 'rook')

        bp1 = Piece('black', 'pawn')
        bp2 = Piece('black', 'pawn')
        bp3 = Piece('black', 'pawn')
        bp4 = Piece('black', 'pawn')
        bp5 = Piece('black', 'pawn')
        bp6 = Piece('black', 'pawn')
        bp7 = Piece('black', 'pawn')
        bp8 = Piece('black', 'pawn')

        wr1 = Piece('white', 'rook')
        wk1 = Piece('white', 'knight')
        wb1 = Piece('white', 'bishop')
        wq = Piece('white', 'queen')
        wking = Piece('white', 'king')
        wb2 = Piece('white', 'bishop')
        wk2 = Piece('white', 'knight')
        wr2 = Piece('white', 'rook')

        wp1 = Piece('white', 'pawn')
        wp2 = Piece('white', 'pawn')
        wp3 = Piece('white', 'pawn')
        wp4 = Piece('white', 'pawn')
        wp5 = Piece('white', 'pawn')
        wp6 = Piece('white', 'pawn')
        wp7 = Piece('white', 'pawn')
        wp8 = Piece('white', 'pawn')

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
                
class Piece:
    def __init__(self, color, type) -> None:
        self.color = color
        self.type = type
        self.guid = uuid.uuid4()
        
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Piece):
            return False
        return self.guid == value.guid
    
    def __hash__(self) -> int:
        return self.guid.__hash__()