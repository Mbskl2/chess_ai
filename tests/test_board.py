from board import Board
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