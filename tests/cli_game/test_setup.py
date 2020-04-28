import pydealer as dealer

def test_create_deck():
    deck = dealer.Deck()
    deck.shuffle()
    assert len(deck) == 52

def test_create_board():
    board = [[0] * 5 for i in range(5)]
    assert board == 5
    assert len(board[1]) == 5

