import pydealer as dealer

def create_deck():
    deck = dealer.Deck()
    deck.shuffle()
    return deck

def create_board():
    # Data representation for the board using a list generator
    board = [[0] * 5 for i in range(5)]
    board[2][2] = 'x'
    return board