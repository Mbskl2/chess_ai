from board import Board, field_to_indexes
from pieces import *
import pytest

def test_invalid_field():
    board = Board()
    board.reset()
    piece = board.board[0][0]
    with pytest.raises(Exception):
        board.put(piece, 'c53')
    with pytest.raises(Exception):
        board.put(piece, '')
    with pytest.raises(Exception):
        board.put(piece, 'x5')
    with pytest.raises(Exception):
        board.put(piece, 'c9')
        
def test_valid_put():
    # Given
    board = Board()
    board.reset()
    piece = board.board[0][0]
    # When
    board.put(piece, 'c5')
    # Then
    assert board.board[3][2] is piece
    
def test_put_on_occupied_field():
    board = Board()
    board.reset()
    piece = board.board[0][0]
    with pytest.raises(Exception):
        board.put(piece, 'c1')
    
def test_pawn_legal_moves_takes():
    board = Board()
    pawn = Pawn('white')
    other_piece = Pawn('black')
    put_piece(board, pawn, 'b2')
    put_piece(board, other_piece, 'a3')
    valid_moves = board.get_valid_moves_for('white')
    assert valid_moves == ['b3', 'bxa3']
    
def test_pawn_legal_moves_blocked():
    board = Board()
    pawn = Pawn('white')
    other_piece = Pawn('white')
    put_piece(board, pawn, 'b2')
    put_piece(board, other_piece, 'b3')
    valid_moves = board.get_valid_moves_for('white')
    assert valid_moves == ['b4']
        
def test_knight_legal_moves():
    board = Board()
    knight = Knight('white')
    put_piece(board, knight, 'b2')
    valid_moves = board.get_valid_moves_for('white')
    assert valid_moves == ['Na4', 'Nc4', 'Nd3', 'Nd1']
    
def put_piece(board: Board, piece: Piece, field: str):
    indexes = field_to_indexes(field)
    board.board[indexes[0]][indexes[1]] = piece
    